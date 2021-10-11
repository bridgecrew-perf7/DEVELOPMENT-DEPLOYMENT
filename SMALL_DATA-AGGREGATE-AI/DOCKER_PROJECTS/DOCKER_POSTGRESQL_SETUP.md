# Docker PostgreSQL project

## Docker setup
```console
sudo apt update
sudo apt upgrade
sudo apt install docker
```
## Docker Compose setup
```console
sudo apt install docker-compose
docker–compose –version
access postgresql commands

##  Docker Compose PostgreSQL setup
```console
cd dockerbuild
docker-compose.yml
```
```console
cd /dockerbuild/postgresbuild
nano Dockerfile
```

## Docker PostgreSQL Compose YAML file
```yaml
version: "3"

services:
  db:
    image: "postgres:14.0"
    restart: "always"
    environment:
      POSTGRES_DB: "postgres"
      POSTGRES_USER: "admin"
      POSTGRES_PASSWORD: "secret"
    ports:
      - "5432:5432"
```


## Docker PostgreSQL Commands
```console
sudo docker exec -it postgres_database_1 bash
psql --host=postgres_database_1 --dbname=db_name --username=user
psql -h postgres_database_1 -d db_name -U user -f infile

psql -U user

psql -U postgres

\c database_name;

\q

\l

\dn

\df

\dv

\dt

\dt+

\d+ table_name

\df+ function_name

\x

\du

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
