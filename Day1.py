# AoC++ 2020 Day1
# Jon H

def find2Entry(Report):
    for i in range(len(Report)-1):
        j= i+1
        while (Report[i]+Report[j]<2020):
            j+=1
        if (Report[i]+Report[j]==2020):
            return Report[i]*Report[j]

def find3Entry(Report):
    for i in range(len(Report)-2):
        j = i
        k = j + 1
        while (Report[i]+Report[j]+Report[k]<2020):
            j+=1
            while (Report[i]+Report[j]+Report[k]<2020):
                k+=1
            if (Report[i]+Report[j]+Report[k]==2020):
                return Report[i]*Report[j]*Report[k]
            k=j+1            

FID = open('Day1\input.txt')
Report = []
for line in FID:
    Report.append(int(line))
Report.sort()
print(find2Entry(Report))
print(find3Entry(Report))
