def nod(a,  b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
a, b = map(int, input().split())
nod = nod(a, b)
nok = a * b // nod
print(nok)
"""
while a != b:: Запуск цикла while до тех пор, пока a не станет равным b.
if a > b: и else:: Проверка условия. Если a больше b, то из a вычитается b, иначе из b вычитается a.
return a: Возврат значения a после завершения цикла, когда a и b станут равными (наименьший общий делитель найден).
nok = a * b // nod: Вычисление наименьшего общего кратного (НОК) по формуле a * b // nod.
"""