def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n1 = int(input())
s_n1 = str(n1)
vozrast = int("".join(sorted(s_n1)))
ybivani = int("".join(sorted(s_n1, reverse=True)))
f = is_prime(vozrast) and is_prime(ybivani)
if f:
    print("Yes")
else:
    print("No")
