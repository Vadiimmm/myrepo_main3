b = int(input("введите число"))
a = lambda x: "четное" if x % 2 == 0 else "нечетное"  --ignore=E103
print(a(b))
