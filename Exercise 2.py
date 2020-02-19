import csv

f=open('100 sales records.csv','rt')

reader=csv.reader(f)
data = []
for row in reader:
    data.append([row[0],row[1],row[13]])
with open('data.csv','w',newline="") as csvFile:
    writer=csv.writer(csvFile)
    writer.writerows(data)
