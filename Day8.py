# AoC++ 2020 Day8
# Jon H

import re

InputStr = ''
FID = open('Day8\input.txt')

# Import Input
for line in FID:
    InputStr+=line
FID.close()
inputList = InputStr.split('\n')


def runInstructions(inputList):

    i=0
    accum=0
    
    visited_i = []
    while True:
        
        if i==len(inputList):
            return accum

        if i in visited_i:
            return -1*accum

        if 'nop' in inputList[i]:
            visited_i.append(i)
            i+=1

        elif 'acc' in inputList[i]:
            accum+=int(inputList[i][4:])
            visited_i.append(i)
            i+=1

        elif 'jmp' in inputList[i]:
            visited_i.append(i)
            i+=int(inputList[i][4:])


accum1 = -1*runInstructions(inputList)
for j in range(len(inputList)):
    if 'jmp' in inputList[j]:
        inputList[j]='nop '+inputList[j][4:]
    elif 'nop' in inputList[j]:
        inputList[j]='jmp '+inputList[j][4:]

    accum2 = runInstructions(inputList)
    if accum2 > 0:
        break

    if 'jmp' in inputList[j]:
        inputList[j]='nop '+inputList[j][4:]
    elif 'nop' in inputList[j]:
        inputList[j]='jmp '+inputList[j][4:]

print(accum1,accum2)
