def readinput() -> list:
    inputfile = open("/Users/subhajitsaha/Projects/p2p-demo/aoc/day2/input.txt", "r")
    reports=[]
    for line in inputfile.readlines():
        numbers = line.rstrip('\n').split(" ")
        reports.append([int(numeric_string) for numeric_string in numbers])
    inputfile.close()
    return reports

def isSafe(report: list) -> bool:
    flag = 0
    if report[0] > report[1] and report[0]-report[1] >= 1 and report[0]-report[1] <= 3 :
        flag = -1
    elif report[0] < report [1] and report[1]-report[0] >= 1 and report[1]-report[0] <= 3:
        flag = 1
    else:
        return False

    for i in range(1, len(report)-1):
        if report[i] > report[i+1] and flag == -1 and report[i]-report[i+1] >= 1 and report[i]-report[i+1] <= 3:
            continue
        elif report[i] < report [i+1] and flag == 1 and report[i+1]-report[i] >= 1 and report[i+1]-report[i] <= 3:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    reports = readinput()
    safeCount = 0
    for report in reports:
        if isSafe(report):
            safeCount += 1
    print(safeCount)
