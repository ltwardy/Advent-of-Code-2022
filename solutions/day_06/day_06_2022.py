# Advent of Code 2022
# Day 06: Tuning Trouble


from shared_functions import fetch_string_data


def solve_part_1(datastream) -> int:
    """Find the first block of 4 non-repeating characters in an input stream."""
    for i in range(3, len(datastream)):
        if len(set(datastream[i - 3: i + 1])) == 4:
            return i + 1
    # Success, but after way more failed attempts than I expected.


def solve_part_2(datastream):
    """Find the first block of 14 non-repeating characters in an input stream."""
    for i in range(13, len(datastream)):
        if len(set(datastream[i - 13: i + 1])) == 14:
            return i + 1
    # Success! Just solve the problem that was asked; I don't need to write the general case.


def solution(filename):
    """Help the elves fix a broken communications device."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    datastream: str = raw_data[0]

    start_of_packet = solve_part_1(datastream)
    print(f"The start-of-packet marker occurs after character number {start_of_packet}.")

    start_of_message = solve_part_2(datastream)
    print(f"The first start-of-message marker occurs after character number {start_of_message}.")


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
