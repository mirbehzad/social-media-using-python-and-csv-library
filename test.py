import csv

with open('genders.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        print(line)
