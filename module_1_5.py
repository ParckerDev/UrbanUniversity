immutable_var = 2, 3, 67, ['this', 'is'], True
print(immutable_var)

# так как кортежи относятся к неизменяемым типам данных, то изменить их не можем
# но есть возможность изменять объекты внутри кортежа, если они относятся к изменяемым типам данных

immutable_var[3].append('python, baby...') # изменили 4 элемент - список, путём добавления ещё одного элемента
print(immutable_var)

mutable_var = [True, 'pasta', 56]
mutable_var[0] = 'pancake'
mutable_var[1] = False
mutable_var[2] = None
print(mutable_var)