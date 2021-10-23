# Python PostgreSQL SQL Pandas Cheat Sheet

## PostgreSQL and pgAdmin4 setup Ubuntu
```console
sudo apt update && sudo apt upgrade
sudo apt install postgresql postgresql-contrib
sudo apt install curl
sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add
sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
sudo apt install pgadmin4
sudo ufw allow http
sudo ufw allow https
http://localhost:5050/browser/
```
```console
sudo -i -u postgres
psql
sudo -u postgres createuser --interactive
sudo adduser postgres
sudo -i -u postgres
psql
psql -d postgres

```

## Questions to ask
1. What server name am I connecting to?
2. What database name am I connecting to?
3. What table name am I connecting to?
4. What database program do I use?
5. What programming language do I use to connect to the database program?
6. What adapter do I use to connect to the database program?

## PostgreSQL pgAdmin4 Docker Compose File
```console
version: '3.5'
services:
  postgres:
    container_name: postgres_container
    image: postgres
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-secret}
      PGDATA: /data/postgres
    volumes:
       - postgres:/data/postgres
    ports:
      - "5432:5432"
    networks:
      - postgres
    restart: unless-stopped
  
  pgadmin:
    container_name: pgadmin_container
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: ${PGADMIN_DEFAULT_EMAIL:-pgadmin4@pgadmin.org}
      PGADMIN_DEFAULT_PASSWORD: ${PGADMIN_DEFAULT_PASSWORD:-admin}
      PGADMIN_CONFIG_SERVER_MODE: 'False'
    volumes:
       - pgadmin:/var/lib/pgadmin

    ports:
      - "${PGADMIN_PORT:-5050}:80"
    networks:
      - postgres
      - nginx
    restart: unless-stopped

networks:
  nginx:
    driver: bridge
    name: nginx
  postgres:
    driver: bridge
    name: db

volumes:
    postgres:
    pgadmin:
```

## PostgreSQL database.ini
```console
[postgresql]
host=string
dbname=string
user=string
password=string
port=integer
```

## PostgreSQL config / connect
```console
import ConfigParser
import psycopg
import config

def config(filename='database.ini', section='postgresql'):

    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def connect():

    conn = None

    try:
        params = config()

        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        db_version = cur.fetchone()
        print(db_version)

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

c = conn.cursor()

c.execute("INSERT INTO table (entry_id, entry_name, int) VALUES (1, "thing", 0)")

c.execute("UPDATE table SET entry_name = 0 WHERE entry_id = 2")

conn.commit()

## Pandas SQL Commands
```console

df = pd.read_sql_query("SELECT * FROM products", conn)

c.execute("SELECT * FROM product")
df = pdf.DataFrame(c.fetchall(), colmns = ["entry_id", "entry_name", int]
```
## PostgreSQL commands
```console
psql -U <database username you want to connect with> -d <database name>

\dn

\df

\dv

\dt

\dt+

\d+ table_name

\df+ function_name

\l

\c databasename

\x

\q


CREATE TABLE logging_table
    id INT PRIMARY KEY NOT NULL,
    int_col INT NOT NULL,
    str_col TEXT NOT NULL,
    book_col BOOL NOT NULL
);

DROP TABLE logging_table;

SELECT * FROM logging_table;

