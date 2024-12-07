import itertools


def readinput() -> list[tuple[int, list[int]]]:
    file = open("./input.txt", "r")
    tests=[]
    for line in file.readlines():
        parts = line.rstrip("\n").split(":")
        tests.append((int(parts[0]), [int(n) for n in parts[1].lstrip(" ").split(" ", )]))
    return tests

def validatetest(target: int, equations: list[str]) -> bool:
    operators=['+', '*']
    n = len(equations)
    operator_combo = itertools.product(operators, repeat=n-1)

    result = 0
    for op in operator_combo:
        for i in range(n-1):
            if i == 0:
                result = equations[i]*equations[i+1] if op[i] == '*' else equations[i]+equations[i+1]
            else:
                result = result*equations[i+1] if op[i] == '*' else result+equations[i+1]
        if result == target:
            return True
    return False

def validatetestwithconcat(target: int, equations: list[str]) -> bool:
    operators=['+', '*', '||']
    n = len(equations)
    operator_combo = itertools.product(operators, repeat=n-1)

    result = 0
    for op in operator_combo:
        for i in range(n-1):
            if i == 0:
                if op[i] == '*':
                    result = equations[i]*equations[i+1]
                elif op[i] == '+':
                    result = equations[i]+equations[i+1]
                else:
                    result = int(str(equations[i])+str(equations[i+1]))
            else:
                if op[i] == '*':
                    result = result*equations[i+1]
                elif op[i] == '+':
                    result = result+equations[i+1]
                else:
                    result = int(str(result)+str(equations[i+1]))
        if result == target:
            return True
    return False

def part1(tests):
    result = 0
    for (target, equations) in tests:
        result += target if validatetest(target, equations) else 0
    print("Result for part 1 is {0}".format(result))

def part2(tests):
    result = 0
    for (target, equations) in tests:
        result += target if validatetestwithconcat(target, equations) else 0
    print("Result for part 2 is {0}".format(result))

if __name__ =="__main__":
    tests = readinput()
    part1(tests)
    part2(tests)