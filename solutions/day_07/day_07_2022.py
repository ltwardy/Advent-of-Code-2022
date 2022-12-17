# Advent of Code 2022
# Day 07: No Space Left On Device

import sys
from pprint import pprint

sys.path.append("../")
from shared_functions import fetch_string_data


# I think I need a custom class to handle this data.
class Directory:
    """Requires two arguments, name (a string) and path-to-directory (a tuple).
    Contents can be specified at creation or can be added by a class method.
    Size is calculated internally based on the current contents."""

    def __init__(self, name: str, path: tuple, contents=None):
        self.name = name
        if contents is None:
            contents = []
        self.contents = contents
        self.path = path

    @property
    def size(self):
        if self.contents:
            return sum([f.size for f in self.contents])
        else:
            return 0

    def __repr__(self):
        return f"Directory ({self.path}: {self.name}: {self.contents}, {self.size}"

    def append_file(self, other):
        self.contents = self.contents.append(other)


# I wish I had just done this from the beginning.
class File:
    """Requires three parameters, name (string), path (tuple), and size (integer)."""

    def __init__(self, name: str, path: tuple, size: int):
        self.name = name
        self.size = size
        self.path = path

    def __repr__(self):
        return f"File {self.path}: {self.name}: size {self.size}"


def parse(raw_data: list[str]) -> list[list]:
    """Make our input more useful for problem-solving."""
    terminal_output = [line.split() for line in raw_data]
    return terminal_output


def create_filesystem(puzzle_input: list) -> dict:
    """Read straight through our puzzle input, converting it to a dictionary of file and directory objects."""
    global filesystem
    global directory_stack
    directory_stack = ["root"]
    filesystem = {("root", "/"): Directory("/", ("root",))}

    for lnum, line in enumerate(puzzle_input):
        print(f"line {lnum}:")

        if line[0] == "dir":
            dirname = line[1]
            full_path = [d for d in directory_stack] + [dirname]
            full_path = tuple(full_path)
            parent_path = tuple(directory_stack)
            if full_path not in filesystem.keys():
                newdir = Directory(dirname, tuple(directory_stack))
                print(f"created directory {dirname} at location {full_path}")
                filesystem[full_path] = newdir
                print(f"added directory {full_path} to the filesystem")
                filesystem[parent_path].contents.append(newdir)
                print(f"added directory {full_path} to {filesystem[parent_path]}")

        elif line[0].isnumeric():
            filename = line[1]
            full_path = [d for d in directory_stack] + [filename]
            full_path = tuple(full_path)
            parent_path = tuple(directory_stack)
            filesize = int(line[0])
            if full_path not in filesystem.keys():
                newfile = File(filename, parent_path, filesize)
                print(f"created file {filename} at location {full_path}")
                filesystem[full_path] = newfile
                print(f"added file {full_path} to the filesystem")
                filesystem[parent_path].contents.append(newfile)
                print(f"added file{full_path} to {filesystem[parent_path]}")

        elif line[0] == "$":
            if line[1] == "cd":
                dirname = line[2]
                if dirname == "..":
                    directory_stack.pop(-1)
                    if not directory_stack:
                        raise RuntimeError("Illegal directory change: can't pop past the base of the directory tree.")
                    print(f"back up a level")
                else:
                    try:
                        assert isinstance(filesystem[tuple(directory_stack + [dirname])], Directory)
                    except AssertionError:
                        print(f"{dirname} is not a Directory in the path {directory_stack}.")
                    directory_stack.append(dirname)
                    print(f"change to directory {tuple(directory_stack)}")

            else:  # command is ls, and no action is needed this line
                print(f"next lines list the contents of directory {tuple(directory_stack)}")

        else:
            raise ValueError(f"Unexpected input:{line}")

    return filesystem


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
    return usage, filesystem
    # 16 Dec 22: hallelujah! 1428881 is the correct answer!


def solve_part_2(filesystem):
    """Find the smallest directory with that frees up enough space on the device."""

    dir_sizes = []
    for item in filesystem.values():
        if isinstance(item, Directory):
            dir_sizes.append(item.size)
    root = max(dir_sizes)  # it had better be the largest!
    unused = 70000000 - root
    more_space_needed = 30000000 - unused
    large_enough = [d for d in dir_sizes if d >= more_space_needed]
    just_large_enough = min(large_enough)
    assert just_large_enough + unused >= 30000000
    return just_large_enough
    # happy dance! that works!


def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    terminal_output = parse(raw_data)

    small_dirs, filesystem = solve_part_1(terminal_output)
    print(f"The directories under 100k each occupy a total of {small_dirs}.")

    pprint(filesystem)
    smallest_big_dir = solve_part_2(filesystem)
    print(f"The smallest directory of sufficient size takes up {smallest_big_dir} disk space.")


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
