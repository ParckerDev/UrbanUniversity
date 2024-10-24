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
    connect.commit()

def get_all_products(cursor=cursor):
    cursor.execute('''
        SELECT * FROM Products
''')
    return cursor.fetchall()


def add_product(title: str, description: str, price: int, cursor=cursor):
    cursor.execute(f'''INSERT INTO Products (title, description, price) VALUES(?, ?, ?)''', (f'{title}', f'{description}', f'{price}'))
    connect.commit()
    


#add_product('Сила Жизни', 'Сила Жизни — это комплекс витаминов и минералов, созданный для поддержания общего здоровья и жизненной энергии. В его формуле содержатся витамины A, C и E, которые действуют как мощные антиоксиданты, защищая клетки от повреждений и поддерживая иммунную систему. Витамины группы B способствуют нормализации обмена веществ и повышению уровня энергии, а магний и калий помогают поддерживать здоровье сердечно-сосудистой системы. Экстракты зеленого чая и ашваганды добавлены для улучшения физической выносливости и снижения уровня стресса. Сила Жизни идеально подходит для людей, стремящихся к активному образу жизни и желающим поддерживать свое здоровье на высоком уровне. Принимайте Сила Жизни ежедневно, чтобы чувствовать себя энергичными и полными сил для достижения своих целей!', 1890)
