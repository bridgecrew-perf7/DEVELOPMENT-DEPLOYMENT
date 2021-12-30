# Python Django Docker-Compose
```
docker-compose -f file.yml up --build
docker-compose exec web python manage.py bootstrap_subscriptions
docker-compose exec web python manage.py promote_user_to_superuser me@example.com
```
