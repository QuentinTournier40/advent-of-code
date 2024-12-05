from re import findall
from functools import reduce


def get_do_list(string):
    do_list = []
    for e in string.split("do()"):
        do_list += findall(r"^.*?(?=don't\(\))|^.*$", e)

    return do_list


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
        line = [line.strip() for line in file]
        line = reduce(lambda x, y: x + y, line)

    result = 0

    do_list = get_do_list(line)
    muls = findall_mul(do_list)

    for mul in muls:
        result += get_mul_value(mul)

    print(result)


if __name__ == "__main__":
    main()
