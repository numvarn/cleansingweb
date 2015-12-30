#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import urlopen
from urlparse import urlparse
from getURLDB import GetPath
import os

def getWeb(urlid, url, directory):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # for none utf-8 web page
    if soup.original_encoding != 'utf-8':
        decoded_html = html.decode('tis-620')
        soup = BeautifulSoup(decoded_html, 'html.parser')

    # remove javascript
    to_extract = soup.findAll('script')
    for item in to_extract:
        item.extract()

    # remove inner CSS
    to_extract = soup.findAll('style')
    for item in to_extract:
        item.extract()

    text = soup.body.get_text()
    text = u''.join(text).encode('utf-8').strip()

    # process for file name from url
    filename = directory+'/'+str(urlid)+'.txt'

    # write result to file
    writeToFile(text, filename)

def writeToFile(str, filename):
    # write data in tmp file
    file = open('tmp.txt', 'w')
    file.write(str)
    file.close()

    removeEmptyLine(filename)

    # remove tmp file
    os.remove('tmp.txt')

def removeEmptyLine(filename):
    newcontent = []
    file1 = open('tmp.txt', 'r')

    for line in file1:
        if not line.strip():
            continue
        else:
            newcontent.append(line)

    # write data in target file
    filecontent = "".join(newcontent)
    file2 = open(filename, 'w')
    file2.write(filecontent)
    file2.close()

# Start program
def start():
    netloc = 'beezab.com'
    directory = '/Users/phisanshukkhi/Desktop/'+netloc

    # Create Object from GetPath Class
    # And query urlpath from DB
    getPath = GetPath(netloc)
    rows = getPath.getResult()

    # Create directory for store file
    if not os.path.exists(directory):
        os.makedirs(directory)

    count = 1
    for row in rows:
        print "GET : ", count," : ",row[0]," : ",row[1]
        count += 1
        getWeb(row[0], row[1], directory)

# Main Program
if __name__ == '__main__':
    start()

