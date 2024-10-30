import requests # буду использовать для получения кода страницы
from bs4 import BeautifulSoup as Bs # буду использовать для парсинга страницы
import pandas as pd # для создания и сохранения результата в таблицу
from time import sleep
import pprint

MAIN_URL = 'https://www.farming-simulator.com/'


def get_pagination_pages(url) -> int:
    '''
    Функция принимает адрес страницы категории в строковом формате,
    возвращает количество страниц (int) в данной категории
    
    '''
    # C помощью request.get получаем код страницы
    print('начата работа функции get_pagination_pages')
    html = requests.get(url).text
    try:
        page = int(Bs(html, 'html.parser').find('ul', class_='pagination text-center clearfix').findAll('a')[-1].text) # type: ignore
    except:
        page = 1
    finally:
        print(f'Найдено {page} страниц в категории')
    return page


def make_category(url):
    '''
    Функция принимает на вход адрес страницы
    и возвращает список из пар название категории и ссылка на страницу с этой категорией
    
    '''
    # C помощью request.get().text получаем код страницы
    html = requests.get(url).text
    # находим с помощью метода find наш список категорий и с помощью метода findAll собираем ссылки на категории в список
    soup = Bs(html, 'html.parser').find('ul', class_='tabs-mods-category-list').findAll('a') # type: ignore
    #создаём список из пар названия категории и ссылки на категорию
    categories = [[category.text, MAIN_URL+category.get('href')] for category in soup]
    return categories


def link_slice(link):
    new_link = link.replace('page=0', '')
    return new_link


# Создаём список категорий
categories = make_category(MAIN_URL+'mod.php')
print(f'Найдено {len(categories)} категорий')
# создаём главный список
FS22_DATA = []

# Теперь проходимся по каждой категории из списка категорий
for category in categories:
    # в каждой категории может быть несколько страниц
    # с помощью функции get_pagination_pages получаем информацию о количестве страниц
    # проходимся по каждой 
    for i in range(get_pagination_pages(category[1])):
        page = f'{link_slice(category[1])}page={i}'

        # теперь парсим каждую страницу
        html = requests.get(page).text
        print(f'Идёт обработка {i+1} страницы в категории {category[0]}') 
        # ищем все карточки на странице и добавляем в список
        cards = Bs(html, 'html.parser').findAll('div', class_='medium-6 large-3 columns')
        # проходимся по каждой карточке и собираем нужные данные
        for card in cards:
            # название категории
            cat = category[0]
            # название дополнения
            name = card.find('h4').text
            try:
                # рейтинг
                rate = float(card.find('div', class_="mod-item__rating-num").text.rstrip().split()[0])
                # количество скачиваний
                downloads = int(card.find('div', class_="mod-item__rating-num").text.rstrip().split()[1][1:-2])
            except:
                # если нет оценок и/или скачиваний то присваиваем 0
                rate = 0
                downloads = 0
            # ссылка для скачивания
            link = MAIN_URL+card.find('a', class_='button button-buy button-middle button-no-margin expanded').get('href')
            # теперь добавляем найденную информацию в главный список
            FS22_DATA.append([cat, name, rate, downloads, link])
        # делаем небольшую задержку
        sleep(0.2)
print(FS22_DATA)
# Создаём список с заголовками будущей таблицы
header = ['Category', 'Name', 'Rate', 'Downloads', 'Link']
# создаём таблицу с помощью pandas
mods = pd.DataFrame(FS22_DATA, columns=header)
# ну и сохраняем полученный результат в файл
mods.to_csv('farming_mods.csv', sep=';', encoding='utf8')