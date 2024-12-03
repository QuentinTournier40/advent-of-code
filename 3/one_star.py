from re import findall

with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file]

muls = []
result = 0

for line in lines:
    muls += findall(r"mul\(\d{1,3},\d{1,3}\)", line)

for mul in muls:
    x, y = findall(r"(\d{1,3})", mul)
    result += int(x) * int(y)

print(result)
