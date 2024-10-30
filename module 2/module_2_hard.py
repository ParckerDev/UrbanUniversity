def encoded(num):
    num_pair = []
    for i in range(1, num):
        for j in range(i+1, num):
            print(f'{num} % ({i} + {j} = {num % (i +j)})')
            if num % (i+j) == 0:
                num_pair.append(i)
                num_pair.append(j)
    num_pair = list(map(str, num_pair))
    return ''.join(num_pair)


print(encoded(9))