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

def part2(input: readinput):
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
    compact_as_whole(expanded)
    print("Checksum for part 2 is {}".format(calculate_checksum(expanded)))

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

def compact_as_whole(expanded: list):
    i = len(expanded)-1
    while i>0:
        j=0
        while expanded[i]== ".":
            i-=1
        id=expanded[i]
        file_size = 0
        while expanded[i]==id:
            file_size+=1
            i-=1
        available_size=0
        while j<=i:
            available_size=0
            while j<=i and expanded[j]!=".":
                j+=1
            while j<=i and expanded[j]==".":
                j+=1
                available_size+=1
            if available_size>=file_size:
                while file_size>0:
                    expanded[j-available_size]=id
                    expanded[i+file_size]="."
                    j+=1
                    file_size-=1


def calculate_checksum(compact: list) -> int:
    sum=0
    for i in range(len(compact)):
        sum+=(int(compact[i]) if compact[i]!="." else 0)*i
    return sum

if __name__ == "__main__":
    #part1(readinput)
    part2(readinput)