def suma_stifr(n):
    return sum(int(i) for i in str(n))

def mal_stifra(n):
    stifri = [int(i) for i in str(n)]
    mini = min(stifri)
    pervi_tre = stifri[:3]
    return mini not in pervi_tre
def sred(numbers, sred):
    res = []
    for i in numbers:
        res.append(abs(sred - i))
    return numbers[res.index(min(res))]

c = []
for i in range(2020, 647039):
    if suma_stifr(i) < 10 and mal_stifra(i):
        c.append(i)

if c:
    srdne = sum(c) // len(c)
    closest_num = sred(c, srdne)
    dlina = len(c)
print(dlina, closest_num)
