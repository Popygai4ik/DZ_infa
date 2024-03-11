from fnmatch import fnmatch
res = []
for i in range(92, 10 ** 8 + 1, 92):
    if fnmatch(str(i), "12[0,2,4,6,8]4[1,3,5,7,9]6?8"):
        res.append((i, i // 92))
res.sort(key=lambda x: x[0])
for i in res:
    print(i[0], i[1])