number = int(input("Введите натуральное число: "))
number = str(number)
max_digit = max(number)
max_digit_position_from_end = len(number) - number.index(max_digit)
max_digit_position_from_start = number.index(max_digit) + 1
print(f"Порядковый номер максимальной цифры от конца числа: {max_digit_position_from_end}")
print(f"Порядковый номер максимальной цифры от начала числа: {max_digit_position_from_start}")