import random
print('доступные цвета: красный, синий, зеленый, белый, черный')
str = input('выберете цвет: ')
mas = ['красный', 'зеленый', 'синий', 'белый', 'черный']
ch1 = random.choice(mas)
while str != ch1:
    if ch1 == 'красный':
        print('цвет любви')
    elif ch1 == 'зеленый':
        print('цвет весны')
    elif ch1 == 'синий':
        print('цвет морской волны')
    elif ch1 == 'белый':
        print('цвет чистоты и ясности')
    else:
        print('цвет космоса')
    str = input('попробуйте снова ')
if str == ch1:
    print('отлично')
