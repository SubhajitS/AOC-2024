import re


def readinput() -> list:
    inputfile = open("./input.txt", "r")
    instructions=inputfile.readlines()
    inputfile.close()
    return instructions

def calculate(instruction: str) -> int:
    pattern = re.compile(r'mul\(\d+,\d+\)',flags=re.MULTILINE)
    sum=0
    for match in pattern.findall(instruction):
        nums=match.replace("mul(", "").replace(")", "").split(",")
        sum+=int(nums[0])*int(nums[1])
    return sum

if __name__ == "__main__":
    result=0
    for instruction in readinput():
        result += calculate(instruction)
    print(result)
    