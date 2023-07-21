string1 = input('input string'')
string2 = ''
for char in string1:
    if char.isupper():
        string2 += char.lower()
    elif char.islower():
        string2 += char.upper()
    else:
        string2 += char
print(string2)
