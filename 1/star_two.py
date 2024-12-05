def main():
    with open("./input.txt", "r") as file:
        lines = [line.strip().split() for line in file]

    similarity_score = 0

    left = [int(line[0]) for line in lines]
    right = [int(line[-1]) for line in lines]

    for i in range(len(lines)):
        n = right.count(left[i])
        similarity_score += left[i] * n

    print(similarity_score)


if __name__ == "__main__":
    main()
