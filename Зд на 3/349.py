from math import isqrt


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True


n, m = map(int, input().split())
c = True

for i in range(max(2, n), m + 1):
    if is_prime(i):
        print(i)
        c = False

if c:
    print('Absent')