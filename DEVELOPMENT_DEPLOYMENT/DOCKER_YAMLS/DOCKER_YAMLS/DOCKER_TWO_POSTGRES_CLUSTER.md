version: "3.8"

services:

  # docker dns name
  postgres_2:
    container_name: postgres_2_container
    image: postgres:14.1
    restart: unless-stopped
    # postgres image specific environment variable options
    environment:
      - POSTGRES_DB=postgres_2
      - POSTGRES_USER=postgres_2
      - POSTGRES_PASSWORD=postgres
      - PGDATA=/var/lib/postgresql_c/data/ # named volume for long term data
      - $PWD/postgres_2_dump.dump:/docker-entrypoint-initdb.d/init.sql:ro # bind mount as backup storage script
      # docker exec -ti postgres_2_container pg_dump -U postgres_2 postgres_2 > postgres_2_dump.dump # postgres docker image backup dump script
    volumes:
       - postgres_2_data:/var/lib/postgresql_c/data/
    ports:
      - "50001:5432"
    networks:
      - postgres_2

  pgadmin:
    container_name: pgadmin4_container
    build:
      context: "./pgadmin4_build"
      dockerfile: "./Dockerfile"
    environment:
      PGADMIN_DEFAULT_EMAIL: pgadmin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
      PGADMIN_CONFIG_SERVER_MODE: 'False'
    volumes:
       - pgadmin_data:/var/lib/pgadmin
    ports:
      - "5050:80"
    networks:
      - postgres_2
      - postgres

  postgres:
    container_name: postgres_2ontainer
    image: postgres:14.1
    environment:
      - POSTGRES_DB=web_app
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - PGDATA=/var/lib/postgresql/data/
      - $PWD/postgres_dump.dump:/docker-entrypoint-initdb.d/init.sql:ro # bind mount as backup storage script
      # docker exec -ti postgres_2_container pg_dump -U postgres_2 postgres_2 > postgres_dump.dump # postgres docker image backup dump script
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    ports:
      - "5432:5432"
    networks:
      - postgres
    restart: unless-stopped

  redis:
    container_name: redis_container
    image: redis
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    restart: unless-stopped

  web:
    container_name: web_container
    build:
      context: .
      dockerfile: Dockerfile.dev
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    env_file:
      - ./.env.dev
    depends_on:
      - postgres
      - redis
    restart: unless-stopped

    networks:
      - postgres_2
      - postgres

  celery:
    container_name: celery_container
    build:
      context: .
      dockerfile: Dockerfile.dev
    command: celery -A web_app worker -l INFO
    volumes:
      - .:/code
    env_file:
      - ./.env.dev
    depends_on:
      - postgres
      - redis
    restart: unless-stopped

networks:
  postgres_2:
    driver: bridge
  postgres:
    driver: bridge

volumes:
  postgres_2_data:
  postgres_data:
  pgadmin_data:
  redis_data:
