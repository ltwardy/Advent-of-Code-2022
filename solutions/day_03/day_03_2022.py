# Advent of Code 2022
# Day 03: Rucksack Reorganization

from shared_functions import fetch_data


def parse_data(input_data) -> list[tuple]:
    rucksacks = []
    for line in input_data:
        splitplace = int(len(line) / 2)
        rucksacks.append((line[:splitplace], line[splitplace:]))
    return rucksacks


def priority_score(letter) -> int:
    return (ord(letter) - 38) if letter == letter.upper() else (ord(letter) - 96)


def solve_part_1(rucksacks):
    """Find duplicate items and assign letter scores.."""

    def oddball(compartments) -> str:
        for letter in compartments[0]:
            if letter in compartments[1]:
                return letter
        raise ValueError("There is no letter in compartment 1 that is also in compartment 2.")

    mispacked = [oddball(bag) for bag in rucksacks]
    score = sum([priority_score(letter) for letter in mispacked])
    return score
    # Correct! gold star!


def solve_part_2(elves):
    """Find duplicate items in groups of three elements."""
    groups = []
    while elves:
        groups.append(elves[:3])
        elves = elves[3:]

    badges = []
    for group in groups:
        for letter in group[0]:
            if letter in group[1] and letter in group[2]:
                badges.append(letter)
                break

    badges_score = sum([priority_score(letter) for letter in badges])
    return badges_score
    # 2607 is correct! Another gold star!


def solution(filename):
    """Help the elves with their mispacked supplies and badges."""
    # process data from filename to make it usable by our solving functions
    elves = fetch_data(filename)
    rucksacks = parse_data(elves)

    score1 = solve_part_1(rucksacks)
    print("The elves have mispacked some of their supplies.")
    print(f"The total priority score for all the wrongly packed items is {score1}.")

    score2 = solve_part_2(elves)
    print("The elves have also forgotten to properly label their ID badges.")
    print(f"The total priority score for their badges is {score2}.")


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
