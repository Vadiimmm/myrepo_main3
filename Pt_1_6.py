string1 = input('input string')
words = string1.split()
capitalized_words = [word.capitalize() for word in words]
capitalized_string = ' '.join(capitalized_words)
print(capitalized_string)