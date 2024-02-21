import math

c = 0
mini = 125890
for i in range(1031, 125889):
    if i % 10 != 5 and math.sqrt(i) % 1 == 0:
        c += 1
        if i % 100 == 36:
            if mini > i:
                mini = i

print(c, mini)
