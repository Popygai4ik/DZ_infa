# n1 = int(input())
#
# sheschik_sumi_posledovatelnosti = 1
# shetchik = 1
#
# while shetchik * (shetchik + 1) < 2 * n1:
#     if (n1 - shetchik * (shetchik - 1) / 2) % shetchik == 0:
#         sheschik_sumi_posledovatelnosti = shetchik
#     shetchik += 1
#
# print(sheschik_sumi_posledovatelnosti)
n1 = int(input("Введите натуральное число: "))

sheschik_sumi_posledovatelnosti = 1
max_start = 1

for start in range(1, n1 + 1):
    count = 0
    total = 0
    while total < n1:
        count += 1  
        total = total + start + count - 1
        if total == n1 and count > sheschik_sumi_posledovatelnosti:
            sheschik_sumi_posledovatelnosti = count
            max_start = start

print("Максимальное количество чисел:", sheschik_sumi_posledovatelnosti)
