import sqlite3

connect = sqlite3.connect('not_telegram.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Вставка 10-ти строк
# for i in range(0, 10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
#                    (f"User{i+1}",f"ex{i+1}@gmail.com",f"{i+1}0", "1000"))


# Обновление баланса у каждой нечетной записи
cursor.execute("""
    UPDATE Users SET balance = ? WHERE id % ? = ? """,
               (500,2,1,) )

# Удаление каждой 3-ей записи
cursor.execute("""
    DELETE FROM Users WHERE (id-?) % ? = ? """,
               (1,3,0,))

# Выборка
cursor.execute("""
    SELECT * FROM Users WHERE age != ?""",
    (60,))
usrs = cursor.fetchall()

for u in usrs:
    print(f"Имя: {u[1]} | Почта: {u[2]} | Возраст: {u[3]} | Баланс: {u[4]}")
connect.commit()
connect.close()