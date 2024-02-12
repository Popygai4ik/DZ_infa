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
for i in range(1871, 9198):
    f = convert(i, 16)
    f2 = convert(i, 10)
    if len(f) != len(f2) and (i % 9 == 2 or i % 9 == 3):
        c.append(i)
k = len(c)
mini = min(c)
print(k, mini)
