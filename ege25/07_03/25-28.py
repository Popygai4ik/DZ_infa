for i in range(244143, 367822):
    res = []
    for j in range(1, int(i ** 0.5) + 1):
        if i % j == 0:
            res.append(j)
            res.append(i // j)
    if len(set(res)) == 5:
        print(*sorted(res))

