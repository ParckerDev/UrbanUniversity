def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()
#inner_function() # вызывает ошибку, так как это локальная функция функции test_finction