
def partOne():

    valid = 0
    file = open("Day2/input.txt", "r")
    for line in file:
        lineList = line.split(" ")
        range = lineList[0].split("-")
        target = lineList[1][0]
        targetCount = 0

        for char in lineList[2]:
            if char == target:
                targetCount+=1

        if targetCount >= int(range[0]) and targetCount <= int(range[1]):
            valid += 1

    file.close()
    print(valid)


def partTwo():

    valid = 0
    file = open("Day2/input.txt", "r")
    for line in file:
        lineList = line.split(" ")
        indices = lineList[0].split("-")
        target = lineList[1][0]

        if (lineList[2][int(indices[0])-1] == target and lineList[2][int(indices[1])-1] != target) or (lineList[2][int(indices[1])-1] == target and lineList[2][int(indices[0])-1] != target):
            valid += 1

    file.close()
    print(valid)


partOne()
partTwo()

