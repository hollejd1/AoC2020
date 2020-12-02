# AoC++ 2020 Day2
# Jon H


def validate1(low, high, key, password):
    i=0
    while (len(password)>1):
        if password[0]==key:
            i+=1
        password=password[1:]
    if password[0]==key:
            i+=1
    if (i>=low) and (i<=high):
        return 1
    return 0


def validate2(low, high, key, password):
    if (password[low-1]==key) ^ (password[high-1]==key):
        return 1
    return 0
    

valid1 = 0
valid2 = 0
FID = open('Day2\input.txt')
for line in FID:
    rng, key, password = line.split(' ')
    low, high = rng.split('-')
    low = int(low)
    high = int(high)
    key = key[0:-1]

    valid1 += validate1(low, high, key, password)
    valid2 += validate2(low, high, key, password)
FID.close()
print(valid1,valid2)
