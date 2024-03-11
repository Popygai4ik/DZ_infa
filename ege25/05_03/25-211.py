res = []

spidok = '0123456789ABCDEF'
for i in spidok:
    for j in spidok:
        shilo = int('1'+i+'DED'+j+'CED',16)
        if shilo % 121 == 0:
            shastnoe = shilo // 121
            res.append((shilo, shastnoe))
res.sort(key=lambda x: x[0])

for shilo, q in res[::-1]:
    print(shilo, q)