INSERT INTO logging_table(id, str_col, int_col, bool_col) VALUES (1, "foo bar", 42, TRUE) (2, "string, 2000, FALSE):

INSERT INTO LOGGING (cloumn1, columnN) VALUES (value1, valueN)

psql --host=postgres_database_1 --dbname=db_name --username=user

psql -h postgres_database_1 -d db_name -U user -f infile

```

## SQL Commands
```console
CREATE ROLE role_name;
Create a new role with a username and password:

CREATE ROLE username NOINHERIT LOGIN PASSWORD password;
Change role for the current session to the new_role:

SET ROLE new_role;
Allow role_1 to set its role as role_2:

GRANT role_2 TO role_1;
Code language: SQL (Structured Query Language) (sql)
Managing databases
Create a new database:

CREATE DATABASE [IF NOT EXISTS] db_name;
Code language: SQL (Structured Query Language) (sql)
Delete a database permanently:

DROP DATABASE [IF EXISTS] db_name;
Code language: SQL (Structured Query Language) (sql)
Managing tables
Create a new table or a temporary table

CREATE [TEMP] TABLE [IF NOT EXISTS] table_name(
   pk SERIAL PRIMARY KEY,
   c1 type(size) NOT NULL,
   c2 type(size) NULL,
   ...
);
Code language: SQL (Structured Query Language) (sql)
Add a new column to a table:

ALTER TABLE table_name ADD COLUMN new_column_name TYPE;
Code language: SQL (Structured Query Language) (sql)
Drop a column in a table:

ALTER TABLE table_name DROP COLUMN column_name;
Code language: SQL (Structured Query Language) (sql)
Rename a column:

ALTER TABLE table_name RENAME column_name TO new_column_name;
Code language: SQL (Structured Query Language) (sql)
Set or remove a default value for a column:

ALTER TABLE table_name ALTER COLUMN [SET DEFAULT value | DROP DEFAULT]
Code language: SQL (Structured Query Language) (sql)
Add a primary key to a table.

ALTER TABLE table_name ADD PRIMARY KEY (column,...);
Remove the primary key from a table.

ALTER TABLE table_name
DROP CONSTRAINT primary_key_constraint_name;
Code language: SQL (Structured Query Language) (sql)
Rename a table.

ALTER TABLE table_name RENAME TO new_table_name;
Code language: SQL (Structured Query Language) (sql)
Drop a table and its dependent objects:

DROP TABLE [IF EXISTS] table_name CASCADE;
Code language: SQL (Structured Query Language) (sql)
Managing views
Create a view:

CREATE OR REPLACE view_name AS
query;
Code language: SQL (Structured Query Language) (sql)
Create a recursive view:

CREATE RECURSIVE VIEW view_name(column_list) AS
SELECT column_list;
Code language: SQL (Structured Query Language) (sql)
Create a materialized view:

CREATE MATERIALIZED VIEW view_name
AS
query
WITH [NO] DATA;
Code language: SQL (Structured Query Language) (sql)
Refresh a materialized view:

REFRESH MATERIALIZED VIEW CONCURRENTLY view_name;
Code language: SQL (Structured Query Language) (sql)
Drop a view:

DROP VIEW [ IF EXISTS ] view_name;
Code language: SQL (Structured Query Language) (sql)
Drop a materialized view:

DROP MATERIALIZED VIEW view_name;
Code language: SQL (Structured Query Language) (sql)
Rename a view:

ALTER VIEW view_name RENAME TO new_name;
Code language: SQL (Structured Query Language) (sql)
Managing indexes
Creating an index with the specified name on a table

CREATE [UNIQUE] INDEX index_name
ON table (column,...)
Code language: SQL (Structured Query Language) (sql)
Removing a specified index from a table

DROP INDEX index_name;
Code language: SQL (Structured Query Language) (sql)
Querying data from tables
Query all data from a table:

SELECT * FROM table_name;
Code language: SQL (Structured Query Language) (sql)
Query data from specified columns of all rows in a table:

SELECT column_list
FROM table;
Code language: SQL (Structured Query Language) (sql)
Query data and select only unique rows:

SELECT DISTINCT (column)
FROM table;
Code language: SQL (Structured Query Language) (sql)
Query data from a table with a filter:

SELECT *
FROM table
WHERE condition;
Code language: SQL (Structured Query Language) (sql)
Assign an alias to a column in the result set:

SELECT column_1 AS new_column_1, ...
FROM table;
Code language: SQL (Structured Query Language) (sql)
Query data using the LIKE operator:

SELECT * FROM table_name
WHERE column LIKE '%value%'
Code language: SQL (Structured Query Language) (sql)
Query data using the BETWEEN operator:

SELECT * FROM table_name
WHERE column BETWEEN low AND high;
Code language: SQL (Structured Query Language) (sql)
Query data using the IN operator:

SELECT * FROM table_name
WHERE column IN (value1, value2,...);
Code language: SQL (Structured Query Language) (sql)
Constrain the returned rows with the LIMIT clause:

SELECT * FROM table_name
LIMIT limit OFFSET offset
ORDER BY column_name;
Code language: SQL (Structured Query Language) (sql)
Query data from multiple using the inner join, left join, full outer join, cross join and natural join:

SELECT *
FROM table1
INNER JOIN table2 ON conditions
Code language: SQL (Structured Query Language) (sql)
SELECT *
FROM table1
LEFT JOIN table2 ON conditions
Code language: SQL (Structured Query Language) (sql)
SELECT *
FROM table1
FULL OUTER JOIN table2 ON conditions
Code language: SQL (Structured Query Language) (sql)
SELECT *
FROM table1
CROSS JOIN table2;
Code language: SQL (Structured Query Language) (sql)
SELECT *
FROM table1
NATURAL JOIN table2;
Code language: SQL (Structured Query Language) (sql)
Return the number of rows of a table.

SELECT COUNT (*)
FROM table_name;
Code language: SQL (Structured Query Language) (sql)
Sort rows in ascending or descending order:

SELECT select_list
FROM table
ORDER BY column ASC [DESC], column2 ASC [DESC],...;
Code language: SQL (Structured Query Language) (sql)
Group rows using GROUP BY clause.

SELECT *
FROM table
GROUP BY column_1, column_2, ...;
Code language: SQL (Structured Query Language) (sql)
Filter groups using the HAVING clause.

SELECT *
FROM table
GROUP BY column_1
HAVING condition;
Code language: SQL (Structured Query Language) (sql)
Set operations
Combine the result set of two or more queries with UNION operator:

SELECT * FROM table1
UNION
SELECT * FROM table2;
Code language: SQL (Structured Query Language) (sql)
Minus a result set using EXCEPT operator:

SELECT * FROM table1
EXCEPT
SELECT * FROM table2;
Code language: SQL (Structured Query Language) (sql)
Get intersection of the result sets of two queries:

SELECT * FROM table1
INTERSECT
SELECT * FROM table2;
Code language: SQL (Structured Query Language) (sql)
Modifying data
Insert a new row into a table:

INSERT INTO table(column1,column2,...)
VALUES(value_1,value_2,...);
Code language: SQL (Structured Query Language) (sql)
Insert multiple rows into a table:

INSERT INTO table_name(column1,column2,...)
VALUES(value_1,value_2,...),
      (value_1,value_2,...),
      (value_1,value_2,...)...
Code language: SQL (Structured Query Language) (sql)
Update data for all rows:

UPDATE table_name
SET column_1 = value_1,
    ...;
Code language: SQL (Structured Query Language) (sql)
Update data for a set of rows specified by a condition in the WHERE clause.

UPDATE table
SET column_1 = value_1,
    ...
WHERE condition;
Code language: SQL (Structured Query Language) (sql)
Delete all rows of a table:

DELETE FROM table_name;
Code language: SQL (Structured Query Language) (sql)
Delete specific rows based on a condition:

DELETE FROM table_name
WHERE condition;
Code language: SQL (Structured Query Language) (sql)
Performance
Show the query plan for a query:

EXPLAIN query;
Code language: SQL (Structured Query Language) (sql)
Show and execute the query plan for a query:

EXPLAIN ANALYZE query;
Code language: SQL (Structured Query Language) (sql)
Collect statistics:

ANALYZE table_name;
Code language: SQL (Structured Query Language) (sql)
```
