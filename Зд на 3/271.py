n = int(input())
a = 0
b = 1
next = 0
shitshik = 0
while next < n:
    a, b = b, next
    next = a + b
    shitshik += 1

if next == n:
    print(1)
    print(shitshik)
else:
    print(0)
def find_fibonacci_position(target):
    a, b = 0, 1
    next_val = 0
    position = 0

    while next_val < target:
        a, b = b, next_val
        next_val = a + b
        position += 1

    return position, next_val

number = int(input())
position, value = find_fibonacci_position(number)

if value == number:
    print("1")
    print(position)
else:
    print("0")


"""
Конечно, давайте разберем этот код.

n1 - это число, которое пользователь вводит с клавиатуры. Программа будет проверять, является ли оно числом Фибоначчи.

previous и current - переменные для хранения двух последних чисел Фибоначчи в процессе их генерации.

flag - булева переменная, которая будет установлена в True, если n1 является числом Фибоначчи.

В цикле for генерируются числа Фибоначчи до тех пор, пока next_value не станет равным n1 или не превысит его. Если next_value станет равным n1, устанавливается флаг flag, и цикл прерывается.

Если флаг установлен, программа выводит "1" и значение переменной num, которая содержит порядковый номер числа Фибоначчи. В противном случае, программа выводит "0".

Код проверяет, является ли введенное пользователем число числом Фибоначчи, и выводит результат.




"""