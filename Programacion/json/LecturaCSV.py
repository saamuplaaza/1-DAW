import csv
with open('programacion.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open('programacion.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(f)