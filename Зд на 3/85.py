def nod(a,  b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
# a, b = map(int, input().split())
# a1 = ''
# b1 = ''
# for i in range(a):
#     a1 = a1 + '1'
# for i in range(b):
#     b1 = b1 + '1'
# print(nod(int(a1), int(b1)))
from math import gcd

a, b = map(int, input().split())
nod = gcd(a, b)
res = '1' * nod
print(res)
