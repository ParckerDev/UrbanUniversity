import sqlite3

connection = sqlite3.connect('product_database.db')
cursor = connection.cursor()

async def initiate_db(table_name):
    await cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name}(
            id INT PRIMARY KEY,
            title TEXT NON NULL,
            description TEXT,
            price INT NOT NULL
            )

    ''')

async def get_all_products(table_name):
    await cursor.execute(f'''
        SELECT * FROM {table_name}
    ''')
    return cursor.fetchall()




connection.commit()
connection.close()