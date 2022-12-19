# Advent of Code 2022
# Day 10: Cathode-Ray Tube

from copy import deepcopy

from shared_functions import fetch_string_data


def parse(raw_data):
    """Make our input more useful for problem-solving."""
    processed_data = []
    for line in raw_data:
        if line[:4] == "addx":
            line = line.split()
            processed_data.append(int(line[1]))
        else:
            processed_data.append(None)
    return processed_data


def solve_part_1(input_instructions: list) -> int:
    """Find the state of a single register at specified points in a program's execution."""
    x = 1
    cycle = 0
    on_deck = 0
    signal_strength = []
    instructions = deepcopy(input_instructions)
    while instructions:
        cycle += 1
        # print(instructions[0])
        if (cycle - 20) % 40 == 0:
            print(f"During cycle {cycle}, the value of X is {x}.")
            signal_strength.append(x * cycle)

        if on_deck:
            x += on_deck
            on_deck = 0
        elif instructions[0] and not on_deck:
            on_deck = instructions.pop(0)
        else:
            _noop = instructions.pop(0)

    return sum(signal_strength)
    # Yay! 17180 is correct! gold star!


def solve_part_2(instructions: list) -> None:
    """Use the information in our program to render a readable message."""

    def sprite(i):
        return [i - 1, i, i + 1]

    x = 1
    cycle = 0
    on_deck = 0
    while instructions:
        # first draw the pixel
        if cycle % 40 == 0:
            print()
            cycle = 0
        if cycle in sprite(x):
            print("#", end="")
        else:
            print(".", end="")

        # then update the register in memory
        cycle += 1
        if on_deck:
            x += on_deck
            on_deck = 0
        elif instructions[0] and not on_deck:
            on_deck = instructions.pop(0)
        else:
            _noop = instructions.pop(0)
    # Bwaahaha! It works! I can read the simulated output: REHPRLUB
    #  and that's the correct answer: another gold star!


def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    program = parse(raw_data)

    interesting_signals = solve_part_1(program)
    print(f"The sum of the interesting signal strengths is {interesting_signals}.")

    print(f"The screen, if it weren't cracked, would be displaying:")
    solve_part_2(program)


# This can be run as a script from the command line, with data filename as argument.

if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
