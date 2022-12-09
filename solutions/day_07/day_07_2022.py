# Advent of Code 2022
# Day 07: No Space Left On Device

import sys

sys.path.append("../")
from shared_functions import fetch_string_data


class Directory():
    """I think I need a custom class to handle this data."""
    print("How do I do this again?")


def parse(raw_data: list[str]) -> list[list]:
    """Make our input more useful for problem-solving."""
    terminal_commands = [line.split() for line in raw_data]
    return terminal_commands


def create_filesystem(input: list) -> dict:
    """Read straight through our puzzle input, converting it to a dictionary of sets."""
    filesystem = dict()
    cwd = None
    # first, create our dictionary of directories
    for line in input:
        if line[0] == "$" and line[1] == "cd":
            cwd = line[2]
            if "." not in cwd and cwd not in filesystem:
                filesystem[cwd] = {}

    # now crawl through again and populate the directories
    cwd = []
    sizes = dict()
    for line in input:
        for line in input:
            if line[0] == "$" and line[1] == "cd":  # change directories
                while line[2]:
                    if "." in line[2]:
                        print(line[2], "pop! ", end="")
                        line[2] = line[2][1:]
                        print("from ", cwd)
                        cwd.pop()
                        continue
                    cwd.append(line[2])
                    line[2] = None
            elif line[0] == "$" and line[1] == "ls":  # populate current directory and track sizes
                continue
            else:  # it's either a file or a directory
                print("we're in ", cwd)
                print("add ", filesystem[cwd[-1]])
                # filesystem[cwd[-1]] = filesystem[cwd[-1]] + [line[1]]
                sizes[line[1]] = line[0]

    print(filesystem)
    print()
    print(sizes)

    return sizes


def solve_part_1(input, cutoff=100000):
    """Find the directories whose sizes are under a threshold and report the sum of their sizes."""
    _filesystem, sizes = create_filesystem(input)
    total = 0
    for directory in sizes.keys():
        if sizes[directory] > 100000:
            total += sizes[directory]
        return total


def solve_part_2(input_data):
    """Describe the next puzzle."""
    pass


def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    terminal_output = parse(raw_data)

    small_files = solve_part_1(terminal_output)
    print(f"The files and directories under 100k each occupy a total of {small_files}.")

    solve_part_2(terminal_output)


# This can be run as a script from the command line, with data filename as argument.
# if __name__ == "__main__":
#     import sys
#
#     try:
#         arg = sys.argv[1]
#     except IndexError:
#         raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")
#
#     print(f"Data file = '{arg}'.")  # debug
#     solution(arg)

solution("testing.txt")
