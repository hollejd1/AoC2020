# AoC++ 2020 Day9
# Jon H

import re

# Import Input
InputStr = ''
FID = open('Day9\inputTest.txt')
InputStr=FID.read()
FID.close()
inputList_str = InputStr.split('\n')
inputList = list(map(lambda x: int(x), inputList_str))

def part1(inputList,i,preamble_size):
    for j in range(preamble_size):
        for k in range(j,preamble_size):
            if inputList[i+j]+inputList[i+k]==inputList[i+preamble_size]:
                return True
    return False


def part2(inputList,goal):
    p2_sum=0
    bounds =[0,1]
    while p2_sum!=goal:
        p2_sum=0
        for i in range(bounds[0],bounds[1]):
            p2_sum += inputList[i]

        if p2_sum==goal:
            return bounds
        elif p2_sum<goal:
            bounds[1]+=1
        elif p2_sum>goal:
            bounds[0]+=1


sum1 = 0
sum2 = 0
preamble_size = 5
for i in range(len(inputList) - preamble_size):
    if not part1(inputList,i,preamble_size):
        sum1 = inputList[i+preamble_size]
        break

p2 = part2(inputList,sum1)
sum2 = max(inputList[p2[0]:p2[1]])+min(inputList[p2[0]:p2[1]])

print(sum1,sum2)
