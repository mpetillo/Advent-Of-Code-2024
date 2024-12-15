with open("input.txt", "r") as document:
    lines = [line.strip("\n") for line in document.readlines()]
    total = 0


    def checkXMAS(position: tuple):
        letters = [lines[position[0] + 1][position[1] + 1], lines[position[0] - 1][position[1] + 1], lines[position[0] + 1][position[1] - 1], lines[position[0] - 1][position[1] - 1]]
        if letters.count('M') == 2 and letters.count('S') == 2:
            if lines[position[0] + 1][position[1] + 1] == lines[position[0] - 1][position[1] - 1]:
                return False
            else:
                return True
        else:
            return False
    
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            if lines[i][j] == 'A':
                if checkXMAS((i,j)):
                    total+=1
    print(total)