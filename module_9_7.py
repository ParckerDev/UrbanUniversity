def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        for i in range(2, result//2 +1):
            if result % i == 0:
                print ('Составное')
                print(result)
                break
        print('Простое')
        return(result)
    return wrapper

@is_prime
def sum_three(a: int, b: int, c: int):
    return a + b + c


# TESTS
result = sum_three(2, 3, 6)
print(result)