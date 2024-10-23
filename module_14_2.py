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

# Delete User where id = 6
cursor.execute(" DELETE FROM Users WHERE id = 6")

# Total users
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# All_balance
cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]
print(all_balance/total_users)

connection.commit()
connection.close()