import csv

with open("API.py", "r") as csv_file:
    reader = csv.reader(csv_file, delimiter="|")
    print(API.text)
