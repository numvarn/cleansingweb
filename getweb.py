#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib import urlopen
from getURLDB import GetPath
import os
import sys

def getWeb(urlid, url, directory):
    # process from local html file
    file_path = directory+'/'+str(urlid)+'.html'

    # check file is exist before process
    if os.path.isfile(file_path):
        html = urlopen(file_path).read()
        soup = BeautifulSoup(html, 'html.parser')

        # for none utf-8 web page
        if soup.original_encoding != 'utf-8':
            try :
                decoded_html = html.decode('tis-620')
                soup = BeautifulSoup(decoded_html, 'html.parser')
            except :
                print "Dectect error ", urlid, " -- ", url
                pass

        # remove javascript
        to_extract = soup.findAll('script')
        for item in to_extract:
            item.extract()

        # remove inner CSS
        to_extract = soup.findAll('style')
        for item in to_extract:
            item.extract()

        # check current document is HTML or FEED
        # text = soup.body.get_text()
        text = soup.get_text()
        text = u''.join(text).encode('utf-8').strip()

        # process for file name from url
        target = directory+'/processed/'
        if not os.path.exists(target):
            os.makedirs(target)
        filename = target+str(urlid)+'.txt'

        # write result to file
        writeToFile(text, filename)
    else:
        print "file ID "+str(urlid)+" is not exist."

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
def main(netloc):
    # netloc = 'beezab.com'
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
        print "Processed : ", count," : ID -- ",row[0], " : ", row[1]
        count += 1
        getWeb(row[0], row[1], directory)

# Main Program
# Get Network Location from command line argument
if __name__ == '__main__':
    if len(sys.argv) != 1:
        main(sys.argv[1])
    else:
        print "Please, Enter Network Location"

