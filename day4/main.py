mat=[]
validwords=['XMAS', 'SAMX']
def readinput():
    file = open("./input.txt", "r")
    for line in file.readlines():
        mat.append(list(line.rstrip("\n")))

def checkhorizontal(i: int, j: int, width: int, validIndexes: list) -> int:
    if j+3 < width:
        segment="".join(mat[i][slice(j, j+4)])
        if segment in validwords:
            validIndexes.append(str(i)+","+str(j))
            validIndexes.append(str(i)+","+str(j+1))
            validIndexes.append(str(i)+","+str(j+2))
            validIndexes.append(str(i)+","+str(j+3))
            return 1
    return 0
    

def checkvertical(i: int, j: int, height: int, validIndexes: list) -> int:
    if i+3<height:
        segment=mat[i][j]+mat[i+1][j]+mat[i+2][j]+mat[i+3][j]
        if segment in validwords:
            validIndexes.append(str(i)+","+str(j))
            validIndexes.append(str(i+1)+","+str(j))
            validIndexes.append(str(i+2)+","+str(j))
            validIndexes.append(str(i+3)+","+str(j))
            return 1
    return 0

def checkdiagonal(i: int, j: int, height: int, width: int, validIndexes: list) -> int:
    count = 0
    if i+3<height:
        if j-3>=0:
            segment=mat[i][j]+mat[i+1][j-1]+mat[i+2][j-2]+mat[i+3][j-3]
            if segment in validwords:
                validIndexes.append(str(i)+","+str(j))
                validIndexes.append(str(i+1)+","+str(j-1))
                validIndexes.append(str(i+2)+","+str(j-2))
                validIndexes.append(str(i+3)+","+str(j-3))
                count += 1
        if j+3<width:
            segment=mat[i][j]+mat[i+1][j+1]+mat[i+2][j+2]+mat[i+3][j+3]
            if segment in validwords:
                validIndexes.append(str(i)+","+str(j))
                validIndexes.append(str(i+1)+","+str(j+1))
                validIndexes.append(str(i+2)+","+str(j+2))
                validIndexes.append(str(i+3)+","+str(j+3))
                count += 1
    return count

if __name__ == "__main__":
    readinput()
    height=len(mat)
    width=len(mat[0])
    count = 0
    validIndexes = []
    for i in range(height):
        for j in range(width):
            count += checkhorizontal(i, j, width, validIndexes)
            count += checkvertical(i, j, height, validIndexes)
            count += checkdiagonal(i, j, height, width, validIndexes)
    print(count)
