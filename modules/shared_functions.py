# Shared functions for AOC 2021

# from decorators import print_debugger

# def choose_dataset(aoc_day):
#     """Return the (string) name of the data file appropriate to today's Advent of Code puzzle."""
#     dataset = None
#     readfile = None
#     while not dataset:
#         dataset = input("Choose your dataset: 0 = testing, 1 = the real thing, Q to choose another day. (Default is 0.) ")
#         if dataset.upper() == "Q":
#             return
#         elif dataset == "1":
#             readfile = "day" + str(aoc_day) + "_input.txt"
#         else:
#             readfile = "day" + str(aoc_day) + "_testing.txt"
#     return readfile

def puzzle_data(aoc_day):
    """Return the (string) name of the puzzle data file appropriate to today's Advent of Code puzzle."""
    readfile = "data/day" + str(aoc_day) + "_input.txt"
    return readfile


def script_name(aoc_day):
    """Return the (string) name of the python script solving this day's puzzle."""
    day = str(aoc_day)
    if aoc_day < 10:
        day = "0" + day
    script = "day_" + day + "_revised"
    return script


def fetch_data(filename):
    """Reads a text file and returns its contents as a list of strings (one string per row in the original file)."""
    rawdata = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            line = str(line)
            rawdata.append(line)
    return rawdata


def array_print(array_name):
    """Prints a list with one element per line rather than comma-separated"""
    for line in array_name:
        print(line)
