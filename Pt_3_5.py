import math
m = int(input("введите кол-во чисел"))
nums = []
r = 0
for i in range(0, m):
    k = int(input("введите число"))
    nums.append(k)
print("начальный список: ", nums)
for n in nums:
    for i in range(1, n + 1):
        if n % i == 0:
            r += 1
    lst = [n for n in nums if r > 2]
    r = 0
print("конечный список: ", lst)
