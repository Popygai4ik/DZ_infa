# def nod(a, b):
#     while b:
#         a, b = b, a % b
#     return a
#
# def fib(i):
#     a, b = 0, 1
#     for i in range(2, i + 1):
#         a, b = b, a + b
#     return b
#
# a, b = map(int, input().split())
# res = nod(fib(a), fib(b))
# print(res % (10 ** 9))
# from math import gcd
# def fib(i):
#     a, b = 0, 1
#     for i in range(2, i + 1):
#         a, b = b, a + b
#     return b
# a, b = map(int, input().split())
# nod = gcd(a, b)
# print(fib(nod)% (10 ** 9))
from math import gcd
a, b = map(int, input().split())
fib = []
v = 10 ** 9
g = gcd(a, b)
fib.append(1)
fib.append(1)
for i in range(2, max(a, b)):
    fib.append((fib[i - 1] + fib[i - 2]) % v)

print(fib[g - 1] % v)
# from math import gcd
#
# a, b = map(int, input().split())
# v = 10 ** 9
#
# pred, sled = 1, 1
#
# for _ in range(2, max(a, b)):
#     pred, sled = sled, (pred + sled) % v
#
# g = gcd(a, b)
# print(pred if g == 0 else sled if g == 1 else sled % v)
# # from math import gcd
# #
# # def find_fib_gcd(a, b):
# #     v = 10 ** 9
# #
# #     fib_prev, fib_curr = 0, 1
# #
# #     for _ in range(2, max(a, b) + 1):
# #         fib_prev, fib_curr = fib_curr, (fib_prev + fib_curr) % v
# #
# #     g = gcd(a, b)
# #     return fib_prev if g == 0 else fib_curr if g == 1 else fib_curr % g
# #
# # a, b = map(int, input().split())
# # result = find_fib_gcd(a, b)
# # print(result)
