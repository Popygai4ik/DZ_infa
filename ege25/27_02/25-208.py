res = []

from fnmatch import fnmatch
for shilo in range(0, 10 ** 6):
    if fnmatch(str(shilo), '12*45*'):
        if shilo % 51 == 0:
            shastnoe = shilo // 51
            res.append((shilo, shastnoe))
res.sort(key=lambda x: x[0])
for shilo, q in res:
    print(shilo, q)

