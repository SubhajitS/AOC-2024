def read_input() -> list[list]:
    file=open("./input.txt")
    mat=[]
    for line in file.readlines():
        mat.append([int(n) for n in list(line.rstrip("\n"))])
    return mat

def main():
    mat = read_input()
    heads = find_trail_heads(mat)
    all_paths = []
    for head in heads:
        find_trails_recursively(mat, head, [head], all_paths)
    print("Total score for part 1 is {}".format(unique_score(all_paths)))
    print("Total ratings for part 2 is {}".format(len(all_paths)))

def unique_score(all_paths: list[list]) -> int:
    d={}
    for path in all_paths:
        sx,sy=path[0]
        dx,dy=path[-1]
        if (sx,sy,dx,dy) not in d:
            d[(sx,sy,dx,dy)] = 1
    return len(d)

def find_trail_heads(mat: list[list]) -> list:
    trailheads = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                trailheads.append((i,j))
    return trailheads

def find_trails_recursively(mat: list[list], start: tuple[int, int], current_path: list, all_paths: list[list]):
    (x,y)=start
    if mat[x][y] == 9:
        all_paths.append(current_path[:])
        return
    moves = [(0,1), (0, -1), (1,0), (-1,0)]
    for (dx, dy) in moves:
        nx, ny = x+dx, y+dy
        if is_validmove(mat, nx, ny, mat[x][y]):
            current_path.append((nx, ny))
            find_trails_recursively(mat, (nx, ny), current_path, all_paths)
            current_path.pop()

def is_validmove(mat:list[list], x: int, y: int, prev: int) ->bool:
    return 0<= x< len(mat) and 0<=y<len(mat[0]) and prev+1==mat[x][y]

if __name__ == "__main__":
    main()