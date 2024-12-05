from re import findall


def findall_mul(array):
    muls = []
    for e in array:
        muls += findall(r"mul\(\d{1,3},\d{1,3}\)", e)

    return muls


def get_mul_value(mul):
    x, y = findall(r"(\d{1,3})", mul)
    return int(x) * int(y)


def main():
    with open("./input.txt", "r") as file:
        lines = [line.strip() for line in file]

    result = 0

    muls = findall_mul(lines)

    for mul in muls:
        result += get_mul_value(mul)

    print(result)


if __name__ == "__main__":
    main()
