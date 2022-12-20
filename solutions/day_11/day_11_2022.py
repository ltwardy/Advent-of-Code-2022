# Advent of Code 2022
# Day 11: Monkey in the Middle

from pprint import pprint

from shared_functions import fetch_string_data


def parse(raw_data):
    """Make our input more useful for problem-solving."""
    # First, break the input into monkeys
    better_data = []
    monkey = []
    raw_data.append("")  # to make sure the last monkey makes it into the data
    for line in raw_data:
        if not line:
            better_data.append(monkey)
            monkey = []
        elif line and not line.startswith("Monkey"):
            monkey.append(line)
            continue

    # Now let's turn text into numbers
    monkey_behavior = []
    for data_group in better_data:
        monkey = dict()

        items = data_group[0][16:]
        items = [int(i) for i in items.split(", ")]
        monkey["items"] = items

        operation = data_group[1][11:]
        operation = operation.split()
        operation = operation[-2:]
        if operation[-1].isnumeric():
            operation[-1] = int(operation[-1])
        monkey["operation"] = operation

        test = data_group[2][6:]
        test = test.split()
        test = int(test[-1])
        monkey["test"] = test

        true = data_group[3].split()
        true = int(true[-1])
        monkey["true"] = true

        false = data_group[4].split()
        false = int(false[-1])
        monkey["false"] = false

        monkey_behavior.append(monkey)

    pprint(monkey_behavior)
    return monkey_behavior


def solve_part_1(input_data):
    """Describe the puzzle."""
    pass


def solve_part_2(input_data):
    """Describe the next puzzle."""
    pass


def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    notes = parse(raw_data)

    solve_part_1(notes)
    solve_part_2(notes)


# This can be run as a script from the command line, with data filename as argument.

if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        arg = "testing.txt"
        # raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
