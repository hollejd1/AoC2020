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
    item=item.replace('F','0')
    item=item.replace('L','0')
    item=item.replace('R','1')
    item=item.replace('B','1')
    SeatIDs.append(int(item,2))

# Sort list, find gap in IDs
SeatIDs.sort()
for i in range(len(SeatIDs)-1):
    if (SeatIDs[i+1] - SeatIDs[i])==2:
        mySeat=SeatIDs[i]+1
        break

print(SeatIDs[-1],mySeat)
