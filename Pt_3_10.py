from pprint import pprint
string = input("Введите строку: ")
unique_letters_dict = {letter: string.count(letter) for letter in set(string)}
pprint(unique_letters_dict)
