# AoC++ 2020 Day4
# Jon H

# Its bad. Its really bad

Input = ''
FID = open('Day4\input.txt')


for line in FID:
    Input+=line
FID.close()

passportsList = Input.split('\n\n')


valid1=0
for passport in passportsList:
    passport = passport.replace('\n',' ')
    fields = passport.split(' ')
    fldList=''
    for item in fields:
        try:
            [fld,content] = item.split(':')
        except:
            pass
        fldList += ' '+fld
    fldList = fldList.replace('byr','1')
    fldList = fldList.replace('iyr','1')
    fldList = fldList.replace('eyr','1')
    fldList = fldList.replace('hgt','1')
    fldList = fldList.replace('hcl','1')
    fldList = fldList.replace('ecl','1')
    fldList = fldList.replace('pid','1')

    if fldList.count('1')==7:
        valid1+=1

print(valid1)


valid2=0
for passport in passportsList:
    passport = passport.replace('\n',' ')
    fields = passport.split(' ')
    valid=0
    for item in fields:
        try:
            [fld,content] = item.split(':')
        except:
            pass
        #print(fld,content)
        if (fld=='byr') and (1920 <= int(content)) and (2002 >= int(content)):
            valid+=1
            #print('passed byr')
        if (fld=='iyr') and (2010 <= int(content)) and (2020 >= int(content)):
            valid+=1
            #print('passed iyr')
        if (fld=='eyr') and (2020 <= int(content)) and (2030 >= int(content)):
            valid+=1
            #print('passed eyr')
        if (fld=='hgt') and (content[-2:]=='in') and (59 <= int(content[:-2])) and (76 >= int(content[:-2])):
            valid+=1
            #print('passed hgt')
        elif (fld=='hgt') and (content[-2:]=='cm') and (150 <= int(content[:-2])) and (193 >= int(content[:-2])):
            valid+=1
            #print('passed hgt')
        if (fld=='hcl') and (content[0]=='#') and (len(content)==7):
            try:
                int(content[1:], 16)
                valid+=1
                #print('passed hcl')
            except:
                pass
        if (fld=='ecl') and ((content=='amb') or (content=='blu') or (content=='brn') or (content=='gry') or (content=='grn') or (content=='hzl') or (content=='oth')):
            valid+=1
            #print('passed ecl')
        if (fld=='pid') and (len(content)==9):
            try:
                int(content)
                valid+=1
            except:
                pass
    if valid==7:
        valid2+=1
    else:
        pass


print(valid2)
