m = int(input("введите кол-во чисел"))
nums = []
for i in range(0, m):
    k = int(input("введите число"))
    nums.append(k)
print("начальный список: ", nums)
squares = [n * n for n in nums]
print("конечный список: ", squares)
