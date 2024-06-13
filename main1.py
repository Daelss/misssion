import psycopg2
import random
import string
import hashlib

# создаем соединение с базой данных
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
)
cur = conn.cursor()

# создаем 15 пользователей и баз данных
for i in range(1, 16):
    username = f"user{i}"
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(4))
    dbname = f"base{i}"

    # # создаем пользователя
    # cur.execute(f"create user {username} with password '{password}';")
    # conn.commit()

    # создаем новое соединение для каждого действия
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="123"
    )
    cur = conn.cursor()

    # # создаем базу данных
    # cur.execute(f"commit")
    # cur.execute(f"create database {dbname} owner {username};")
    # conn.commit()

    # предоставляем привилегии пользователю
    cur.execute(f"grant all privileges on database {dbname} to {username};")
    conn.commit()

    # отзываем нежелательные привилегии
    cur.execute(f"revoke all privileges on database {dbname} from {username};")
    conn.commit()

# Создание базы данных BaseAll и таблицы UsersAll
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
)
cur = conn.cursor()

cur.execute("commit")

# Создание базы данных BaseAll и таблицы UsersAll
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
)
cur = conn.cursor()

cur.execute("commit")

# # Создание базы данных BaseAll
# cur.execute("CREATE DATABASE BaseAll;")
# conn.commit()

# # Создание таблицы UsersAll
# cur.execute("""
# CREATE TABLE UsersAll (
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(50) NOT NULL,
#     password_hash VARCHAR(255) NOT NULL
# );
# """)
# conn.commit()

# Заполнение таблицы UsersAll данными созданных пользователей и рандомных паролей
for i in range(1, 16):
    username = f"user{i}"
    password_hash = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))
    cur.execute("INSERT INTO UsersAll (username, password_hash) VALUES (%s, %s);", (username, password_hash))
    conn.commit()

# создаем соединение с базой данных
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="123"
)
cur = conn.cursor()

# Создаем функцию для хэширования паролей с использованием SHA-256
cur.execute('''
CREATE OR REPLACE FUNCTION hash_password(input_text text) RETURNS text AS $$
BEGIN
    RETURN encode(sha256(input_text::bytea), 'hex');
END;
$$ LANGUAGE plpgsql;
''')
conn.commit()

# Обновляем пароли в таблице UsersAll, используя созданную функцию hash_password
cur.execute("UPDATE UsersAll SET password_hash = hash_password(password_hash);")
conn.commit()

# закрываем соединение и курсор за пределами цикла
cur.close()
conn.close()