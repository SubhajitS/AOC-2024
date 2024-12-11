def read_input() -> list[int]:
    return [int(n) for n in open("./input.txt", "r").readline().rstrip("\n").split(" ")]

def blink(list: list[int]) -> list[int]:
    newlist=[]
    for stone in list:
        if stone == 0:
            newlist.append(1)
        elif len(str(stone))%2 == 0:
            stone_str = str(stone)
            left_half, right_half = int(stone_str[:int(len(stone_str)/2)]), int(stone_str[int(len(stone_str)/2):])
            newlist.append(left_half)
            newlist.append(right_half)
        else:
            newlist.append(stone*2024)
    return newlist

def part1(list: list[int], times: int):
    for i in range(times):
        list=blink(list)
    
    print("Number of stone after {} blink is {}".format(times, len(list)))
    

if __name__ == "__main__":
    part1(read_input(), 25)
    