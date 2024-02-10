c = []
for i in range(2568, 7859):
    if ((i % 4 == 0) or (i % 5 == 0)) and (i % 11 != 0) and (i % 20 != 0) and (i % 27 != 0):
        c.append(i)
print(f"Минимум: {min(c)}")
print(f"Макс: {max(c)}")
