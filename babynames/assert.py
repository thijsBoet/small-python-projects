import os
import sys
import shutil

# import urllib.request, urllib.error, urllib.parse
# url = 'https://www.ssa.gov/cgi-bin/popularnames.cgi'
# response = urllib.request.urlretrieve(url, 'jongens_2018.txt')
# shutil.copy('D:\\python\\small-python-projects\\babynames\\baby1992.html', 'D:\\python\\small-python-projects\\babynames\\baby1992.txt')

baby1990 = open('baby1992.txt', 'r')
baby1990Content = baby1990.read()
baby1990.close()

print(baby1990Content)


# use regex to extract name, gender, year and rank

# sort by name

