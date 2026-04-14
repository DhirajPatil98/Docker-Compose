import os
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template( 
        "index.html", 
        app_version=os.environ.get('APP_VERSION'), 
        db_password=os.environ.get('db_PASSWORD'), 
        app_token=os.environ.get('APP_TOKEN') )

@app.route('/about', methods=['GET'])
def about():
    
    #version = '1.0.0'    # this is hardcoding the value, we can use environment variable instead.

    version = os.environ.get('APP_VERSION')

    #return f 'Flask App Version: {version}'

    return {'version': version}, 200

@app.route('/secret', methods=['GET'])
def secret():

    creds = dict()

    creds['DB_PASSWORD'] = os.environ.get('db_PASSWORD')
    creds['APP_TOKEN'] = os.environ.get('APP_TOKEN') 
    creds['APP_VERSION']= open("/run/secrets/app_version", "r").read()   

    return creds, 200

@app.route('/volume', methods=['GET', 'POST'])    
def volume():
    filename = "/data/test.txt"
    if request.method == 'POST':
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'w') as f:
            f.write('Customer data entered')

        return 'saved!', 201
    else:
        f = open(filename, 'r')

        return f.read(), 200
