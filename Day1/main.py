
def main():
    data = []
    file = open("Day1/input.txt", "r")
    for line in file:
        data.append(int(line))
    file.close()

    print(twoNumbers(data))
    print(threeNumbers(data))

def twoNumbers(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if i != j:
                if data[i] + data[j] == 2020:
                    return (data[i] * data[j])

    return -1

def threeNumbers(data):
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if i != j and j != k and i != k:
                    if data[i] + data[j] +data[k] == 2020:
                        return (data[i] * data[j] * data[k])

    return -1

main()