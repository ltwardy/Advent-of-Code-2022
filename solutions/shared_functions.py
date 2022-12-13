# Shared functions for AOC 2022

# from decorators import print_debugger
# import os
# from pathlib import Path

def data_filename(aoc_day):
    """Return the (string) name of the puzzle data file appropriate to today's Advent of Code puzzle."""
    readfile = aoc_filename(aoc_day) + "_input.txt"
    return readfile

# def data_filename(aoc_day):  # ToDo: fix this so it works from the wrapper script
#     """Return a path object pointing to the data file appropriate to today's Advent of Code puzzle."""
#      working_directory =
#      readfile = Path.joinpath(working_directory), aoc_filename(aoc_day), aoc_filename(aoc_day) + "_input.txt")
#      return readfile


def aoc_scriptname(aoc_day):
    """Return the (string) name of the python script solving this day's puzzle."""
    script = aoc_filename(aoc_day) + "_2022"
    return script


def aoc_filename(aoc_day) -> str:
    """Generate the correctly-formatted name of my AoC files appropriate to a given day."""
    day = str(aoc_day)
    if aoc_day < 10:
        day = "0" + day
    filename = "day_" + day
    return filename


def fetch_string_data(filename):
    """Reads a text file and returns its contents as a list of strings (one string per row in the original file)."""
    rawdata = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            line = str(line)
            rawdata.append(line)
    return rawdata


def fetch_rstrip_data(filename):
    """Reads a text file and returns its contents as a list of strings (one string per row in the original file)."""
    rawdata = []
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            line = str(line)
            rawdata.append(line)
    return rawdata


def fetch_raw_data(filename):
    """Reads a text file and returns its contents as a list of strings (one string per row in the original file)."""
    rawdata = []
    with open(filename, "r") as file:
        for line in file:
            line = line.rstrip()
            rawdata.append(line)
    return rawdata


def array_print(array_name):
    """Prints a list with one element per line rather than comma-separated"""
    for line in array_name:
        print(line)
