a = []
for i in open('17-3.txt'):
    a.append(int(i))
count = 0
maxi = -88005553535
for i in range(len(a) - 1):
    if (a[i] % 2 == 0 and a[i] % 4 == 0 and a[i + 1] % 2 != 0 and a[i + 1] % 11 == 0) or \
       (a[i] % 2 != 0 and a[i] % 11 == 0 and a[i + 1] % 2 == 0 and a[i + 1] % 4 == 0):
        count += 1
        maxi = max(maxi, a[i] + a[i + 1])

print(count, maxi)
