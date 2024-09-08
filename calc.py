import tkinter as tk


def get_values():
    num1 = int(number_1_entry.get()) # забираем данные со строки number_1_entry
    num2 = int(number_2_entry.get()) # забираем данные со строки number_2_entry
    return num1, num2

def insert_answer(res):
    answer_entry.delete(0, 'end') # очищаем поле с результатом
    answer_entry.insert(0, str(res)) # вставляем в поле результат


def plus():
    num1, num2 = get_values()
    res = num1 + num2
    insert_answer(res)
    

def minus():
    num1, num2 = get_values()
    res = num1 - num2
    insert_answer(res)

def umnog():
    num1, num2 = get_values()
    res = num1 * num2
    insert_answer(res)


def delit():
    num1, num2 = get_values()
    res = num1 / num2
    insert_answer(res)


# create app-window
window = tk.Tk()

window.title('КАРкулRтор НАФИK') # название окна спрограммой
window.geometry('350x300') # задаёам размер окна высота*ширина
window.resizable(False, False) # запрещаем изменять окно по (ширине, высоте)

button_plus = tk.Button(window, text='+', width=2, height=1, command=plus) # создаём кнопку и указываем, что она пренадлежит окну window, и текст на кнопке "+"
button_plus.place(x=70, y=130) # задаем расположение кнопки
button_minus = tk.Button(window, text='-', width=2, height=1, command=minus)
button_minus.place(x=130, y=130)
button_umnog = tk.Button(window, text='*', width=2, height=1, command=umnog)
button_umnog.place(x=190, y=130)
button_delit = tk.Button(window, text='/', width=2, height=1, command=delit)
button_delit.place(x=250, y=130)

number_1_label = tk.Label(window, text='Введите первое число:')
number_1_label.place(x=70, y=10)
number_1_entry = tk.Entry(window, width=27)
number_1_entry.place(x=70, y=33)
number_2_label = tk.Label(window, text='Введите второе число:')
number_2_label.place(x=70, y=65)
number_2_entry = tk.Entry(window, width=27)
number_2_entry.place(x=70, y=88)
answer_label = tk.Label(window, text='Результат:')
answer_label.place(x=70, y=180)
answer_entry = tk.Entry(window, width=27)
answer_entry.place(x=70, y=205)
window.mainloop()
