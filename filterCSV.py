#!/usr/bin/python

import csv

filterNetLoc = ["www.networkherbs.com"]

targetOutput = open("/Users/phisan/Desktop/filtered.csv", "wb")
writer = csv.writer(targetOutput, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
rows = csv.reader(open("/Users/phisan/ResearchCode/webcrawler/TextMining/spiders/items.csv","rb"))

netloclist = []
urllist = []
desclist = []
for row in rows:
    if row[0] in filterNetLoc and row[1] not in urllist:
        netloclist.append(row[0])
        urllist.append(row[1])
        desclist.append(row[2])

index = 0
for netloc in netloclist:
    newrow = []
    newrow.append(netloclist[index])
    newrow.append(urllist[index])
    newrow.append(desclist[index])
    writer.writerow(newrow)
    index += 1

targetOutput.close()
