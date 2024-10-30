def get_matrix(row, col, value):
    return [[value for j in range(col)] for i in range(row)]

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)