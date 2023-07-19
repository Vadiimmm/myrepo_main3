from pprint import pprint
string = input("Введите строку: ")
vowels = ['a', 'e', 'i', 'o', 'u']
d = dict()
for letter in string:
    if letter.lower() in vowels:
        d[letter] = True
    else:
        d[letter] = False
pprint(d)
