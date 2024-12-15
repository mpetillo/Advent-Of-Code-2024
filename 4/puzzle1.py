directions = [(1,-1), (1,0), (1,1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
letters = ['X', 'M', 'A', 'S']

with open("input.txt", "r") as document:
    lines = [line.strip() for line in document.readlines()]
    total = 0

    def checkXMAS(position: tuple, direction: tuple):
        try:
            for key, letter in enumerate(letters):
                row = position[0] + (direction[0] * key)
                col = position[1] + (direction[1] * key)
                if row < 0 or col < 0 or row > len(lines) or col > len(lines[0]):
                    return False
                elif lines[row][col] != letter:
                    return False
            return True
        except:
            return False
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'X':
                for k in directions:
                    if checkXMAS((i, j), k):
                        total += 1
    print(total)