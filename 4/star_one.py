
def search_xmas_horizontally(array, x, y):
    cpt = 0

    try:
        if (array[y][x + 1] == "M" and
            array[y][x + 2] == "A" and
            array[y][x + 3] == "S"):
            cpt += 1
    except IndexError:
        pass

    try:
        if (array[y][x - 1] == "M" and
            array[y][x - 2] == "A" and
            array[y][x - 3] == "S" and
            x >= 3):
            cpt += 1
    except IndexError:
        pass

    return cpt


def search_xmas_vertically(array, x, y):
    cpt = 0
    try:
        if (array[y + 1][x] == "M" and
            array[y + 2][x] == "A" and
            array[y + 3][x] == "S"):
            cpt += 1
    except IndexError:
        pass

    try:
        if (array[y - 1][x] == "M" and
            array[y - 2][x] == "A" and
            array[y - 3][x] == "S" and
            y >= 3):
            cpt += 1
    except IndexError:
        pass

    return cpt


def search_xmas_diagonally(array, x, y):
    cpt = 0

    try:
        if (array[y - 1][x - 1] == "M" and
            array[y - 2][x - 2] == "A" and
            array[y - 3][x - 3] == "S" and
            y >= 3 and
            x >= 3):
            cpt += 1
    except IndexError:
        pass

    try:
        if (array[y + 1][x - 1] == "M" and
            array[y + 2][x - 2] == "A" and
            array[y + 3][x - 3] == "S" and
            x - 3 >= 0):
            cpt += 1
    except IndexError:
        pass

    try:
        if (array[y - 1][x + 1] == "M" and
            array[y - 2][x + 2] == "A" and
            array[y - 3][x + 3] == "S" and
            y - 3 >= 0):
            cpt += 1
    except IndexError:
        pass

    try:
        if (array[y + 1][x + 1] == "M" and
            array[y + 2][x + 2] == "A" and
            array[y + 3][x + 3] == "S"):
            cpt += 1
    except IndexError:
        pass

    return cpt


def main():
    with open("./input.txt", "r") as file:
        lines = [line.strip() for line in file]

    xmas_number = 0

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "X":
                xmas_number += search_xmas_horizontally(lines, x, y)
                xmas_number += search_xmas_vertically(lines, x, y)
                xmas_number += search_xmas_diagonally(lines, x, y)

    print(xmas_number)


if __name__ == "__main__":
    main()
