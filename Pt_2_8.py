n = int(input('введите n '))
for i in range(0, n):
    if i ** 2 > n:
        m = i
        break
print(m)
