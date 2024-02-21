c = []
def sum_of_stifr(n):
    return sum(int(digit) for digit in str(n))
for i in range(2894, 174883):
    if i % 10 == 8 and sum_of_stifr(i) > 22:
        c.append(i)
print(len(c), c[12])