with open("INPUT.TXT", "r") as f:
    n1 = int(f.readline().strip())
res = 1
b_s = 0
for i in range(1, n1 + 1):
    if n1 % i == 0:
        s = sum(int(stifra) for stifra in str(i))
        if s > b_s or (s == b_s and i < res):
            b_s = s
            res = i
with open("OUTPUT.TXt", "w") as file:
    file.write(str(res))
def find_special_divisor(num):
    result = 1
    m_s = 0

    for i in range(1, num + 1):
        if num % i == 0:
            seishas_suma = sum(int(i) for i in str(i))
            if seishas_suma > m_s or (seishas_suma == m_s and i < result):
                m_s = seishas_suma
                result = i

    return result

with open("INPUT.TXT", "r") as f:
    num = int(f.readline().strip())

# Вызов функции
result = find_special_divisor(num)
with open("OUTPUT.TXt", "w") as file:
    file.write(str(result))