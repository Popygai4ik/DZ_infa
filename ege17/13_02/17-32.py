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
for i in range(1000, 10000):
    f = convert(i, 6)
    r = f[-2:]
    if (r == '13' or r == '14') and len(f) <= 5:
        c.append(i)
k = len(c)
maxi = max(c)
print(k, maxi)