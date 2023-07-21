n = int(input("введи предел"))
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1 --ignore=E731
a = []
for i in range(1, n):
    if fib(i) > n:
        break
    a.append(fib(i))
print(a)
