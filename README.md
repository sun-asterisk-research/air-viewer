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
