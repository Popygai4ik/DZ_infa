def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

max_ranitsa = 0
res = []
for i in range(326359, 421987):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if is_prime(i // j) and is_prime(j):
                raznitsa = abs(j - i // j)
                if raznitsa > max_ranitsa:
                    max_ranitsa = raznitsa
                    res = sorted([j, i // j])

print(*res)
