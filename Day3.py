# AoC++ 2020 Day3
# Jon H

SlopeMat = []
FID = open('Day3\input.txt')
for line in FID:
    SlopeMat.append(line)
FID.close()

width = len(SlopeMat[0])-1
height = len(SlopeMat)

slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

treesList = []

for slope in slopes:
    trees = 0
    x=0
    y=0
    while (y<height):
        if SlopeMat[y][x]=='#':
            trees+=1
        x+=slope[0]
        y+=slope[1]
        if x>= width:
            x-=width
    treesList.append(trees)

treeMult = 1
for item in treesList:
    treeMult *= item
print(treesList,treeMult)
