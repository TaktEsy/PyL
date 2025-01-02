import sqlite3

connection = sqlite3.connect('base.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER
)
''')

cursor.execute('''
   CREATE INDEX IF NOT EXISTS idx_email ON Users (email)
''')

# Вставка
# for i in range(1, 30):
#     cursor.execute("INSERT INTO Users (username, email, age) VALUES (?,?,?)",(f"newuser{i}",f"ex{i}@gmail.com",f"{18+i}"))

# Обновление
# cursor.execute("""
#     UPDATE Users SET age = ? WHERE id =?
# """,
#                (25, 1))

# cursor.execute('''
#     DELETE FROM Users WHERE username = ?''',
# ("newuser",))


# Полная выборка
# cursor.execute("""SELECT * FROM Users""")

# Конкретная выборка
# cursor.execute("SELECT * FROM Users WHERE age<?", (30,))

cursor.execute("SELECT username, age FROM Users GROUP BY AGE")
users = cursor.fetchall()
for user in users:
    print(user)
connection.commit()
connection.close()