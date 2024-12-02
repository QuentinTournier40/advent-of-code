with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file]

similarity = 0

left = [int(line.split()[0]) for line in lines]
right = [int(line.split()[-1]) for line in lines]

for i in range(len(lines)):
    occurrence = right.count(left[i])
    similarity += left[i] * occurrence

print(similarity)