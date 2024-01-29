def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def suma(n):
    return sum(int(i) for i in str(n))

a, b = map(int, input().split())

m_sum = -1
m_shislo = -1
f = False
for i in range(b, a - 1, -1):
    if is_prime(i):
        f = True
        seisha_suma = suma(i)
        if seisha_suma > m_sum or (seisha_suma == m_sum and i > m_shislo):
            m_sum = seisha_suma
            m_shislo = i
print(m_shislo)
```516:


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_2_prime(num):
    str_num = str(num)
    increasing_order = int("".join(sorted(str_num)))
    decreasing_order = int("".join(sorted(str_num, reverse=True)))

    return is_prime(increasing_order) and is_prime(decreasing_order)


n1 = int(input())
if is_2_prime(n1):
    print("Yes")
else:
    print("No")
831:
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def digit_sum(num):
    return sum(int(digit) for digit in str(num))

a, b = map(int, input().split())

max_sum = -1
max_number = -1
found_prime = False

for number in range(b, a - 1, -1):
    if is_prime(number):
        found_prime = True
        current_sum = digit_sum(number)
        if current_sum > max_sum or (current_sum == max_sum and number > max_number):
            max_sum = current_sum
            max_number = number

if found_prime:
    print(max_number)
else:
    print("В заданном диапазоне нет простых чисел.")

```