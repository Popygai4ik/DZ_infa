import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

с = 0
sumi = 0
for i in range(356712, 420902):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0 and is_prime(j):
            for k in range(j + 1, int((i // j) ** 0.5) + 1):
                if (i // j) % k == 0 and is_prime(k) and (j % 10 == k % 10):
                    if (i // j) // k != k and (i // j) // k != j and is_prime((i // j) // k) and (j % 10 == (i // j) // k % 10):
                        с += 1
                        sumi += i

print(с, sumi // с)
