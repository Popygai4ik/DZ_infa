n, k = map(str, input().split())
n = int(n)
l_k = len(k)
fak = 1
for i in range(n, 0, -l_k):
    fak = fak * i
print(fak)
