def calculate_structure_sum(data_structure):
    sum = 0
    if isinstance(data_structure, dict):
        sum += dict_calc(data_structure)
    else:
        sum += no_dict_calc(data_structure)
    return sum

def no_dict_calc(args):
    sum = 0
    for elem in args:
        if isinstance(elem, (int, float)):
            sum += elem
        elif isinstance(elem, str):
            sum += len(elem)
        elif isinstance(elem, dict):
            sum += dict_calc(elem)
        else: # list or tuple or set
            
            sum += no_dict_calc(elem)
    return sum

def dict_calc(kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum += no_dict_calc([key, value])
    return(sum)



# TESTS

data_structure_1 = 'quatro'
data_structure_2 = [2, 3, 'gh']
data_structure_3 = {'cube': 7, 'drum': [1, 2, 'fds']}
data_structure_4 = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure_1)
print(result)
result = calculate_structure_sum(data_structure_2)
print(result)
result = calculate_structure_sum(data_structure_3)
print(result)
result = calculate_structure_sum(data_structure_4)
print(result)