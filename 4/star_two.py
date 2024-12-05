def is_xmas(lines, x, y):
    try:
        top_left_bottom_right = ((lines[y - 1][x - 1] == "M" and
                                  lines[y + 1][x + 1] == "S") or
                                 (lines[y - 1][x - 1] == "S" and
                                  lines[y + 1][x + 1] == "M") and
                                  y > 0 and
                                  x > 0)
    except IndexError:
        top_left_bottom_right = False

    try:
        bottom_left_top_right = ((lines[y + 1][x - 1] == "M" and
                                 lines[y - 1][x + 1] == "S") or
                                (lines[y + 1][x - 1] == "S" and
                                 lines[y - 1][x + 1] == "M") and
                                 y > 0 and
                                 x > 0)
    except IndexError:
        bottom_left_top_right = False

    return top_left_bottom_right and bottom_left_top_right


def main():
    with open("./input.txt", "r") as file:
        lines = [line.strip() for line in file]

    xmas_number = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "A":
                if is_xmas(lines, x, y):
                    xmas_number += 1

    print(xmas_number)


if __name__ == "__main__":
    main()
