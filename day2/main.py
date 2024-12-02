def readinput() -> list:
    inputfile = open("/Users/subhajitsaha/Projects/p2p-demo/aoc/day2/input.txt", "r")
    reports=[]
    for line in inputfile.readlines():
        numbers = line.rstrip('\n').split(" ")
        reports.append([int(numeric_string) for numeric_string in numbers])
    inputfile.close()
    return reports

def isSafe(report: list) -> bool:
    sum = 0
    for i in range(len(report)-1):
        if report[i] - report[i+1] >=1 and report[i] - report[i+1] <=3:
            sum -= 1
        elif report[i+1] - report[i] >=1 and report[i+1] - report[i] <=3:
            sum += 1
        else:
            continue
    return abs(sum) == len(report) -1

if __name__ == "__main__":
    reports = readinput()
    safeCount = 0
    for report in reports:
        if isSafe(report):
            safeCount += 1
    print(safeCount)
