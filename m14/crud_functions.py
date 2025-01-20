import sqlite3

connection = sqlite3.connect('hpup_base.db')
cursor = connection.cursor()

def initiate_db():

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INT,
        title TEXT,
        description TEXT,
        price INT
    );
    ''')
    connection.commit()

def select(item, table):
    cursor.execute(f"SELECT {item} FROM {table}")
    res = cursor.fetchall()
    connection.commit()
    return res

