a = int(input('input number between 10 and 20'))

while a < 10 or a > 20:
        if a >= 10 and a <= 20:
                print('thank you')
        if a < 10:
                print('number is less than 10')
        else:
                print('number is more than 20')
        a = int(input('try again'))
if a >= 10 and a <= 20:
        print('thank you')
