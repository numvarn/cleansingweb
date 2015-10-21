import csv
# with open('items.csv', 'wb') as csvfile:
cr = csv.reader(open("items.csv","rb"))
for row in cr:
    print row[1].decode('tis-620'), row[2]

