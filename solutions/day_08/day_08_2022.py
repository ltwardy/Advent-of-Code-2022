# Advent of Code 2022
# Day 08: Treetop Tree House

import sys

sys.path.append("../")
from shared_functions import fetch_string_data
import numpy as np


def parse(raw_data):
    """Convert our input to a numpy array."""
    grid = [[int(char) for char in line] for line in raw_data]
    grid = np.array(grid)
    print(grid)
    return grid


def solve_part_1(grid):
    """Count how many trees are visible from outside the grid."""
    rows, columns = grid.shape
    visible = (2 * rows) + (2 * columns) - 4
    for r in range(1, rows - 1):
        for c in range(1, columns - 1):
            if r == (0 or rows - 1) or c == (0 or columns - 1):
                visible += 1
                continue
            else:
                if grid[r, c] > min((np.max(grid[r, :c]),
                                     np.max(grid[r, c + 1:]),
                                     np.max(grid[:r, c]),
                                     np.max(grid[r + 1:, c]))):
                    visible += 1
    return visible
    # Success! That was easier than yesterday :)


def solve_part_2(grid):
    """Find the tree with the best view of other trees."""
    rows, columns = grid.shape
    best_tree = 0
    for r in range(1, rows - 1):
        for c in range(1, columns - 1):
            tree = grid[r, c]
            scenery = []
            for view in (np.flip(grid[r, :c]),
                         grid[r, c + 1:],
                         np.flip(grid[:r, c]),
                         grid[r + 1:, c]):
                visible = 0
                for neighbor in view:
                    visible += 1
                    if neighbor >= tree:
                        break
                scenery.append(visible)
            scenic_score = np.prod(scenery)
            if scenic_score > best_tree:
                best_tree = scenic_score
    return best_tree
    # Ok, got it!


def solution(filename):
    """Help the elves assess locations for placement of a tree house."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    grid = parse(raw_data)

    visible_trees = solve_part_1(grid)
    print(f"{visible_trees} trees can be seen from outside the patch of forest.")

    score = solve_part_2(grid)
    print(f"The best tree in this patch of forest has a scenic score of {score}.")


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
