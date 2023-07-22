a = int(input('введите число '))
stra = str(a)
step = len(stra)
temp = a
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit**step
    temp //= 10
if a == sum:
    print('это число армстронга')
else:
    print('это  не число армстронга')
