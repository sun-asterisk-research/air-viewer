# Running a Air Visual application backend + frontend over HTTPS with traefik and Let's Encrypt

copy .env.example -> .env
copy frontend/.env.example -> frontend/.env

modified: traefik/traefik.toml
change to your domain
```
domain = "service.test"
```
make sure that `/etc/hosts` add follow domain like `127.0.0.1 service.test`

To run docker production:

```
docker-compose up -d
```

traefik UI: http://service.test:8080

frontend: https://service.test
backend: https://service.test/api/

# Run Project development

config both `.env` `API_HOST='http://localhost:5000'`

### backend
```
cd backend/app
bash ./backend-live.sh
```
### frontend
```
cd frontend
npm run dev
```

## Client
Connect SDS011 with raspberry pi
Clone git 
```
git clone https://github.com/sun-asterisk-research/air-visual.git
```
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
*/5 * * * * python3 air-visual/client/aqi_client.py >> log.txt &
```