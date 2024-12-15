with open("input.txt", "r") as document:
    safe = 0
    line = document.readline()
    while line:
        level = [int(i) for i in line.split()]
        good = True
        comp = [-1, -2, -3] if level[0] - level[1] < 0 else [1, 2, 3]
        for i in range(len(level)-1):
            if level[i] - level[i+1] not in comp:
                good=False
                break
        if good:
            safe += 1       
        line = document.readline()
    print(safe)         

