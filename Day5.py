# AoC++ 2020 Day5
# Jon H


InputStr = ''
FID = open('Day5\input.txt')

# Import Input
for line in FID:
    InputStr+=line
FID.close()
inputList = InputStr.split('\n')

# Find Seat ID of Pass
SeatIDs = []
for item in inputList:
    # Find row via BST
    rowBounds = [0,128]
    for char in item[:7]:
        if (char=='F'):
            rowBounds = [rowBounds[0],(rowBounds[0]+rowBounds[1])/2]
        else:
            rowBounds = [(rowBounds[0]+rowBounds[1])/2,rowBounds[1]]
    
    # Find column via BST
    colBounds = [0,8]
    for char in item[7:]:
        if (char=='L'):
            colBounds = [colBounds[0],(colBounds[0]+colBounds[1])/2]
        else:
            colBounds = [(colBounds[0]+colBounds[1])/2,colBounds[1]]
    
    # Calculate ID
    SeatIDs.append(rowBounds[0]*8+colBounds[0])

# Sort list, find gap in IDs
SeatIDs.sort()
for i in range(len(SeatIDs)-1):
    if (SeatIDs[i+1] - SeatIDs[i])==2:
        mySeat=SeatIDs[i]+1
        print(SeatIDs[i]+1)
        break

print(SeatIDs[-1],mySeat)
