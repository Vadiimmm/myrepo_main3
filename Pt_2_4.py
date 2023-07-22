a = int(input('input a'))
b = int(input('input b'))
c = int(input('input c'))
d = b**2 - 4 * a * c
if d < 0:
    print('корней нет')
elif d == 0:
    x = (-b) / (2 * a)
    print(f'x = {x}')
else:
    x1 = (-b + d**0.5)/(2 * a)
    x2 = (-b - d**0.5)/(2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
