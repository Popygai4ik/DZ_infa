a, b = map(int, input().split())
c = []
for i in range(a, b + 1):
    kv = str(i ** 2)
    if kv.endswith(str(i)):
        c.append(i)
print(*c)
