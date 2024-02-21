def max_stifra(n):
    return max(map(int, str(n)))

count = 0
max_50 = 0

for i in range(1007, 746002):
    first = int(str(i)[0])
    if first == max_stifra(i):
        kolvo_5 = str(i).count('5')
        if kolvo_5 >= 2 and kolvo_5 % 2 == 0:
            count += 1
            if str(i).startswith('50'):
                max_50 = i

print(count, max_50)
