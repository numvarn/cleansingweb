#!/usr/bin/python

import csv
import os
from urlparse import urlparse

targetOutput = open("/Users/phisan/Desktop/filtered.csv", "wb")
writer = csv.writer(targetOutput, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
<<<<<<< HEAD
rows = csv.reader(open("/Users/phisan/Desktop/urllist.csv","rb"))
=======
rows = csv.reader(open("/Users/phisanshukkhi/Desktop/items.csv","rb"))
>>>>>>> 08a6ea34f8f2cd14c82b43799a9ac842aec1cc0d

count = 0
for row in rows:
    if len(row) != 0:
        url = row[0]
        path = urlparse(url).path
        ext = os.path.splitext(path)[1]

        if ext!=".jpg" and ext!=".jpeg" and ext!=".JPG" and ext!=".JPEG" and ext!=".pdf" and ext!=".doc" and ext!=".gif" and ext!=".swf" and ext!=".png" and ext!=".js":
<<<<<<< HEAD
            newrow = ['health.mthai.com', row[0]]
=======
            newrow = ['health.sanook.com', row[0]]
>>>>>>> 08a6ea34f8f2cd14c82b43799a9ac842aec1cc0d
            writer.writerow(newrow)
            count += 1

targetOutput.close()
