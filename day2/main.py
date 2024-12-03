def readinput() -> list:
    inputfile = open("./input.txt", "r")
    reports=[]
    for line in inputfile.readlines():
        numbers = line.rstrip('\n').split(" ")
        reports.append([int(numeric_string) for numeric_string in numbers])
    inputfile.close()
    return reports

def isSafe(report: list) -> bool:
    return (all(report[i] - report[i + 1] >0 and report[i] - report[i + 1] <4 for i in range(len(report) - 1)) or
        all(report[i+1] - report[i] >0 and report[i+1] - report[i] <4 for i in range(len(report) - 1)))

def isSafeWithTolerance(report: list) -> bool:
    if isSafe(report):
        return True
    for i in range(len(report)):
        new_report = report[:i] + report[i+1:]
        
        if isSafe(new_report):
            return True
    return False

if __name__ == "__main__":
    reports = readinput()
    safeCount = 0
    for report in reports:
        if isSafeWithTolerance(report):
            safeCount += 1
    print(safeCount)
