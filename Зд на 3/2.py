n1 = int(input())
с = 0
# Здесь поиск для старта и конца, чтобы проходили отрицательные числы и другие не стандартные вводы
start = min(1, n1)
stop = max(1, n1) + 1
for i in range(start, stop):
    с += i
print(с)

