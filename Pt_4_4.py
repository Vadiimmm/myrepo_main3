import itertools
def find_combinations(numbers, target_sum):
    combinations = []
    for r in range(1, len(numbers) + 1):
        for combination in itertools.combinations(numbers, r):
            if sum(combination) == target_sum:
                combinations.append(combination)
    combinations = list(set(combinations))
    return combinations


input_numbers = input("Введите список чисел через пробел: ")
numbers = list(map(int, input_numbers.split()))
target_sum = int(input("Введите целевую сумму: "))
result = find_combinations(numbers, target_sum)
print("Уникальные комбинации суммы", target_sum, ":", result)
