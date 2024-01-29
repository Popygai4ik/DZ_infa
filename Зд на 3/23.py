n1 = int(input())
res = 0
start = min(1, n1)
stop = max(1, n1) + 1
for i in range(start, stop):
    if n1 % i == 0:
        res += i
print(res)
