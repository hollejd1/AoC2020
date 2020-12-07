# AoC++ 2020 Day7
# Jon H

import re

InputStr = ''
FID = open('Day7\input.txt')

# Import Input
for line in FID:
    InputStr+=line
FID.close()
inputList = InputStr.split('\n')

sum1 = 0
sum2 = 0
ruleList = []
for item in inputList:
    item = item.split(' bags contain ')
    if item[1][0]=='n':
        pass
    else:
        rule = []
        rule.append(item[0])
        item[1] = re.sub('bags?\.?','',item[1])
        item = item[1].split(', ')
        
        for subRule in item:
            rule.append(subRule[0])
            rule.append(subRule[2:-1])
        ruleList.append(rule)
        



def part1(ruleList,currentBag,goalBag):
    for rule in ruleList:
        if currentBag==rule[0]:
            for i in range(len(rule[1:])//2):
                if goalBag==rule[(i+1)*2]:
                    return True
                else:
                    if part1(ruleList,rule[(i+1)*2],goalBag):
                        return True
            return False


def part2(ruleList,currentBag):
    for rule in ruleList:
        if currentBag==rule[0]:
            bagsInside = 1
            for i in range(len(rule[1:])//2):
                bagsInside += int(rule[(i+1)*2-1])*part2(ruleList,rule[(i+1)*2])
            return bagsInside

    return 1



goalBag = 'shiny gold'
for startRule in ruleList:
    if part1(ruleList,startRule[0],goalBag):
        sum1+=1

sum2 = part2(ruleList,goalBag)-1

print(sum1,sum2)
