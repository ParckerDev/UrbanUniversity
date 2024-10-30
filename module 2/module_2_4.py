numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = numbers[1:]
not_primes = []
for num in numbers[1:]:
    for i in range(2, num):
        if num % i == 0:
            primes.remove(num)
            not_primes.append(num)
            break
print(f'Primes: {primes}')
print(f'Not Primes: {not_primes}')
