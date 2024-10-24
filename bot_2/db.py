from email import message
import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
        id INT,
        usrname TEXT,
        first_name TEXT,
        block INT
        )
''')

# Добавление юзера
def add_user(user_id, username, first_name):
    check_user = cursor.execute('SELECT * FROM Users WHERE id = ?', (user_id,))
    if check_user.fetchone() is None:
        cursor.execute(f'''
            INSERT INTO Users VALUES ('{user_id}', '{username}', '{first_name}', 0)
        ''')
    connection.commit()

# Показать всех юзеров
def show_users():
    users_list = cursor.execute("SELECT * FROM Users")
    message = ''
    for user in users_list:
        message += f'{user[0]} @{user[1]} {user[2]}\n'
    connection.commit()
    return message

# Показать количество пользователей
def show_stat():
    users_count = cursor.execute("SELECT COUNT(*) FROM Users").fetchone()
    connection.commit()
    return users_count[0]

# Добавление юзера в блок
def add_to_block(user_id):
    cursor.execute(f"UPDATE Users SET block = 1 WHERE user_id = {user_id}")
    connection.commit()

# Удаление юзера из блока
def add_to_block(user_id):
    cursor.execute(f"UPDATE Users SET block = 0 WHERE user_id = {user_id}")
    connection.commit()

# Проверка есть ли юзер в блоке
def check_block_user(user_id):
    return False if cursor.execute(f'SELECT block FROM Users WHERE user_id = {user_id}').fetchone()[0] == 0 else True
     


connection.commit()
connection.close()