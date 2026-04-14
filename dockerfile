FROM python:3.12-alpine

#RUN apk --no-cache add curl
RUN apk add --no-cache curl

WORKDIR /app


COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .
COPY templates/ templates/


CMD [ "gunicorn" ,"--bind", "0.0.0.0:5000" ,"app:app"]