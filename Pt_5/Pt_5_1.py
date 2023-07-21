import csv
books = [
    ["The witcher: The last wish", "Andrzej Sapkowski", "1993"],
    ["Metro 2033", "Dmitry Glukhovsky", "2002"],
    ["The Hobbit, or There and Back Again", "J. R. R. Tolkien", "1937"],
    ["A Man Called Ove", "Fredrik Backman", "2012"],
    ["Flowers for Algernon", "Daniel Keyes", "1958"],
    ]
with open("books.csv", "w", encoding = "cp1251", newline = "") as file:
    writer = csv.writer(file, delimiter = ";")
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




    
