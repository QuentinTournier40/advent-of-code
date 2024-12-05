def main():
    with open("./input.txt", "r") as file:
        lines = [line.strip().split() for line in file]

    distance = 0

    left = [int(line[0]) for line in lines]
    right = [int(line[-1]) for line in lines]

    for _ in lines:
        min_left = min(left)
        min_right = min(right)

        distance += abs(min_left - min_right)

        left.remove(min_left)
        right.remove(min_right)

    print(distance)


if __name__ == "__main__":
    main()
