# AoC++ 2020 Day6
# Jon H

import re

InputStr = ''
FID = open('Day6\input.txt')

# Import Input
for line in FID:
    InputStr+=line
FID.close()
inputList = InputStr.split('\n\n')

sum1 = 0
sum2 = 0
for item in inputList:
    charlist = item.replace('\n','')
    charlist="".join(set(charlist))
    sum1+=len(charlist)

    personList = item.split('\n')

    numQs = 0
    for char in charlist:
        valid = True
        for person in personList:
            if char not in person:
                valid = False
        if valid==True:
            numQs+=1
    sum2+=numQs

print(sum1,sum2)
