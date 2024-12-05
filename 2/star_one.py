def is_line_safe(line):
    # not all increasing or all decreasing
    if line != sorted(line) and line != sorted(line, reverse=True):
        return False

    good_difference = 0

    for i in range(len(line) - 1):
        if 0 < abs(line[i] - line[i + 1]) <= 3:
            good_difference += 1

    return good_difference == len(line) - 1


def main():
    with open("./input.txt", "r") as file:
        lines = [list(map(int, line.strip().split())) for line in file]

    safe_reports = 0

    for line in lines:
        if is_line_safe(line):
            safe_reports += 1

    print(safe_reports)


if __name__ == "__main__":
    main()
