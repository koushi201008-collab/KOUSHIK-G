import csv

choice = input("Enter 'even' or 'odd': ").strip().capitalize()

with open('numbers.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        if row[1] == choice:
            print(row[0])
