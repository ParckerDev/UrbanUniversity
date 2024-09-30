import os
import time

def scan_folder(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            filesize = os.path.getsize(file_path)
            filetime = os.path.getmtime(file_path)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            parrent_directory = os.path.basename(file_path)

            print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parrent_directory}')

scan_folder('.')