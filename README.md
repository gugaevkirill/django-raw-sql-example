# django-raw-sql-example

## Quickstart
1. `cp .env.example .env`
2. `docker-compose build`
3. `docker-compose up -d`
4. Run migrations:
    ```bash
    docker exec -it django_raw_sql bash
   python manage.py migrate
    ```
5. Visit http://localhost:8101/test_view/