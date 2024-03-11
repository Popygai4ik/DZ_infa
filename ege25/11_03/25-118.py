import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



count = 0
max_number = 0
res = []
c = 0
for i in range(158928, 345294):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if is_prime(j):
                for k in range(j + 1, int((i // j) ** 0.5) + 1):
                    if (i // j) % k == 0 and is_prime(k):
                        if (i // j) // k != k and (i // j) // k != j and is_prime((i // j) // k):
                            res.append(i)



print(len(res), min(res))
