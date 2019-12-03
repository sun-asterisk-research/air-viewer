Web application:
https://airviewer.sun-asterisk.vn/ 

# Running a Air Viewer application backend + frontend over HTTPS with traefik and Let's Encrypt

copy `.env.example` -> `.env`


copy `frontend/.env.example` -> `frontend/.env`


change to your domain in your `.env`. In this case `service.test`

```
//.env
API_HOST=service.test

#DATABASE
DB_PORT=3306
DB_DATABASE=air_viewer
DB_USERNAME=example
DB_PASSWORD=example
MYSQL_ROOT_PASSWORD=root
```

```
//frontend/.env
API_HOST=https://service.test
```

make sure that `/etc/hosts` add follow domain like `127.0.0.1 service.test`


## Run docker staging (can connect mysql via port 3306)

```
docker-compose -f docker-compose.dev.yml up -d
```

## Run docker production

```
docker-compose up -d
```

frontend: https://service.test
backend: https://service.test/api/

# Run Project development

### backend

make environment here
```
//requiments.txt
aniso8601==8.0.0
Click==7.0
Flask==1.1.1
Flask-Cors==3.0.8
Flask-JWT-Extended==3.24.1
Flask-RESTful==0.3.7
Flask-SQLAlchemy==2.4.1
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
passlib==1.7.1
PyJWT==1.7.1
PyMySQL==0.9.3
pytz==2019.3
six==1.13.0
SQLAlchemy==1.3.10
uWSGI==2.0.18
Werkzeug==0.15.5
```

Install envireonment 
```
pip install -r requirements.txt

cd backend/app
bash ./backend-live.sh
```
Open: http://localhost:5000/api/

### frontend
```
cd frontend
npm install
npm run dev
```
Open: http://localhost:3000

# PI Sensor Client
Connect SDS011 with raspberry pi
```
cd client
pip3 install -r requirements.txt
```
Test code Client
```
python3 aqi_client.py
```
Result
```
Result: AQI: 15, PM2.5: 3.5, PM10: 4.3
2019-11-27 17:17:46.292042
```
Edit client
```
vim aqi_client.py
```
Edit `url = 'https://airviewer.sun-asterisk.vn/api/secret/xxxx'`
with `xxxx=<secret key>`

Setup crontab
```
crontab -l 
*/5 * * * * python3 air-viewer/client/aqi_client.py >> log.txt &
```
