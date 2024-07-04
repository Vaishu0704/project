import csv
with open('TD.csv') as csvfile:
    reader=csv.reader(csvfile)
    for col in reader:
        print(col[0],col[1],col[2],sep='|')