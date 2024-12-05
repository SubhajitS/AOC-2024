orders={}
updates=[]

def readinput():
    inputfile = open("./input.txt", "r")
    ordersFinished = False
    for row in inputfile.readlines():
        if row == "\n":
            ordersFinished = True
            continue
        if ordersFinished:
            updates.append([int(num) for num in row.rstrip("\n").split(",")])
        else:
            order = row.rstrip("\n").split('|')
            key = int(order[0])
            value = int(order[1])
            if key in orders:
                newvalue = list(orders[key])
                newvalue.append(value)
                orders[key] = newvalue
            else:
                orders[key] = [value]

def isvalid(update: list) -> bool:
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] in orders:
                if update[i] in orders[update[j]]:
                    return False
    return True

def correctorder(update):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] in orders:
                if update[i] in orders[update[j]]:
                    temp=update[i]
                    update[i]=update[j]
                    update[j]=temp

if __name__ == "__main__":
    readinput()
    sum = 0
    for update in updates:
        if not isvalid(update):
            correctorder(update)
            print(update)
            sum += update[int(len(update)/2)]
    print(sum)