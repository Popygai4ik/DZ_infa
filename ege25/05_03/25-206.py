res = []

for i in '0123456789':
    for j in '0123456789':
        shilo = int(f'1{i}34567{j}9')
        if shilo % 17 == 0:
            shastnoe = shilo // 17
            res.append((shilo, shastnoe))

res.sort(key=lambda x: x[0])
for shilo, shastnoe in res:
    print(shilo, shastnoe)
