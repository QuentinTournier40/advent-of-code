from math import floor


def get_rules_dict(rules):
    rules_dict = {f"{i}": [] for i in range(10, 100)}

    for rule in rules:
        rule = rule.split("|")
        rules_dict[rule[1]] += [rule[0]]

    return rules_dict


def is_page_correct(page, rules_dict):
    is_correct = True
    incorrect_numbers = []

    for i, number in enumerate(page):
        if not is_correct:
            continue

        # numbers that shouldn't be after 'number'
        list_number = rules_dict[number]

        for n in list_number:
            if n in page[i + 1:]:
                incorrect_numbers.append(n)
                is_correct = False

    return is_correct, incorrect_numbers


def get_incorrect_pages(pages, rules_dict):
    incorrect_pages = []

    for page in pages:
        page = page.split(",")
        is_correct, _ = is_page_correct(page, rules_dict)

        if not is_correct:
            incorrect_pages.append(page)

    return incorrect_pages


def fix_incorrect_page(page, rules_dict):
    is_correct, incorrect_numbers = is_page_correct(page, rules_dict)

    while not is_correct:
        for n in incorrect_numbers:
            index = page.index(n)
            page.pop(index)
            page.insert(0, n)

        is_correct, incorrect_numbers = is_page_correct(page, rules_dict)


def get_page_middle_number(page):
    return int(page[floor(len(page) / 2)])


def main():
    with open("./input.txt", "r") as file:
        lines = [line.strip() for line in file]

    rules = lines[:lines.index('')]
    rules_dict = get_rules_dict(rules)

    pages = lines[lines.index('') + 1:]

    sum_middles = 0

    incorrect_pages = get_incorrect_pages(pages, rules_dict)

    for page in incorrect_pages:
        fix_incorrect_page(page, rules_dict)
        sum_middles += get_page_middle_number(page)

    print(sum_middles)


if __name__ == "__main__":
    main()
