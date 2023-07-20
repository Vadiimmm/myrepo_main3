def find_palindromes(string):
    palindromes = []
    n = len(string)

    # Проверяем все возможные подстроки
    for i in range(n):
        for j in range(i+1, n+1):
            substring = string[i:j]

            # Проверяем, является ли подстрока палиндромом
            if substring == substring[::-1] and len(substring)>1 :
                palindromes.append(substring)

    return palindromes

# Пример использования
input_string = input("Введите строку: ")
result = find_palindromes(input_string)
print("Палиндромы в строке:", result)
