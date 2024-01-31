numbers = list(map(int, input().split()))
results = [1 if is_smith_number(num) else 0 for num in numbers]
print(" ".join(map(str, results)))
