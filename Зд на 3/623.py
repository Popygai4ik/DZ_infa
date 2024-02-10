# n1 = int(input())
# if n1 == 0:
#     print(0)
# elif n1 == 1:
#     print(1)
# else:
#     a, b = 1, 1
#     for i in range(1, (n1) % 60):
#         a, b = b, (a + b) % 10
#     print(b)
# n1 = int(input())
# last_stifri = [1,1,2,3,5,8,3,1,4,5,9,4,3,7,0,7,7,4,1,5,6,1,7,8,5,3,8,1,9,0,9,9,8,7,5,2,7,9,6,5,1,6,7,3,0,3,3,6,9,5,4,9,3,2,5,7,2,9,1]
# print(last_stifri[n1 % 60])
def last_stifri():
    a, b = 0, 1
    res = []
    for i in range(60):
        a, b = b, a + b
        res.append(a % 10)
    return res


n = int(input('i = '))
res = last_stifri()
print(res[n % 60])
