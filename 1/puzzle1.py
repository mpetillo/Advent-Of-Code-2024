with open("puzzle1.txt", "r") as document:
    left = []
    right = []
    line = document.readline().split()
    while line:
        left.append(int(line[0]))
        right.append(int(line[1]))
        line = document.readline().split()
    left.sort()
    right.sort()
    distance = 0
    for leftnum, rightnum in zip(left, right):
        distance += abs(leftnum - rightnum)
    print(distance)