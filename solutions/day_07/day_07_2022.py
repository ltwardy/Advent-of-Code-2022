# Advent of Code 2022
# Day 07: No Space Left On Device

import sys

sys.path.append("../")
from shared_functions import fetch_string_data
from shared_functions import array_print
from collections import namedtuple


class Directory():
    """I think I need a custom class to handle this data."""
    print("How do I do this again?")


def parse(raw_data: list[str]) -> list[list]:
    """Make our input more useful for problem-solving."""
    terminal_commands = [line.split() for line in raw_data]
    return terminal_commands


def create_filesystem(input: list) -> dict:
    """Read straight through our puzzle input, converting it to a dictionary of sets."""
    # let's try namedtuples.
    # tuples aren't mutable, but there's a ._replace() method to deal with that

    Directory = namedtuple("Directory", "name contents size", defaults=[[], None])
    File = namedtuple("File", "name size")

    # first, create our filesystem as a list of directories containing other directories and files
    root = Directory("/")
    namespace = {"/": root}
    filesystem = [root]
    directory_stack = []
    for line in input:
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    directory_stack.pop(-1)
                    cwd = directory_stack[-1]
                else:
                    directory_stack.append(line[2])
                    cwd = directory_stack[-1]
            else:  # command is ls
                pass
        elif line[0] == "dir":
            dirname = line[1]
            namespace[dirname] = Directory(dirname, [], None)
            filesystem.append(dirname)
            namespace[cwd].contents.append(dirname)
        elif line[0].isnumeric():
            filename = line[1]
            filesize = int(line[0])
            # cwd = directory_stack[-1]
            namespace[filename] = File(filename, filesize)
            namespace[cwd].contents.append(filename)
        else:
            raise ValueError(f"Unexpected input:{line}")
        print(f"namespace = {namespace}")
        print(f"filesystem = {filesystem}")
        print(f"directory_stack = {directory_stack}")
        print()

    #         if dir_name not in flat_fs.keys():
    #             flat_fs[dir_name] = {"size": 0, "contents": [], "type": "directory"}
    #     elif line[1] == "dir" and line[0] not in flat_fs.keys():
    #         flat_fs[line[0]] = {"size": None, "contents": []}
    #
    # # now crawl through again and populate the directories
    # cwd = "/"
    # for line in input:
    #     if line[0] == "$":
    #         if line[1] == "cd":  # change directories
    #             cwd = line[2]
    #     elif line[0].isnumeric():
    #         flat_fs[cwd]["contents"].append(line[1])
    #         flat_fs[cwd]["size"] += int(line[0])
    #         flat_fs[line[1]] = {"size": int(line[0]), "type": "file"}
    #     else:  # what's left are directory names
    #         print(line[1])
    #         print("Hm. How'd I miss that?")
    #         assert line[0] == "dir"
    #         if line[1] not in flat_fs.keys():
    #             flat_fs[line[1]] = {"size": 0, "contents": [], "type": "directory"}

    # print(flat_fs)
    return filesystem


def calculate_sizes(filesystem):
    """Crawl through filesystem and calculate directory sizes."""
    for item in filesystem:
        if item["type"] == "directory":
            for filedir in item["contents"]:
                item["size"] += filesystem[filedir]["size"]


def find_small_files_usage(filesystem, cutoff=100000):
    """Return the total space in a dictionary of files and folders occupied by items under a cutoff size. """
    usage = 0
    print(type(filesystem))
    print(filesystem)
    for item in filesystem:
        print(item)
        size = filesystem[item]["size"]
        if size <= cutoff:
            usage += size
    return usage


def solve_part_1(input, cutoff=100000):
    """Find the directories whose sizes are under a threshold and report the sum of their sizes."""
    filesystem = create_filesystem(input)
    # usage = find_small_files_usage(filesystem, cutoff)
    # return usage


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
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)

# solution("testing.txt")
