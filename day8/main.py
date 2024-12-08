import itertools


def readinput() -> list[list[str]]:
    file = open('./input.txt', "r")
    mat=[]
    for line in file.readlines():
        mat.append(list(line.rstrip("\n")))
    return mat

def findantennas(mat: list[list[str]]) -> dict[str, list]:
    antennas = {}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]!=".":
                if mat[i][j] in antennas:
                    coordinates = list(antennas[mat[i][j]])
                    coordinates.append((i,j))
                    antennas[mat[i][j]] = coordinates
                else:
                    antennas[mat[i][j]] = [(i,j)]
    return antennas

def findantinodes(antennas: dict[str, list], height, width):
    antinodes = {}
    for frequency in antennas:
        for c in itertools.combinations(antennas[frequency], r=2):
            (x,y) = (c[1][0]-c[0][0], c[1][1]-c[0][1])
            antinode1 = (c[0][0]-x, c[0][1]-y)
            antinode2 = (c[1][0]+x, c[1][1]+y)
            if isvalidantinode(antinode1, height, width):
                antinodes[antinode1] = frequency
            if isvalidantinode(antinode2, height, width):
                antinodes[antinode2] = frequency
    
    print("Part 1: Number of distinct antinode is {0}".format(len(antinodes)))

def findrepeatingantinodes(antennas: dict[str, list], height, width):
    antinodes = {}
    for frequency in antennas:
        for c in itertools.combinations(antennas[frequency], r=2):
            (x,y) = (c[1][0]-c[0][0], c[1][1]-c[0][1])
            antinode1 = (c[0][0]-x, c[0][1]-y)
            while isvalidantinode(antinode1, height, width):
                antinodes[antinode1] = frequency
                antinode1 = (antinode1[0]-x, antinode1[1]-y)
            antinode2 = (c[1][0]+x, c[1][1]+y)
            while isvalidantinode(antinode2, height, width):
                antinodes[antinode2] = frequency
                antinode2 = (antinode2[0]+x, antinode2[1]+y)
                
    for (x,y) in sum([antennas[a] for a in antennas if len(antennas[a])>1],[]):
        if (x,y) not in antinodes:
            antinodes[(x,y)]=''
            
    print("Part 2: Number of distinct repeated antinode is {0}".format(len(antinodes)))


def isvalidantinode(node: tuple[int, int], height, width) -> bool:
    if node[0]<0 or node[0]>=height:
        return False
    if node[1]<0 or node[1]>= width:
        return False
    return True

if __name__ == "__main__":
    mat = readinput()
    height = len(mat)
    width = len(mat[0])
    antennas = findantennas(mat)
    findantinodes(antennas, height, width)
    findrepeatingantinodes(antennas, height, width)