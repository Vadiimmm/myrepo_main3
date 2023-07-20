try:
    num = int(input("Введите число больше 11: "))
    x = [a for a in str(num)]
    
    for i in range(len(x)-1):
        for j in range(len(x)-i-1):
            if x[j] < x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    print(''.join(x))
except ValueError:
    print("Неверное значение")
