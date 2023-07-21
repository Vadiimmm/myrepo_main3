from functools import reduce
m = int(input("Введите кол-во элементов в списке"))
a = []
for i in range(0, m):
    k = int(input("Введите число"))
    a.append(k)
print(a)
srzn = reduce((lambda x, y: x + y), a) / m--ignore=E731
print(srzn)
