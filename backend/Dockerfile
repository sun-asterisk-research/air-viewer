FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN echo "Asia/Ho_Chi_Minh" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

RUN pip install flask_cors flask-restful flask-jwt-extended passlib flask-sqlalchemy pymysql

COPY ./app /app
WORKDIR /app/

EXPOSE 80
