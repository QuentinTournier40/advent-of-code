with open("./input.txt", "r") as file:
    lines = [line.strip() for line in file]

distance = 0

left = [int(line.split()[0]) for line in lines]
right = [int(line.split()[-1]) for line in lines]

for _ in range(len(lines)):
    minLeft = min(left)
    minRight = min(right)

    distance += abs(minLeft - minRight)

    left.remove(minLeft)
    right.remove(minRight)

print(distance)