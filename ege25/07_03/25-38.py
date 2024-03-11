maxi_sumi = 0
mexi_deliteli = []
for i in range(268220, 270336):
    res = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            res.append(j)
            res.append(i // j)
    if len(set(res)) <= 4:
        sumi = sum(set(res))
        if sumi > maxi_sumi:
            maxi_sumi = sumi
            mexi_deliteli = sorted(set(res), reverse=True)

print(maxi_sumi, len(mexi_deliteli), *mexi_deliteli)
