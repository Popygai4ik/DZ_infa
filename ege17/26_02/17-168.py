a = []
for i in open('17-3.txt'):
    a.append(int(i))
c = 0
mini = 1234567890987654323456789

for i in range(len(a) - 3):
    f = a[i:i + 4]
    if a[i] > a[i + 1] > a[i + 2] > a[i + 3]:
        if a[i] - a[i + 3] > 1000:
            c += 1
            mini = min(mini, sum(a[i:i + 4]))

print(c, mini)

