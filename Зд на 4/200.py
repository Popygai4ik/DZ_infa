n, k = map(int, input().split())
zeros_count = 0
while n >= k:
    n //= k
    zeros_count += n
print(zeros_count)
