c = []
for i in range(3201, 12877):
    if i % 4 == 0 and i % 7 != 0 and i % 13 != 0 and i % 11 != 0 and i % 19 != 0:
        c.append(i)
print(f"Кол-во: {len(c)}")
print(f"Макс: {max(c)}")

