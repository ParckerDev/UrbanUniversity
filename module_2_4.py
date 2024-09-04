numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = numbers[1:]
not_primes = []
for num in primes:
    for i in range(2, num):
        print(f'{num} % {i} = {num % i}')
