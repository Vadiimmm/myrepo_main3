a = input("Введите строку: ")
b = []
for i in a:
    k = ord(i)
    m = k + 3
    if m >= 123:
        m = 97 + (m - 123)
    b.append(chr(m))
print("".join(b))

    
