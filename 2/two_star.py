with open("./input.txt", "r") as file:
    lines = [list(map(int, line.strip().split())) for line in file]

def isSafe(line):
    if line != sorted(line) and line != sorted(line, reverse=True):
        return False

    goodDifference = 0
    
    for i in range(len(line)-1):
        if 0 < abs(line[i] - line[i+1]) <= 3:
            goodDifference += 1

    return goodDifference == len(line) - 1


safeReports = 0

for line in lines:
    isAnySafe = []

    for i in range(len(line)):
        item = line.pop(i)
        isAnySafe.append(isSafe(line))
        line.insert(i, item)

    if True in isAnySafe:
        safeReports += 1

print(safeReports)

