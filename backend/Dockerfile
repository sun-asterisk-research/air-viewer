FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install flask_cors flask-restful flask-jwt-extended passlib flask-sqlalchemy pymysql

COPY ./app /app
WORKDIR /app/

EXPOSE 80
