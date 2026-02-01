import csv

daten = [
["Name", "Age", "City"],
["Ali",40, "Köln"],
["Anna", 20, "Dinslaken"]
]

with open("my.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(daten)

with open("my.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)