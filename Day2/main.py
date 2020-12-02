
def partOne():

    validPasswords = []

    file = open("Day2/input.txt", "r")
    for line in file:
        lineList = line.split(" ")

        # further splits the first item such that range[0] is the
        #   minimum and range[1] is the maximum amount of the target
        #   character required for the password to be valid
        range = lineList[0].split("-")

        # isolates the target character from the list;
        #   the [0] is necessary to remove the colon
        target = lineList[1][0]

        # counter and loop used to track the number of occurances of the target
        targetCount = 0
        for char in lineList[2]:
            if char == target:
                targetCount+=1

        # checks to see if the password is valid and adds it to the list
        if targetCount >= int(range[0]) and targetCount <= int(range[1]):
            validPasswords.append(lineList[2])

    file.close()
    print(len(validPasswords))


def partTwo():

    validPasswords = []
    file = open("Day2/input.txt", "r")
    for line in file:

        lineList = line.split(" ")
        # further splits the first item such that range[0] is the
        #   first and range[1] is the second index to check for the target
        indices = lineList[0].split("-")
        target = lineList[1][0]
        # checks the specified indices to to see if the target is present
        if (lineList[2][int(indices[0])-1] == target and lineList[2][int(indices[1])-1] != target) or (lineList[2][int(indices[1])-1] == target and lineList[2][int(indices[0])-1] != target):
            validPasswords.append(lineList[2])

    file.close()
    print(len(validPasswords))



partOne()
partTwo()