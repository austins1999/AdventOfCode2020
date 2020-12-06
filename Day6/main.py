
def main():
    file = open("Day6/input.txt", "r")
    print("Sum of individual 'yes' answers: " + str(partOne(file)))
    file.seek(0)
    print("Sum of group 'yes' answers: " + str(partTwo(file)))
    file.close()


def partOne(file):
    stringFile = file.read()
    groups = stringFile.split("\n\n")
    sum = 0
    for group in groups:
        group = group.replace("\n", "")
        for i in range(26):
            if chr(i+97) in group:
                sum += 1
     
    return sum


def partTwo(file):
    stringFile = file.read()
    groups = stringFile.split("\n\n")
    sum = 0
    for group in groups:
        members = group.split("\n")
        answers = members[0]
        if '' in members:
            members = members[:(len(members)-1)]
        for i in range(1, len(members)):
            for char in answers:
                if char not in members[i]:
                    answers = answers.replace(char, "")
        sum += len(answers)

    return(sum)


main()