c = []
for i in range(1606, 9681):
    if i % 11 == 0 and i % 7 != 0 and i % 13 != 0 and i % 17 != 0 and i % 19 != 0:
        c.append(i)
print(f"Кол-во: {len(c)}")
print(f"Макс: {max(c)}")
