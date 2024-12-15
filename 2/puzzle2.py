def checkvalidity(level):
    if len(level) < 2:
        return False
    good = True
    comp = [-1, -2, -3] if level[0] - level[1] < 0 else [1, 2, 3]
    for i in range(len(level)-1):
        if level[i] - level[i+1] not in comp:
            good=False
            break
    return good

with open("input.txt", "r") as document:
    safe = 0
    line = document.readline()
    while line:
        level = [int(i) for i in line.split()]
        if not checkvalidity(level):
            for i in range(len(level)):
                copy = level.copy()
                copy.pop(i)
                if checkvalidity(copy):
                    safe += 1
                    break
        else:
            safe += 1
        line = document.readline()
    print(safe)