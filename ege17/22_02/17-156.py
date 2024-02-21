a = []
for i in open('17-2.txt'):
    a.append(int(i))
maxi = max(a)
print(a.count(maxi), a.index(maxi) + 1)