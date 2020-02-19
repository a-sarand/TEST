import csv

csv_data = [["StudentId", "Grade"], [123456, "A"]]
try:
    with open('person.csv', 'w', newline="") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csv_data)
except:
    print("Error in opening in file")

f = open("person.csv", 'rt')

reader = csv.reader(f)
for row in reader:
   print (row)