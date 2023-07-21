import csv
try:
    n = int(input("введите количество записей: "))
    books = []
    for i in range(n):
        row = input("Введите название, автора, год через запятую:").split(", ")
        for i in range(len(row)):
            row[i] = str(row[i])
        books.append(row)

    with open("books.csv", "w", encoding="cp1251", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(
            (
                "Книга",
                "Автор",
                "Год выпуска"
            )
        )
        writer.writerows(
            books
        )
    print(books)
    a = []
    k = 0
    avtor = str(input("Введите нужного автора: "))
    for i, word in enumerate(books):
        for j in word:
            if avtor == str(books[i][1]):
                print(' '.join(word))
                k += 1
                break
    if k == 0:
        print("Нет подходящего автора")
except ValueError:
    print("Неверное значение")
