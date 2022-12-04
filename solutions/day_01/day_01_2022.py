# Advent of Code 2022
# Day 01: Calorie Counting

from shared_functions import fetch_data


def find_calories_per_elf(input_data: list) -> list[int]:
    calories_by_elf = [0]
    elf = 0
    for entry in input_data:
        if not entry:
            elf = 0
            calories_by_elf.append(elf)
        else:
            elf += int(entry)
            calories_by_elf[-1] = elf
    return calories_by_elf


def solve_part_1(calories_per_elf) -> int:
    """Find the elf carrying the most calories worth of food."""
    most_food = max(calories_per_elf)
    print(f"The elf carrying the most food has {most_food} calories in their pack.")
    return most_food
    # 654450 is correct! First star of the season!
    # Less than half an hour, including frowning at Git, renaming files, and other setup tasks


def solve_part_2(calories_per_elf) -> int:
    """Find how much food the top three food-carrying elves have, combined."""
    top_three_food = 0
    for top_elves in range(3):
        most_food = max(calories_per_elf)
        top_three_food += most_food
        top_carrier = calories_per_elf.index(most_food)
        del (calories_per_elf[top_carrier])
    print(f"The top three food-carrying elves have {top_three_food} calories between them.")
    # 199357 was correct! Day 1 complete! I love this game!

    return top_three_food


def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    processed_data = fetch_data(filename)
    calories_per_elf = find_calories_per_elf(processed_data)

    print("We need to find out how much food the elves have with them.")
    solve_part_1(calories_per_elf)
    solve_part_2(calories_per_elf)


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
