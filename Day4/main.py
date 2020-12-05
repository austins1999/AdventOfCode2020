
def partOne():
    file = open("Day4/input.txt", "r")
    validCount = 0
    currPassport = ""
    for line in file:
        if (len(line) == 1):
            if("byr:" in currPassport and "iyr:" in currPassport and 
                "eyr:" in currPassport and "hgt:" in currPassport and "hcl:" in currPassport
                and "ecl:" in currPassport and "pid:" in currPassport):
                validCount += 1
            currPassport = ""

        else:
            currPassport += line

    if("byr:" in currPassport and "iyr:" in currPassport and 
        "eyr:" in currPassport and "hgt:" in currPassport and "hcl:" in currPassport
        and "ecl:" in currPassport and "pid:" in currPassport):
        validCount += 1

    print(str(validCount) + " valid passports detected.")


# ABANDON ALL HOPE, YE WHO ENTER HERE
def partTwo():
    file = open("Day4/input.txt", "r")
    validCount = 0
    validFields = [False, False, False, False, False, False, False]
    currPassport = ""

    for line in file:

        if (len(line) == 1):
            index = currPassport.find("byr:")
            if(index != -1):
                byr = int(currPassport[(index+4):(index+8)])
                validFields[0] = (byr >= 1920 and byr <= 2002)
            
            index = currPassport.find("iyr:")
            if(index != -1):
                iyr = int(currPassport[(index+4):(index+8)])
                validFields[1] = (iyr >= 2010 and iyr <= 2020)

            index = currPassport.find("eyr:")
            if(index != -1):
                eyr = int(currPassport[(index+4):(index+8)])
                validFields[2] = (eyr >= 2020 and eyr <= 2030)

            index = currPassport.find("hgt:")
            if(index != -1):
                endIndex = currPassport.find("c", index)
                if(endIndex != -1 and (endIndex - index) < 8):
                    hgt = currPassport[(index+4):endIndex]
                    hgt = int(hgt)
                    validFields[3] = (hgt >= 150 and hgt <= 193)
                else:
                    endIndex = currPassport.find("i", index)
                    if(endIndex != -1 and (endIndex - index) < 8):
                        hgt = currPassport[(index+4):endIndex]
                        hgt = int(hgt)
                        validFields[3] = (hgt >= 59 and hgt <= 76)

            index = currPassport.find("hcl:")
            if(index != -1):
                if(currPassport[(index+4)] == '#'):
                    lookinGood = True
                    i = (index + 5)
                    while (i < (index+11) and lookinGood):
                        if (currPassport[i] != '0' and
                            currPassport[i] != '1' and
                            currPassport[i] != '2' and
                            currPassport[i] != '3' and
                            currPassport[i] != '4' and
                            currPassport[i] != '5' and
                            currPassport[i] != '6' and
                            currPassport[i] != '7' and
                            currPassport[i] != '8' and
                            currPassport[i] != '9' and
                            currPassport[i] != 'a' and
                            currPassport[i] != 'b' and
                            currPassport[i] != 'c' and
                            currPassport[i] != 'd' and
                            currPassport[i] != 'e' and
                            currPassport[i] != 'f'):
                            lookinGood = False
                        i += 1
                    validFields[4] = ((currPassport[(index+11)] == " " or currPassport[(index+11)] == "\n") and lookinGood)

            index = currPassport.find("ecl:")
            if(index != -1):
                ecl = currPassport[(index+4):(index+7)]
                validFields[5] = (ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth")
            
            index = currPassport.find("pid:")
            if(index != -1):
                endIndex = currPassport.find(" ", index)
                if ((endIndex-index) > 16):
                    endIndex = currPassport.find("\n", index)
                pid = currPassport[(index+4):endIndex]
                try:
                    pid = int(pid)
                    pid = str(pid)
                    validFields[6] = (len(pid) == 9)
                except:
                    pass
            
            if(validFields[0] and validFields[1] and validFields[2] and validFields[3]
                and validFields[4] and validFields[5] and validFields[6]):
                validCount += 1
            currPassport = ""
            validFields = [False, False, False, False, False, False, False]

        else:
            currPassport += line

    print(str(validCount) + " valid passports detected.")


partOne()
partTwo()