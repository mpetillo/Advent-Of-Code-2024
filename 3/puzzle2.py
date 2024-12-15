import re

with open("input.txt", "r") as document:
    line = document.readline()
    final = 0
    add = True
    while line:
        regex = re.compile(r"mul\(\d+,\d+\)|don't\(\)|do\(\)")
        m = regex.findall(line)
        regexnum = re.compile(r"\d+")
        print(m)
        for i in m:
            if "don't" in i:
                add = False
            elif "do" in i:
                add = True
            else:
                if add:
                    nums = regexnum.findall(i)
                    final += int(nums[0]) * int(nums[1])
        line = document.readline()
    print(final)
