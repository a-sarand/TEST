import csv

f=open('100 sales records.csv','rt')

reader=csv.reader(f)
counter = 0
for row in reader:
    if row[0] == "Europe":
        counter+=1
print("All the records of europe %d" %counter)

f1=open('100 sales records.csv','rt')
reader=csv.reader(f1)
next(reader)
total=0
for row in reader:
    total += int(row[8])
print(total)

f2=open('100 sales records.csv','rt')
reader=csv.reader(f2)
itemType={}
next(reader)
for row in reader:
    itemType[row[2]]=""

list=itemType.keys()
print(list)




