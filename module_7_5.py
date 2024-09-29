import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(file)

        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')