with open("./input.txt", "r") as file:
    lines = [list(map(int, line.strip().split())) for line in file]

safeReports = 0

for line in lines:
    if line != sorted(line) and line != sorted(line, reverse=True):
        continue

    goodDifference = 0
    
    for i in range(len(line)-1):
        if 0 < abs(line[i] - line[i+1]) <= 3:
            goodDifference += 1
    
    if goodDifference == len(line) - 1:
        safeReports += 1

print(safeReports)