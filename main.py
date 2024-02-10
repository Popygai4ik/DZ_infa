def calculate_fac(number, fak):
    n = int(number)
    fak_length = len(fak)
    result = 1
    for i in range(n, 0, -fak_length):
        result *= i
    return result

num, kolva = map(str, input().split())
result = calculate_fac(num, kolva)
print(result)