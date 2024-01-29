def digit_sum(ishodnor_shilso, osnovanie):
    shislo = 0
    while ishodnor_shilso:
        shislo += ishodnor_shilso % osnovanie
        ishodnor_shilso //= osnovanie
    return shislo


n1, p1 = map(int, input().split())
n2, p2 = map(int, input().split())
d1 = digit_sum(n1, p1)
d2 = digit_sum(n2, p2)
if d1 == d2:
    print(d1)
else:
    print(0)

