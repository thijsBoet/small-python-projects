import os
import sys
import re

os.chdir('D:\\python\\small-python-projects\\babynames')

baby2018 = open('baby2018.html', 'r')
baby2018Content = baby2018.read()
baby2018.close()

# use regex to extract rank, year, gender and name
rankedNames = re.findall(r'<td>(\d*)</td> <td>(\w*)</td> <td>(\w*)</td>', baby2018Content)

# convert tuples tp dictionary
rankedBoysDict = {}
for rankedName in rankedNames:
    rankedBoysDict[rankedName[0]] = rankedName[1]

rankedGirlsDict = {}
for rankedName in rankedNames:
    rankedGirlsDict[rankedName[0]] = rankedName[2]

def prettyPrint(text):
    print("{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in text.items()) + "}")

prettyPrint(rankedBoysDict)
prettyPrint(rankedGirlsDict)

# sort by name
print(sorted(rankedBoysDict.items(), key=lambda x: x[1]))
print(sorted(rankedGirlsDict.items(), key=lambda x: x[1]))