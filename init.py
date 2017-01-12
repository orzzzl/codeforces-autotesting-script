#!/usr/bin/env python
# coding=utf-8

import subprocess
import urllib2
from bs4 import BeautifulSoup
import re


domain = "http://codeforces.com"
f = open("config", "r")
url = f.read()
req = urllib2.Request(url)
response = urllib2.urlopen(req)
page = response.read()
soup = BeautifulSoup(page, "html.parser")
all_links = soup.find_all(href=re.compile("problem/[A-Z]"))
for link in all_links:
    ele = domain + link['href']
    problem = ele[-1]
    print "process problem", problem
    page = urllib2.urlopen(ele).read()
    sp = BeautifulSoup(page, "html.parser")
    for br in sp.find_all("br"):
        br.replace_with("\n")
    samples = sp.find_all("pre")
    cnt = 0
    for s in samples:
        print "writing sample", cnt
        filename = ""
        if (cnt % 2 == 0):
            filename = str(problem) + str(cnt / 2) + ".in"
        else:
            filename = str(problem) + str(cnt / 2) + ".out"
        cnt += 1
        ff = open(filename, "w")
        ff.write(s.getText())
        ff.close()
