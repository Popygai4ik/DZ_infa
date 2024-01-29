"""
Напишите программу, которая вводит два целых числа и находит их произведение
, не ис-пользуя операцию умножения. Учтите, что числа могут быть отрицательными.
"""
n1 = int(input())
n2 = int(input())
znak = 0
if n1 < 0 and n2 < 0:
    znak = 1
elif n1 < 0 or n2 < 0:
    znak = -1
else:
    znak = 1
n1 = abs(n1)
n2 = abs(n2)
res = 0
for i in range(n2):
    res = res + n1
if znak == -1:
    print(-res)
else:
    print(res)