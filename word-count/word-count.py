import re

def countWords(filename):
  book = open(filename, 'r')
  bookStr = book.read()
  bookStrReg = re.sub('\W+\^d', '', bookStr)
  bookStrRegList = bookStrReg.split()
  return len(bookStrRegList)

print(countWords('alice-in-wonderland.txt'))

def countFrequencyWords(filename):
  book = open(filename, 'r')
  bookStr = book.read()
  bookStrReg = re.sub('\W+\^d', '', bookStr)
  bookStrRegList = bookStrReg.split()
  bookStrRegDict = {}
  for word in bookStrRegList:
    if word not in bookStrRegDict.keys():
      bookStrRegDict[word] = 1
    else:
      bookStrRegDict[word] += 1
  return sorted(bookStrRegDict.items(), key=lambda x: x[1])

print(countFrequencyWords('alice-in-wonderland.txt'))