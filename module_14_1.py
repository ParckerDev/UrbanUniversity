import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
               id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER,
               balance INTEGER NOT NULL
               )
''')

# Create INDEX with email
cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Create users
for i in range(1,11):
    cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', f'{i*10}', 1000))

# Update balance
cursor.execute(" UPDATE Users SET balance = 500 WHERE id % 2 != 0")

# Delete Users
cursor.execute(" SELECT * FROM Users")
users = cursor.fetchall()
for i in range(1, len(users) + 1, 3):
    cursor.execute(" DELETE FROM Users WHERE id = ?", (f'{i}',))

cursor.execute(" SELECT * FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')
    
connection.commit()
connection.close()