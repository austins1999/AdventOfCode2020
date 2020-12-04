
def main():
    map = []
    file = open("Day3/input.txt", "r")
    for line in file:
        currLine = []
        line = line.strip("\n")
        for char in line:
            currLine.append(char)
        map.append(currLine)

    file.close()
    one = checkSlope(map, 1, 1)
    two = checkSlope(map, 1, 3)
    three = checkSlope(map, 1, 5)
    four = checkSlope(map, 1, 7)
    five = checkSlope(map, 2, 1)
    product = one * two * three * four * five
    print(one,"*",two,"*",three,"*",four,"*",five,"=",product)


def checkSlope(map, rise, run):
    treeCount = 0
    row = 0
    col = 0
    while row < len(map):
        if(map[row][col] == '#'):
            treeCount += 1
        row += rise
        col = (col + run) % len(map[0])
    
    return(treeCount)


main()