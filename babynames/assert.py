import os
import sys
import urllib.request, urllib.error, urllib.parse

# open html pages
# https://www.svbkindernamen.nl/int/nl/kindernamen/wizard/zoeknaam/jongensnamen_2018/index.html

# https://programminghistorian.org/en/lessons/working-with-web-pages
#https://programminghistorian.org/en/lessons/downloading-multiple-records-using-query-strings

url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
response = urllib.request.urlopen(url)
webContent = response.read()

print(webContent)

# save html pages

# convert to one txt file

# use regex to extract name, gender, year and rank

# sort by name

