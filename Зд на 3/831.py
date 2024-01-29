def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def suma(n):
    return sum(int(i) for i in str(n))

a, b = map(int, input().split())

m_sum = -1
m_shislo = -1
f = False
for i in range(b, a - 1, -1):
    if is_prime(i):
        f = True
        seisha_suma = suma(i)
        if seisha_suma > m_sum or (seisha_suma == m_sum and i > m_shislo):
            m_sum = seisha_suma
            m_shislo = i
print(m_shislo)
