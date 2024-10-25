numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
n = 0
primes = []  # список простых чисел
not_primes = []  # список составных чисел

for num in numbers:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                not_primes.append(num)
                break

        else:
            primes.append(num)
    else:
        not_primes.append(num)
print('Список простых чисел:', primes)
print('Список не простых чисел:', not_primes)
















