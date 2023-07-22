import random
print('0 - орел, 1 - решка')
mas = ['орел', 'решка']
orl = random.choice(mas)
w = 0
k = 0
while k < 3:
    orl = random.choice(mas)
    a = int(input('введите ваш вариант'))
    if a == 1 or a == 0:
        if a == 0 and orl == 'орел' or a == 1 and orl == 'решка':
            w += 1
        else:
            k += 1
        print(f'выйгрыш - {w}, проигрыш - {k}')
    else:
        break
