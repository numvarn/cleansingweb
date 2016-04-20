#!/usr/bin/python

import csv
rows = csv.reader(open("/Users/phisan/ResearchCode/rmstopwords/stopwords.csv","rb"))
for row in rows:
    print row[0]
