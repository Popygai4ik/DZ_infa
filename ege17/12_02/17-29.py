def convert(n, base):
    if n == 0:
        return '0'
    stifri = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    while n > 0:
        digit = n % base
        res = stifri[digit] + res
        n //= base
    return res
c = []
for i in range(2807, 8559):
    f = convert(i, 2)
    f2 = convert(i, 9)
    if (int(f) % 100 == 11) and (int(f2) % 10 == 5):
        c.append(i)
print(f"Макс: {max(c)}")
print(f"Сумма: {sum(c)}")
