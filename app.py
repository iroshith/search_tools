#-*- coding:utf-8 -*-
__doc__ = u"""
"""
import sys
reload(sys)  
sys.setdefaultencoding('utf8')
sys.path.append("./googlesearch/")
from googlesearch import search

from HTMLParser import HTMLParser
import urllib2
import csv


class GetTitle(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title_flag = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.title_flag = True

    def handle_data(self, data):
        if self.title_flag:
            self.title = data
            self.title_flag = False

def main():
    gt = GetTitle()
    f = open(sys.argv[1], 'rb')
    reader = f.readlines()
    f.close()
    for row in reader:
        for url in search(row, stop=20):
            print url
    	    try:
                response = urllib2.urlopen(url)
                gt.feed(response.read())
                gt.close()
                print gt.title.encode('utf-8')
            except Exception, e:
                print e
if __name__ == '__main__':
    main()