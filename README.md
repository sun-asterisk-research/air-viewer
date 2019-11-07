# Running a Air Visual application backend + frontend over HTTPS with traefik and Let's Encrypt

copy .env.example -> .env
config `MYSQL_ROOT_PASSWORD`

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

