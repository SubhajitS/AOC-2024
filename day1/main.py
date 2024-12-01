def readinput() -> tuple[list, list]:
    inputfile = open("input.txt", "r")
    left=[]
    right=[]
    for line in inputfile.readlines():
        numbers = line.rstrip('\n').split("   ")
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
    inputfile.close()
    return (left, right)

def calculateDistance() -> int:
    (left, right) = readinput()
    left.sort()
    right.sort()

    distance=0
    for i in range(len(left)):
        distance += abs(right[i]-left[i])
    return distance

def calculateSimilarity() -> int:
    (left, right) = readinput()
    similarity = 0
    for l in left:
        similarity+= l*right.count(l)
    return similarity

if __name__ == "__main__":
    print(calculateDistance())
    print(calculateSimilarity())