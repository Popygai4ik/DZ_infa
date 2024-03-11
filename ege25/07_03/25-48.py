n, m = 2484292, 2484371
m1 = m + 1
ma = [True] * m1
ma[0] = False
ma[1] = False
f = False
for i in range(int(m ** 0.5) + 1) :
    if i % 2 != 0 or i == 2 :
        if ma[i] :
            for j in range(i + i, m1, i) :
                ma[j] = False

ans = [i for i in range(n, m1) if ma[i]]
c = 0
for i in ans :
    c += 1
    print(f"{c} {i}", sep='\n')

