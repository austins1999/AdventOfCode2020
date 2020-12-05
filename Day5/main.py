
import math

def partOne(file):

    highestID = 0
    for line in file:

        upper = 127
        lower = 0
        i = 0
        # find the row
        while(i < 7):
            if(line[i] == 'F'):
                upper = upper - math.ceil((upper - lower) / 2)
            else:
                lower = lower + math.ceil((upper - lower) / 2)
            i += 1
        
        # NOTE: upper = lower, so it doesn't matter which we use here
        row = lower

        # reset upper and lower variables to find column
        upper = 7
        lower = 0
        while(i < 10):
            if(line[i] == 'L'):
                upper = upper - math.ceil((upper - lower) / 2)
            else:
                lower = lower + math.ceil((upper - lower) / 2)
            i += 1

        col = lower
        currentID = int((row * 8) + col)
        if(currentID > highestID):
            highestID = currentID
        
    return str(highestID)


def partTwo(file):

    seatIDs = []
    for line in file:

        upper = 127
        lower = 0
        i = 0
        while(i < 7):
            if(line[i] == 'F'):
                upper = upper - math.ceil((upper - lower) / 2)
            else:
                lower = lower + math.ceil((upper - lower) / 2)
            i += 1
        
        row = lower

        upper = 7
        lower = 0
        while(i < 10):
            if(line[i] == 'L'):
                upper = upper - math.ceil((upper - lower) / 2)
            else:
                lower = lower + math.ceil((upper - lower) / 2)
            i += 1

        col = lower
        seatIDs.append(int((row * 8) + col))

    seatIDs.sort()
    for i in range(1, len(seatIDs) - 1):
        if((seatIDs[i + 1] - seatIDs[i]) > 1):
            return str(seatIDs[i] + 1)
        
    return "ERROR: Seat not found"


def main():
    file = open("Day5/input.txt", "r")
    print("The highest eat ID is: " + partOne(file))
    file.seek(0)
    print("My seat ID is: " + partTwo(file))
    file.close()


main()