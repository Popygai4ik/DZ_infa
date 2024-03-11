res = []

from fnmatch import fnmatch
for shilo in range(10 ** 7 - 1, 0, -1):
    if fnmatch(str(shilo), '14?4*'):
        if shilo % 217 == 0:
            s = 0
            for i in range(1, shilo + 1):
                if shilo % i == 0 and i % 2 != 0:
                    s+=i
            res.append((shilo, s))
        if len(res) == 7:
            break
res.sort(key=lambda x: x[0])
for shilo, q in res:
    print(shilo, q)
