def ymn(n):
    c = 1
    lis = list(map(int, str(n).split()))
    for i in lis:
        c *= i
    return c
res = 1
n = int(input())
current_number = 1
while True:
    product = ymn(current_number)
    if product == n:
        break

    current_number += 1
print(res)