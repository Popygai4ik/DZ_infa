a = []
for i in open('17-1.txt'):
    a.append(int(i))
count = 0
b = []
minimymi = 100000000
for i in range(len(a) - 1):
  if (abs(a[i]) % 10 == 6 and abs(a[i]) % 3 == 0) or (abs(a[i + 1]) % 10 == 6 and abs(a[i + 1]) % 3 == 0):
    b.append((a[i], a[i + 1]))
    minimymi = min(minimymi, a[i], a[i + 1])
print(len(b), minimymi)
