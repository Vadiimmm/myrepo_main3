import random
print('0 - орел, 1 - решка')
mas = ['орел', 'решка']
orl = random.choice(mas)
w = 0
l = 0
while l < 3:
    orl = random.choice(mas)
    a = int(input('введите ваш вариант'))
    if a == 1 or a == 0:
        if a == 0 and orl == 'орел' or a == 1 and orl == 'решка':
            w += 1
        else:
            l += 1
        print(f'выйгрыш - {w}, проигрыш - {l}')
    else:
        break
