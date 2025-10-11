import csv

file = open('assignment.csv', 'r') 
reader = csv.reader(file)

row_index = 0
for row in reader:
    col_index = 0
    while col_index < len(row):
        cell = row[col_index]
        if 'ai' in cell.lower():
            print("Match at Row", row_index + 1, "Column", col_index + 1, ":", cell)
        col_index += 1
    row_index += 1

file.close()

