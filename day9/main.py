def readinput() -> list[str]:
    file=open("./input.txt", "r")
    return list(file.readline())

def part1(input: readinput):
    raw = input()
    expanded=[]
    for i in range(len(raw)):
        j=int(raw[i])
        if i%2!=0:
            #Empty block
            while j>0:
                expanded.append(".")
                j-=1
        else:
            #File block
            while j>0:
                expanded.append(str(int(i/2)))
                j-=1
    compact(expanded)
    print("Checksum for part 1 is {}".format(calculate_checksum(expanded)))

def compact(expanded: list):
    i=0
    j = len(expanded)-1
    while i<j:
        if(expanded[i])!=".":
            i+=1
            continue
        while expanded[j]== ".":
            j-=1
        expanded[i]=expanded[j]
        expanded[j]="."
        i+=1
        j-=1

def calculate_checksum(compact: list) -> int:
    sum=0
    for i in range(len(compact)):
        sum+=(int(compact[i]) if compact[i]!="." else 0)*i
    return sum

if __name__ == "__main__":
    part1(readinput)