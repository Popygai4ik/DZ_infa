res = []

from fnmatch import fnmatch
for shilo in range(0, 10 ** 7):
    if fnmatch(str(shilo), '?6*6*?6'):
        if shilo % 6 == 0 and shilo % 8 == 0 and shilo % 7 == 0:
            s = 0
            for i in range(1, shilo + 1):
                if shilo % i == 0:
                    s+=i
            res.append((shilo, s))
        if len(res) == 7:
            break
res.sort(key=lambda x: x[0])
for shilo, q in res:
    print(shilo, q)
