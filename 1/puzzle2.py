with open("input.txt", "r") as document:
    left = []
    right = []
    line = document.readline().split()
    while line:
        left.append(int(line[0]))
        right.append(int(line[1]))
        line = document.readline().split()
    simularity = 0
    for leftnum, rightnum in zip(left, right):
        print(right.count(rightnum))
        simularity += leftnum * right.count(leftnum)
    print(simularity)