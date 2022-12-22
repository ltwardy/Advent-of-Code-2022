# Advent of Code 2022
# Day 11: Monkey in the Middle


import math
import sys
from copy import deepcopy

sys.path.append("../")

from decorators import *
from shared_functions import fetch_string_data

# toggle printing
global suppress_printing

debug_option = input("There's a lot of monkey business in this puzzle.  Do you want to see the shenanigans (y/N)? ")
if debug_option.upper() == "Y":
    suppress_printing = False
else:
    suppress_printing = True


def parse(raw_data):
    """Make our input more useful for problem-solving."""
    # First, break the input into monkeys
    better_data = []
    monkey = []
    raw_data.append("")  # to pass my "if not line" check and make sure the last monkey gets appended
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
        operation = operation.split()[-2:]
        if operation[-1].isnumeric():
            operation[-1] = int(operation[-1])
        monkey["operation"] = operation

        test = data_group[2][6:]
        test = test.split()
        monkey["test"] = int(test[-1])

        true = data_group[3].split()
        monkey["true"] = int(true[-1])

        false = data_group[4].split()
        monkey["false"] = int(false[-1])

        monkey["activity"] = 0
        monkey_behavior.append(monkey)
    return monkey_behavior


def perform_operation(old: int, operation: str, increase_num):
    try:
        increase_num = int(increase_num)
        if operation == "+":
            print(f"  Worry level is increased by {increase_num} to {old + increase_num}")
            return old + increase_num
        else:
            print(f"  Worry level is multiplied by {increase_num} to {old * increase_num}")
            return int(old) * increase_num
    except ValueError:
        print(f"  Worry level is squared to {old ** 2}")
        return old ** 2


@conditional_decorator(disable_printing, suppress_printing)
def monkey_business(monkeys: list, number_of_rounds=20, relief_happens=True) -> int:
    """Find the most active monkeys and report a worry score."""
    monkeys = deepcopy(monkeys)
    modulo_trick = math.prod([monkey["test"] for monkey in monkeys])
    assert type(modulo_trick) is int

    for r in range(number_of_rounds):
        for m, active_monkey in enumerate(monkeys):
            print(f"Monkey {m}")
            items_held = active_monkey["items"]
            active_monkey["activity"] += len(items_held)
            while items_held:
                item = items_held.pop(0)
                print(f" Monkey inspects an item with worry level of {item}.")
                operation = active_monkey["operation"]
                new_worry = perform_operation(item, *operation)
                if relief_happens:
                    relief = new_worry // 3
                else:
                    relief = new_worry % modulo_trick
                print(f"   Monkey gets bored; worry level is divided by 3 to {relief}")
                if _test_result := relief % active_monkey["test"]:
                    destination = active_monkey["false"]
                    print(f"    Current worry level {relief} is not divisble by {active_monkey['test']}: ", end='')
                    print(f"throw to monkey {destination}")
                    monkeys[destination]["items"].append(relief)
                else:
                    destination = active_monkey["true"]
                    print(f"    Current worry level {relief} is divisble by {active_monkey['test']}: ", end='')
                    print(f"throw to {destination}")
                    monkeys[destination]["items"].append(relief)
            # nothing more to pop
            print("out of items for this monkey")
            print()
            continue
        print(f"At the end of round {+ 1},")
        for m, monkey in enumerate(monkeys):
            print(f"Monkey {m}: {monkey['items']}")
        print()
    print(f"After {number_of_rounds} rounds of shenanigans:")
    for m, monkey in enumerate(monkeys):
        print(f"Monkey {m} inspected items {monkey['activity']} times.")
    activities = [monkey["activity"] for monkey in monkeys]
    top_2 = sorted(activities)[-2:]
    print(top_2)
    shenanigans_score = math.prod(top_2)
    return shenanigans_score
    # Yay! part 1 is correct!
    # This can be rewritten slightly to accommodate changes for part 2
    # (once I've read enough to understand the modulo trick and why it works, because I was not getting it on my own).
    # Part 2 now works as well -- thanks, internet!


def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    notes = parse(raw_data)

    hijinks = monkey_business(notes)
    print(f"The level of monkey business in this situation is {hijinks}.")

    more_hijinks = monkey_business(notes, number_of_rounds=10_000, relief_happens=False)
    print(f"If I keep getting more worried, after 10000 rounds the level of monkey business will be {more_hijinks}.")


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        arg = "testing.txt"

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
