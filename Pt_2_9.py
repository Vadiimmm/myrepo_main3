number = int(input("Введите натуральное число: "))
number = str(number)
max_digit = max(number)
digit_position_end = len(number) - number.index(max_digit)
digit_position_start = number.index(max_digit) + 1
print(f"Порядковый номер макс цифры от конца: {digit_position_end}")
print(f"Порядковый номер макс цифры от начала: {digit_position_start}")
