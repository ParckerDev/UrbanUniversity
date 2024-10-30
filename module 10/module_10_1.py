from datetime import datetime
from time import sleep
from threading import Thread


def write_words(word_count: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as file:
        for num in range(word_count):
            file.write(f'Какое-то слово № {num+1}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = datetime.now()
result_time = end_time - start_time
print(f'Выполнение функций без потоков выполнено за {result_time}')

start_time = datetime.now()
thread_1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
end_time = datetime.now()
result_time = end_time - start_time
print(f'Выполнение функций c потоками выполнено за {result_time}')