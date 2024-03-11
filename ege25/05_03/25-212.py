res = []

spidok = '0123456789ABCDEF'
for i in spidok:
    for j in spidok:
        shilo = int('1'+i+'DED'+j+'BABA',16)
        if shilo % 186 == 0:
            shastnoe = shilo // 186
            res.append((shilo, shastnoe))
res.sort(key=lambda x: x[0])

for shilo, q in res[::-1]:
    print(shilo, q)
