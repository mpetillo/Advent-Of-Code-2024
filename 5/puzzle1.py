def checkRules(pages: list, rules: list):
    for i in rules:
        if pages.index(i[0]) > pages.index(i[1]):
            return False
    return True

with open("input.txt", "r") as document:
    rules = []
    final = 0
    line = document.readline().strip("\n")
    while line:
        split = line.split("|")
        rules.append((int(split[0]), int(split[1])))
        line = document.readline().strip("\n")
    line = document.readline().strip("\n")
    while line:
        pages = line.split(",")
        pages = [int(i) for i in pages]
        currentrules = []
        for i in rules:
            if i[0] in pages and i[1] in pages:
                currentrules.append(i)
        print(pages)
        if checkRules(pages, currentrules):
            final += pages[int(len(pages)//2)]
            
        line = document.readline().strip("\n")
    
    print(final)