import re

with open("input.txt", "r") as document:
    line = document.readline()
    final = 0
    while line:
        regex = re.compile(r"mul\(\d+,\d+\)")
        m = regex.findall(line)
        regexnum = re.compile(r"\d+")
        print(m)
        for i in m:
            nums = regexnum.findall(i)
            final += int(nums[0]) * int(nums[1])
        line = document.readline()
    print(final)
