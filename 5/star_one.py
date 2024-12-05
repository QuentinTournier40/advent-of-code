from math import floor


def get_rules_dict(rules):
    rules_dict = {f"{i}": [] for i in range(10, 100)}

    for rule in rules:
        rule = rule.split("|")
        rules_dict[rule[1]] += [rule[0]]

    return rules_dict


def is_page_correct(page, rules_dict):
    is_correct = True

    for i, number in enumerate(page):
        if not is_correct:
            continue

        # numbers that shouldn't be after 'number'
        list_number = rules_dict[number]

        for n in list_number:
            if n in page[i + 1:]:
                is_correct = False

    return is_correct


def get_correct_pages(pages, rules_dict):
    correct_pages = []

    for page in pages:
        page = page.split(",")
        is_correct = is_page_correct(page, rules_dict)

        if is_correct:
            correct_pages.append(page)

    return correct_pages


def get_page_middle_number(page):
    return int(page[floor(len(page) / 2)])


def main():
    with open("./input.txt", "r") as file:
        lines = [line.strip() for line in file]

    rules = lines[:lines.index('')]
    rules_dict = get_rules_dict(rules)

    pages = lines[lines.index('') + 1:]

    sum_middles = 0

    correct_pages = get_correct_pages(pages, rules_dict)

    for page in correct_pages:
        sum_middles += get_page_middle_number(page)

    print(sum_middles)


if __name__ == "__main__":
    main()
