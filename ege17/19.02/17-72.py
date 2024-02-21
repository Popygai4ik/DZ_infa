с = 0
max_8 = 0

for i in range(2848, 109500):
    if '9' in str(i):
        suma_stifr = sum(int(j) for j in str(i) if int(j) > 5)
        if suma_stifr % 3 == 0:
            с += 1
            if str(i).startswith('8'):
                max_8 = i
print(с, max_8)

