def main():
    file = open("Day7/input.txt", "r")
    data = processFile(file)
    file.close()

    print("Number of potential shiny gold containers: " + str(goldSearch(data, 0, 0, 0)))
    #print("Sum of group 'yes' answers: " + str(partTwo(file)))


def processFile(file):
    stringFile = file.read()
    lines = stringFile.split("\n")
    data = []
    sum = 0
    for i in range(len(lines) - 1):
        splitLine = lines[i].split(",")
        endIndex = splitLine[0].index("bag") - 1
        bagType = splitLine[0][:endIndex]
        data.append([bagType])

        for j in range(1, len(splitLine)):
            endIndex = splitLine[j].index("bag") - 1
            startIndex = 3
            bagType = splitLine[j][startIndex:endIndex]
            data[i].append(bagType)

    return data


def goldSearch(data, i, j, sum):
    if data[i][j] == "shiny gold":
        return 1
    elif j < (len(data[i]) - 1):
        sum += goldSearch(data, i, (j + 1), sum)
    elif i < (len(data) - 1):
        sum += goldSearch(data, (i + 1), 0, sum)
    return sum

    


main()