a = [int(x) for x in open('17-3.txt')]

c = 0
mini = 926347623694928348729384792349872839479832749872389479823498674895734795734975893475987348957349875347958734895734987598347589734985739475843

for i in range(len(a) - 2):
    if a[i] < a[i + 1] < a[i + 2]:
        c += 1
        raznitsa = a[i + 2] - a[i]
        if raznitsa < mini:
            mini = raznitsa

print(c, mini)