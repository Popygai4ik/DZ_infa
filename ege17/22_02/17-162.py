a = []
for i in open('17-3.txt'):
    a.append(int(i))
c = 0
mini = 88005553535
for i in range(len(a) - 1):
    if ((a[i] + a[i + 1]) / 2) % 7 == 0 and (a[i] * a[i + 1]) % 2 != 0:
        c += 1
        mini = min(mini, ((a[i] + a[i + 1]) // 2))
print(c, mini)
