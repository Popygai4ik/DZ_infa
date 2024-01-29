n1 = int(input())
if n1 == 0:
    print(0)
elif n1 == 1:
    print(1)
else:
    a, b = 0, 1
    for i in range(2, n1 + 1):
        a, b = b, a + b
    print(b)