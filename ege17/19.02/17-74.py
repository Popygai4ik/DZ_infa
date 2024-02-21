def stiri_raznie(n):
    for j in str(n):
        if str(n).count(j) > 1:
            return False
    return True

def suma_stifr(n):
    return sum(1 for j in str(n) if int(j) > 4)

naibolee_30000 = 0
pred_ranitsa = 99999999999999999999
c = 0

for i in range(5903, 174204):
    if stiri_raznie(i) and suma_stifr(i) == 3:
        c += 1
        rznitsa = abs(i - 30000)
        if rznitsa < pred_ranitsa:
            pred_ranitsa = rznitsa
            naibolee_30000 = i

print(c, naibolee_30000)
