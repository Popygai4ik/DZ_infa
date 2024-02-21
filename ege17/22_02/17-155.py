a = []
for i in open('17-1.txt'):
    a.append(int(i))
count = 0
b = []
maximi = -88005553535
for i in range(1, len(a) - 1):
    if min(a[i - 1], a[i], a[i + 1]) == a[i]:
        b.append(a[i])
        maximi = max(maximi, a[i])
print(len(b), maximi)
