from enum import Enum

Direction = Enum('Direction', [('UP', 1), ('RIGHT', 2), ('DOWN', 3), ('LEFT', 4), ('STOP', 5)])

def readinput() -> list:
    file = open("./input.txt", "r")
    mat=[]
    for line in file.readlines():
        mat.append(list(line))
    return mat

def findstart(mat: list)-> tuple[int, int]:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "^":
                return (i,j)
    return (-1, -1)

def trackpath(mat:list, direction: Direction, current: tuple[int, int], path: dict):
    (x,y)=current

    while x>=0 and x<len(mat) and y>=0 and y<len(mat[0]):
        if mat[x][y] == "#":
            #Take right turn
            if direction == Direction.UP:
                x+=1
                y+=1
                direction = Direction.RIGHT
            elif direction == Direction.RIGHT:
                x+=1
                y-=1
                direction = Direction.DOWN
            elif direction == Direction.DOWN:
                x-=1
                y-=1
                direction = Direction.LEFT
            elif direction == Direction.LEFT:
                x-=1
                y+=1
                direction = Direction.UP
        else:
            if (x,y) not in path:
                path[(x,y)]=direction
            #continue forward
            if direction == Direction.UP:
                x-=1
            elif direction == Direction.RIGHT:
                y+=1
            elif direction == Direction.DOWN:
                x+=1
            elif direction == Direction.LEFT:
                y-=1

if __name__ == "__main__":
    path={}
    mat = readinput()
    (x,y) = findstart(mat)
    direction=Direction.UP
    trackpath(mat, direction, (x,y), path)
    print(len(path))

