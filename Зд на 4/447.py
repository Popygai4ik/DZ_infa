n1 = int(input())
last = 1
fak = 1
for i in range(1, n1 + 1):
    fak *= i
    while fak % 10 == 0:
        fak //= 10
    last = fak % 10
print(last)
