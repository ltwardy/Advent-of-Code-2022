""" Advent of Code 2022: wrapper for running my daily solution scripts."""

from pydoc import importfile

from pyprojroot import here


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
                    if aoc_day < 10:
                        aoc_day = "0" + str(aoc_day)
                    else:
                        aoc_day = str(aoc_day)

                    solver_path = here() / "solutions" / f"day_{aoc_day}" / f"day_{aoc_day}_2022.py"
                    solver_path = str(solver_path.resolve())

                    data_path = here() / "solutions" / f"day_{aoc_day}" / "input.txt"
                    data_path = str(data_path.resolve())

                    solver = importfile(solver_path)
                    solver.solution(data_path)
                except FileNotFoundError:
                    print(f"That puzzle hasn't been solved yet.")
                aoc_day = None

        except ValueError:
            print("Please type an integer from 1 to 25, or Q to quit.")
            aoc_day = None

    print("Merry Christmas, and see you next year!")


# Execution begins here.
if __name__ == "__main__":
    run_aoc_scripts()
