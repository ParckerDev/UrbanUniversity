import os
import time

directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        filesize = os.path.getsize(file_path)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parrent_directory = os.path.basename(root)

        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parrent_directory}')