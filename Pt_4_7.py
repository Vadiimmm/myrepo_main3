import itertools
input_str = input("Введите список через пробел: ")
a = input_str.split()
print("Начальный список: ", a)
combinations = []
combinations = list(itertools.permutations(a))

print("варианты перестановок: ", combinations)
