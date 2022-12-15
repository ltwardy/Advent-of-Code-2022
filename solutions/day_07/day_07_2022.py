# Advent of Code 2022
# Day 07: No Space Left On Device

from pprint import pprint
import sys

sys.path.append("../")
from shared_functions import fetch_string_data


def calculate_size(files):
    return sum([f.size for f in files])


class Directory:
    """I think I need a custom class to handle this data."""

    def __init__(self, name: str, contents=None):
        self.name = name
        if contents is None:
            contents = []
        self.contents = contents
        # self.parent = "/".join(directory_stack)
        self.parent = cwd

    @property
    def size(self):
        if self.contents:
            return sum([f.size for f in self.contents])
        else:
            return 0

    def __repr__(self):
        return f"Directory ({self.parent}.{self.name}: {self.contents}, {self.size}"

    def append_file(self, other):
        self.contents = self.contents.append(other)


class File:
    """I wish I had just done this from the beginning."""

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        # self.parent = "/".join(directory_stack)
        self.parent = cwd

    def __repr__(self):
        return f"File {self.parent}.{self.name}: size {self.size}"


def parse(raw_data: list[str]) -> list[list]:
    """Make our input more useful for problem-solving."""
    terminal_commands = [line.split() for line in raw_data]
    return terminal_commands


def create_filesystem(puzzle_input: list) -> dict:
    """Read straight through our puzzle input, converting it to a dictionary of sets."""

    # first, create our filesystem as a dictionary of files and directories
    global filesystem
    global directory_stack
    global cwd
    directory_stack = []
    filesystem = {"/": Directory("/")}
    cwd = None
    for lnum, line in enumerate(puzzle_input):
        print(f"line {lnum}:")
        if line[0] == "$":
            if line[1] == "cd":
                dirname = line[2]
                if dirname == "..":
                    directory_stack.pop(-1)
                    cwd = directory_stack[-1]
                    print(f"back up a level")
                else:
                    try:
                        assert isinstance(filesystem[dirname], Directory)
                        print(f"change to directory {dirname}")
                        directory_stack.append(line[2])
                        cwd = directory_stack[-1]
                    except AssertionError:
                        print(f"{dirname} is not a Directory")
            else:  # command is ls, and no action is needed this line
                print(f"next lines list the contents of directory {cwd}")
        elif line[0] == "dir":
            dirname = line[1]
            if dirname not in filesystem.keys():
                newdir = Directory(dirname)
                print(f"create directory {dirname}")
                filesystem[dirname] = newdir
                print(f"add directory {dirname} to the filesystem")
                filesystem[cwd].contents.append(newdir)
                print(f"add directory {dirname} to {filesystem[cwd].name}")
        elif line[0].isnumeric():
            filename = line[1]
            filesize = int(line[0])
            if filename not in filesystem.keys():
                newfile = File(filename, filesize)
                # filesystem[filename] = newfile
                print(f"create file {filename}")
                try:
                    parent = filesystem[cwd]
                    parent.contents.append(newfile)
                    print(f"add file {filename} to directory {parent}")
                except AttributeError as a:
                    print("--------------------------------------------------------------")
                    print("Error ad")
                    print(f"line {lnum}: {directory_stack} : {filesystem[cwd]} : {line}")
                    print(a)
                    print("--------------------------------------------------------------")
                    break
        else:
            raise ValueError(f"Unexpected input:{line}")

        print(f"directory_stack = {directory_stack}")
        pprint(filesystem)
        print()

    return filesystem


# def find_small_files_usage(filesystem, cutoff):
#     """Return the total space in a dictionary of files and directories by any items under a cutoff size. """
#     usage = 0
#     for filefolder in filesystem.values():
#         fsize = filefolder.size
#         if fsize <= cutoff:
#             usage += fsize
#     return usage


def find_small_dirs_usage(filesystem, cutoff):
    """Return the total space in a dictionary of files and directories used by directories under a cutoff size. """
    usage = 0
    for filefolder in filesystem.values():
        if isinstance(filefolder, Directory):
            fsize = filefolder.size
            if fsize <= cutoff:
                usage += fsize
    return usage


def solve_part_1(puzzle_input, cutoff=100000):
    """Find the directories whose sizes are under a threshold and report the sum of their sizes."""
    filesystem = create_filesystem(puzzle_input)
    usage = find_small_dirs_usage(filesystem, cutoff)
    return usage
    # problem 1: this solves the test case correctly but recurses too deeply for the input file (?!)
    # problem 2: solved the recursion problem but my answer 1057205 is too low


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
