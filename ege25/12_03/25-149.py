import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [2]
for i in range(3, int(60000000**0.25) + 1, 2):
    if is_prime(i):
        primes.append(i)


ans = []

for i in primes[1:]:
    num = i ** 4
    if 55000000 <= num <= 60000000:
        ans.append([num, num])
    else:
        while num <= 60000000:
            if num >= 55000000:
                ans.append([num, i ** 4])
            num *= 2

ans.sort(key=lambda x: x[0])
for i in ans:
    print(i[0], i[1])
