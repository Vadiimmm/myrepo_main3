mas = ['поле чудес', 'сто к одному', 'слабое звено', 'своя игра']
for i in range(0, len(mas)):
    print(mas[i])
a = input('введите передачу')
b = int(input(' введите позицию от 1 до 5'))
c = []
if b < 1 or b > 5:
    print('неверная позиция')
else:
    for i in range(0, b -1):
        c.append(mas[i])
    c.append(a)
    for i in range(b - 1, len(mas)):
        c.append(mas[i])
    for i in range(0, len(c)):
        print(c[i])
	
	
