from enum import Enum

Direction = Enum('Direction', [('UP', 1), ('RIGHT', 2), ('DOWN', 3), ('LEFT', 4), ('STOP', 5)])

def readinput() -> list:
    file = open("./input.txt", "r")
    mat=[]
    for line in file.readlines():
        mat.append(list(line.rstrip("\n")))
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

def part1(mat:list, direction: Direction, current: tuple[int, int], path: dict):
    trackpath(mat, direction, (x,y), path)
    print("Solution for part 1 is {}".format(len(path)))

def part2(mat:list, direction: Direction, current: tuple[int, int]):
    (x,y)=current
    possible_scenarios = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (x,y)==(i,j) or (x-1,y)==(i,j) or mat[i][j] == "#":
                continue
            path={}
            mat[i][j]="#"
            possible_scenarios += 1 if checkcircularpath(mat, direction, current, path) else 0
            mat[i][j]="."
    print("Solution to 2nd part {}".format(possible_scenarios))

def checkcircularpath(mat:list, direction: Direction, current: tuple[int, int], path: dict) -> bool:
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
            elif path[(x,y)] == direction:
                return True
            #continue forward
            if direction == Direction.UP:
                x-=1
            elif direction == Direction.RIGHT:
                y+=1
            elif direction == Direction.DOWN:
                x+=1
            elif direction == Direction.LEFT:
                y-=1
    return False

if __name__ == "__main__":
    path={}
    mat = readinput()
    (x,y) = findstart(mat)
    direction=Direction.UP
    part1(mat, direction, (x,y), path)
    part2(mat, direction, (x,y))


