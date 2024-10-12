from datetime import datetime
import multiprocessing
import os

# Указываю относительный путь к папке
folder_path = 'module_10_Files/'

# Получаю список файлов в папке
file_list = os.listdir(folder_path)

# Фильтрую только файлы (исключаем папки)
file_list = [os.path.join(folder_path, file) for file in file_list if os.path.isfile(os.path.join(folder_path, file))]

print(f' Файлы в задании: {file_list}')

# функция чтения данных из файла
def read_info(file_path):
    all_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)

print('Начинаем линейный вызов...')
start_func = datetime.now()
for file in file_list:
    read_info(file)
end_func = datetime.now()
print(f'Линейный вызов выполнен за {end_func-start_func}')

print('Начинаем мультипроцессовый вызов...')
start_func = datetime.now()
with multiprocessing.Pool(processes=8) as pool:
    pool.map(read_info, file_list)
end_func = datetime.now()
print(f'мультипроцессовый вызов выполнен за {end_func-start_func}')