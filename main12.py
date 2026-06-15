import csv

file_path = 'airport-codes_csv (1).csv'

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        if row.get('iso_country') == 'UA':
            print(row.get('name'))