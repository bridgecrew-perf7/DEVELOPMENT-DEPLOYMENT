# Python PostgreSQL SQL Pandas Cheat Sheet

## Questions to ask
1. What server name am I connecting to?
2. What database name am I connecting to?
3. What table name am I connecting to?
4. What database program do I use?
5. What programming language do I use to connect to the database program?
6. What adapter do I use to connect to the database program?

## PostgreSQL database.ini
```
[postgresql]
host=string
database=string
user=string
password=string
port=integer
```

## PostgreSQL config / connect
```
import ConfigParser
import psycopg2
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

# verify with SELECT * FROM table

```

## PostgreSQL commands

```console
sudo psql -U USER -d logging_db
\du
CREATE TABLE logging_table
    id INT PRIMARY KEY NOT NULL,
    int_col INT NOT NULL,
    str_col TEXT NOT NULL,
    book_col BOOL NOT NULL
);
INSERT INTO
    logging_table(id, str_col, int_col, bool_col)
VALUES
    (1, "foo bar", 42, TRUE)
    (2, "string, 2000, FALSE):
\q
```

## Pandas SQL Commands
```console
df = pd.read_sql_query("SELECT * FROM products", conn)

c.execute("SELECT * FROM product")
df = pdf.DataFrame(c.fetchall(), colmns = ["entry_id", "entry_name", int]



