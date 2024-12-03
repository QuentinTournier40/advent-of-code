from re import findall
from functools import reduce

with open("./input.txt", "r") as file:
    line = [line.strip() for line in file]
    line = reduce(lambda x, y: x + y, line)

def removeDontPart(string):
    doList = []
    for e in string.split("do()"):
        doList += findall(r"^.*?(?=don't\(\))|^.*$", e)

    return doList


muls = []
result = 0

for e in removeDontPart(line):
    muls += findall(r"mul\(\d{1,3},\d{1,3}\)", e)

for mul in muls:
    x, y = findall(r"(\d{1,3})", mul)
    result += int(x) * int(y)

print(result)