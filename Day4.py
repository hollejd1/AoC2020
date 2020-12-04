# AoC++ 2020 Day4
# Jon H

# Better, not great

InputStr = ''
FID = open('Day4\input.txt')


for line in FID:
    InputStr+=line
FID.close()

InputStr = InputStr.split('\n\n')

passportsList = []
for item in InputStr:
    passport = []
    item = item.replace('\n',' ')
    fields = item.split(' ')
    for field in fields:
        try:
            passport.append(field.split(':'))
        except:
            pass
    passportsList.append(passport)

ans1=0
ans2=0

for passport in passportsList:
    valid1=0
    valid2=0
    for fld in passport:
        if (fld[0]=='byr'):
            valid1+=1
            if (1920 <= int(fld[1])) and (2002 >= int(fld[1])):
                valid2+=1
        elif (fld[0]=='iyr'):
            valid1+=1
            if (2010 <= int(fld[1])) and (2020 >= int(fld[1])):
                valid2+=1
        elif (fld[0]=='eyr'):
            valid1+=1
            if (2020 <= int(fld[1])) and (2030 >= int(fld[1])):
                valid2+=1
        elif (fld[0]=='hgt'):
            valid1+=1
            if (fld[1][-2:]=='in') and (59 <= int(fld[1][:-2])) and (76 >= int(fld[1][:-2])):
                valid2+=1
            elif (fld[1][-2:]=='cm') and (150 <= int(fld[1][:-2])) and (193 >= int(fld[1][:-2])):
                valid2+=1
        elif (fld[0]=='hcl'):
            valid1+=1
            if (fld[1][0]=='#') and (len(fld[1])==7):
                try:
                    int(fld[1][1:], 16)
                    valid2+=1
                except:
                    pass
        elif (fld[0]=='ecl'):
            valid1+=1
            if ((fld[1]=='amb') or (fld[1]=='blu') or (fld[1]=='brn') or (fld[1]=='gry') or (fld[1]=='grn') or (fld[1]=='hzl') or (fld[1]=='oth')):
                valid2+=1
        elif (fld[0]=='pid'):
            valid1+=1
            if (len(fld[1])==9):
                try:
                    int(fld[1])
                    valid2+=1
                except:
                    pass
    
    if valid1==7:
        ans1+=1
    if valid2==7:
        ans2+=1

print(ans1,ans2)
