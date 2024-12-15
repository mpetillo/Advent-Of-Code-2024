def reorder(pages:list, rules:list):
    nodes = {}
    final = []
    for i in pages:
        nodes[i] = []
    for i in rules: 
        nodes[i[0]].append(i[1])
    while len(final) != len(pages):
        for key, value in nodes.items():
            if value == []:
                final.append(key)
                nodes.pop(key)
                for key2 in nodes:
                    try:
                        nodes[key2].remove(key)
                    except:
                        pass
                break
    return final[int(len(final)//2)]
    
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
        if not checkRules(pages, currentrules):
            final += reorder(pages, currentrules)
        line = document.readline().strip("\n")
    
    print(final)