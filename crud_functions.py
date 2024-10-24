import sqlite3

connect = sqlite3.connect('products.db')
cursor = connect.cursor()



def initiate_db(cursor=cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NON NULL UNIQUE,
            description TEXT,
            price INTEGER NOT NULL
            )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
                   id INTEGER PRIMARY KEY,
                   username TEXT NT NULL,
                   email TEXT NOT NULL,
                   age INTEGER NOT NULL,
                   balance INTEGER NOT NULL
                   )
        ''')

    connect.commit()

def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, 1000))
    connect.commit()

def is_included(username):
    return cursor.execute(f"SELECT COUNT(*) FROM Users WHERE username = ?", (f'{username}',)).fetchone()[0] > 0


def get_all_products(cursor=cursor):
    cursor.execute('''
        SELECT * FROM Products
''')
    return cursor.fetchall()


def add_product(title: str, description: str, price: int, cursor=cursor):
    cursor.execute(f'''INSERT INTO Products (title, description, price) VALUES(?, ?, ?)''', (f'{title}', f'{description}', f'{price}'))
    connect.commit()
    


