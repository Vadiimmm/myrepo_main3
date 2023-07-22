dist = int(input('сколько хотите проехать? '))
rashod = int(input('сколько автомобиль расходует за 100км? '))
oil = int(input('сколько литров у вас в баке?'))
if dist <= oil / rashod:
    print('проедите')
else:
    print('не проедите')
