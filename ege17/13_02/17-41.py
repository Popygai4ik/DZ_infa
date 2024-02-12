c = []
for i in range(2371, 9433):
    if (((i % 8 == 5) and ((i // 8) % 8 == 1)) or ((i % 8 == 7) and ((i // 8) % 8 == 1))) and (i % 3 != 0) and (i % 5 != 0):
        c.append(i)
k = len(c)
mini = max(c)
print(k, mini)
