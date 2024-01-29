n1 = int(input())
res = 1
b_s = 0
for i in range(1, n1 + 1):
    if n1 % i == 0:
        s = sum(int(stifra) for stifra in str(i))
        if s > b_s or (s == b_s and i < res):
            b_s = s
            res = i
print(res)
