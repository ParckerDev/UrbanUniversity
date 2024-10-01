from datetime import datetime
from time import sleep
from threading import Thread


def write_words(word_count: int, file_name: str):
    with open(file_name, 'w+', encoding='utf-8') as file:
        for num in range(word_count):
            file.write(f'Какое-то слово № {num+1}')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')



    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')