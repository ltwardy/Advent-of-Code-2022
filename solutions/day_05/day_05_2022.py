# Advent of Code 2022
# Day 05: Supply Stacks

import copy
import sys

sys.path.append("../")

from shared_functions import fetch_rstrip_data


def parse(raw_data):
    """Make our input more useful for problem-solving."""

    stack_grid = []
    instructions = []
    for line in raw_data:
        if not line:
            continue
        if line[0] == "m":
            step = [int(element) for element in line.split() if element.isnumeric()]
            instructions.append(step)
        else:
            row = []
            while line:
                row.append(line[1:2])
                line = line[4:]
            stack_grid.append(row)

    # Now let's get the starting state information into a more useful format
    stacks_of_crates = [[] for _letter in stack_grid[-1]]
    for line in stack_grid:
        for index, character in enumerate(line):
            if character.isalpha():
                stacks_of_crates[index].append(character)
    stacks_of_crates.insert(0, ["dummy"])  # so my instructions line up nicely with the stack indices and I stay saner.

    return stacks_of_crates, instructions


def solve_part_1(starting_state, instructions) -> str:
    """Rearrange stacks of items one-by-one, according to my instructions.

    The top of each stack is the first item, i.e. stack[0]
    Items should only be removed or added at the top.
    At the end, I will read off the top elements and join them to give my answer to the puzzle.
    """
    stacks_of_crates = copy.deepcopy(starting_state)  # so I don't clobber my starting state for part 2
    for number, source, destination in instructions:
        for repeats in range(number):
            in_motion = stacks_of_crates[source].pop(0)
            stacks_of_crates[destination].insert(0, in_motion)
    top_crates = "".join([stack[0] for stack in stacks_of_crates[1:] if stack])
    return top_crates
    # Success! Gold star!


def solve_part_2(stacks_of_crates, instructions):
    """Rearrange stacks of items in groups, according to the corrected instructions.

    The top of each stack is the first item, i.e. stack[0]
    Items should only be removed or added at the top.
    At the end, I will read off the top elements and join them to give my answer to the puzzle.
    """

    for number, source, destination in instructions:
        in_motion = stacks_of_crates[source][:number]
        stacks_of_crates[source] = stacks_of_crates[source][number:]
        stacks_of_crates[destination][0:0] = in_motion  # whoa, I'd forgotten about that syntax -- thanks, internet :)
    top_crates = "".join([stack[0] for stack in stacks_of_crates[1:] if stack])
    return top_crates
    # Success again! Another gold star!


def solution(filename):
    """Simulate the rearrangement of stacks of crates."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_rstrip_data(filename)
    starting_state, instructions = parse(raw_data)

    top_crates = solve_part_1(starting_state, instructions)
    print(f"The top crates of the stacks after the crane is done moving them will be {top_crates}.")

    print("Oh, no! I was moving crates one at a time, but I should have moved them in order-preserving chunks.")
    top_crates = solve_part_2(starting_state, instructions)
    print(f"The top crates of the stacks after the crane is done moving them will actually be {top_crates}.")


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
