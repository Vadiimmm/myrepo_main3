import csv
try:  
    a = ''
    b = []
    n = int(input("введите начальный год"))
    m = int(input("введите начальный год"))

    with open('books.csv') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            a = ', '.join(row)
            b = a.split(";")
            if int(b[2]) >= n and int(b[2]) <= m:
                print(row)
            else:
                print("Нет подходящих данных")
                break
except ValueError:
    print("Неверное значение")
                
            
       
        
