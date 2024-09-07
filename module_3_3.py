def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = ['__', False, [1.5, 5, 37, 20.1]]
values_dict = {'a': values_list, 'b': {'a': 1, 'z': 45,}, 'c': 'string'}


print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)