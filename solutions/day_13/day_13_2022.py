# Advent of Code 2022
# Day XX: Puzzle name

import sys

sys.path.append("../")
from shared_functions import fetch_raw_data
from shared_functions import array_print
from ast import literal_eval
import math


def parse(raw_data):
    """Make our input more useful for problem-solving."""
    better_data = []
    pair = []
    for line in raw_data:
        if line:
            pair.append(literal_eval(line))
        else:
            better_data.append(pair)
            pair = []
    else:  # append last pair which otherwise gets missed
        better_data.append(pair)

    return better_data


def compare_values(left, right):
    """Determine whether the given pair of values are in the correct order; return "correct", "wrong". or 'equal'"""
    print(left, " vs ", right)

    if type(left) is int and type(right) is int:
        # print("compare ints")
        return compare_ints(left, right)

    elif type(left) is list and type(right) is list:
        # print("compare lists")
        return compare_lists(left, right)

    else:  # one list, one integer
        # print("compare mixed")
        return compare_mixed(left, right)


def compare_ints(left: int, right: int):
    """If both arguments are integers, return a string related to their order; if not, raise an error."""
    if type(left) is not int or type(right) is not int:
        raise TypeError(f"Expected integer arguments: {left}, {right}.")
    print("Compare integers: ", left, " vs ", right)
    if left < right:
        print("Left is smaller, so inputs are in the right order.")
        return "correct"
    elif right < left:
        print("Right is smaller, so inputs ar NOT in the right order.")
        return "wrong"
    else:
        assert right == left
        # print("equal integers")
        return "equal"


def compare_lists(left: list, right: list):
    """Compare elements in lists index by index; if the right side has nothing to compare, the order is 'wrong'."""
    if type(left) is not list or type(right) is not list:
        raise TypeError(f"Expected list arguments: {left}, {right}.")
    print("Compare lists: ", left, " vs ", right)
    for e, l_element in enumerate(left):
        try:
            r_element = right[e]
        except IndexError:
            print("ran out of right-hand elements")
            order = "wrong"
            return order
        order = compare_values(l_element, r_element)
        if order == "equal":
            print("equal list elements")
        elif order == "wrong":
            return "wrong"
        else:
            assert order == "correct"
            return "correct"
    else:  # if the for loop is exhausted without incident
        return "equal"


def compare_mixed(left, right):
    print("Compare mixed: ", left, " vs ", right)
    if type(left) is int:
        assert type(right) is list
        left = [left]
    else:
        assert type(left) is list and type(right) is int
        right = [right]
    return compare_lists(left, right)


def solve_part_1(signal):
    """Determine how many packets are already in the correct order."""
    correct_indices = []
    print(signal)
    for index, pair in enumerate(signal):
        print(pair)
        # order = compare_lists(pair[0], pair[1])
        order = compare_values(pair[0], pair[1])
        if order == "correct" or order == "equal":
            print("That pair is in the correct order!")
            correct_indices.append(index + 1)
        else:
            print("Wrong order, sorry.")
        print()
    score = sum(correct_indices)
    return score
    # 52-something-something was too high
    # 4017 is too low
    # but the test case works, so this is going to require more work.  sigh.

def solve_part_2(input_data):
    """Describe the next puzzle."""
    pass


def solution(filename):
    """Briefly describe the puzzle here."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_raw_data(filename)
    signal = parse(raw_data)

    score = solve_part_1(signal)
    print("I've found which packets are in the correct order.")
    print(f"The sum of the indices of the correctly-ordered packet pairs is {score}.")

    solve_part_2(signal)


# This can be run as a script from the command line, with data filename as argument.

if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)

# solution("testing.txt")   # debug
