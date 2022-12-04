""" Advent of Code 2022: wrapper for running my daily solution scripts."""
# 1 December 2022: This doesn't work yet

import importlib
import os

from modules.shared_functions import *


def run_aoc_scripts():
    """Ask user to choose and run Advent of Code scripts."""
    aoc_day = None
    while not aoc_day:
        try:
            aoc_day = input("Which day's challenge would you like to run? (Type Q to quit.) ")
            if aoc_day.upper() == "Q":
                break
            aoc_day = int(aoc_day)
            if aoc_day < 1 or aoc_day > 25:
                print("Day numbers must be between 1 and 25.")
                aoc_day = None
            else:
                print(f"Executing the day {aoc_day} script...")  # debug
                try:
                    print(__file__)
                    working_dir = os.getcwd()
                    print(working_dir)
                    print(os.listdir(working_dir))
                    todays_script = script_name(aoc_day)
                    print(todays_script)
                    todays_script = todays_script + ".py"
                    assert todays_script in os.listdir("modules")  #

                    solver = importlib.import_module(script_name(aoc_day))  # TODO: Fix broken path to today's script
                    solver.solution(puzzle_data(aoc_day))
                except ModuleNotFoundError as err:
                    print(f"That puzzle hasn't been solved yet: {err}.")
                aoc_day = None

        except ValueError:
            print("Please type an integer from 1 to 25, or Q to quit.")
            aoc_day = None

    print("Merry Christmas, and see you next year!")


# Execution begins here.
if __name__ == "__main__":
    run_aoc_scripts()
