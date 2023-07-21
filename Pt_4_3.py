a = int(input("введите начало диапазона: "))
b = int(input("введите конец диапазона: "))
d = 2
for i in range(a, b + 1):
    while i % d != 0:
        d += 1
    if d == i:
        print(i)
    d = 2
