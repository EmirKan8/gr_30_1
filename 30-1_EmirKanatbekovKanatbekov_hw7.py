import sqlite3
import re


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as error:
        print(error)

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(error)

def create_product(conn, product: tuple):
    try:
        sql = '''insert into products (product_title, price, quantity)
        values (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def update_quantity(conn, product: tuple):
    try:
        sql = '''update products set quantity = ? where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def update_price(conn, product: tuple):
    try:
        sql = '''update products set price = ? where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def delete_product(conn, id):
    try:
        sql = '''delete from products where id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as error:
        print(error)

def select_all_products(conn):
    try:
        sql = '''select * from products
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def select_by_price_and_quantity(conn, limit):
    try:
        sql = '''select * from products where price < ? and quantity > ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)

def search_by_word(conn, word):
    try:
        sql = '''select * from products where product_title like ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, ('%'+word+'%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(error)


database = r'hw.db'

sql_create_products_table = '''
create table products (
id integer primary key autoincrement,
product_title varchar(200) not null,
price  double(10, 2) not null default 0.0,
quantity integer(5) not null default 0
)
'''

connection = create_connection(database)
create_table(connection, sql_create_products_table)
create_product(connection, ('Фанта', 88.8, 8))
create_product(connection, ('Перец Чили', 90.42, 3))
create_product(connection, ('Мыло детское', 25.19, 5))
create_product(connection, ('Апельсиновый сок', 22.11, 6))
create_product(connection, ('Яблочный фрэш', 45.73, 14))
create_product(connection, ('Султан чай', 37.55, 9))
create_product(connection, ('Пицца', 152.38, 19))
create_product(connection, ('Макарон', 299.99, 2))
create_product(connection, ('Сэндвич', 124.12, 18))
create_product(connection, ('Alpen Gold oreo', 267.42, 12))
create_product(connection, ('Alpen Gold с фундуком', 135.68, 4))
create_product(connection, ('Дюшес', 29.35, 11))
create_product(connection, ('Квас', 20.28, 10))
create_product(connection, ('Кукла Ферби', 91.4, 5))
create_product(connection, ('Кымыс', 78.2, 13))
update_quantity(connection, (13, 7))
update_price(connection, (33.33, 12))
delete_product(connection, 2)
select_all_products(connection)
select_by_price_and_quantity(connection, (100, 5))
search_by_word(connection, 'Мыло')

connection.close()