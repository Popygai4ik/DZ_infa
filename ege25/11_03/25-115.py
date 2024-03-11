def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

max_ranitsa = 200000000
res = []
c = 0
f = 0
for i in range(478392, 502440):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            if is_prime(i // j) and is_prime(j) and (j != (i // j)):
                c += 1
                raznitsa = abs(j - i // j)
                if raznitsa < max_ranitsa:
                    max_ranitsa = raznitsa
                    res.append(i)

print(c, max(res))

