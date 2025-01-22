import sqlite3

connection = sqlite3.connect('hpup_base.db')
cursor = connection.cursor()

def initiate_db():

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL
    );
    ''')
    connection.commit()

def select(item, table):
    cursor.execute(f"SELECT {item} FROM {table}")
    res = cursor.fetchall()
    connection.commit()
    return res

def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES('{username}', '{email}', '{age}', 1000)")
    connection.commit()


def is_included(username):
    check_user = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))

    if check_user.fetchone() is None:
        return False
    else:
        return True
    connection.commit()

# print(is_included("admin"))
# add_user("admin", "email", 20)
