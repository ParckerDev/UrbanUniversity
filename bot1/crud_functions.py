import sqlite3

connect = sqlite3.connect('products.db')
cursor = connect.cursor()



def initiate_db(cursor=cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INT PRIMARY KEY,
            title TEXT NON NULL,
            description TEXT,
            price INT NOT NULL
            )
    ''')
    connect.commit()
    connect.close()