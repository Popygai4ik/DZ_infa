from math import gcd

a, b = map(int, input().split())
nod = gcd(a, b)
print(nod)
