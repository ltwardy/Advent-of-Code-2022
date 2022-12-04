# Advent of Code 2022
# Day 04: Camp Cleanup


from shared_functions import fetch_data


def parse_input(raw_data) -> list[list[list, list]]:
    """Reformat the puzzle input into something nicer to wrk with."""
    chore_assignments = []
    for elf_pair in raw_data:
        pair = []
        for elf in elf_pair.split(","):
            chores = [int(endpoint) for endpoint in elf.split("-")]
            chores = set(range(chores[0], chores[1] + 1))
            pair.append(chores)
        chore_assignments.append(pair)
    print(chore_assignments)
    return chore_assignments


def solve_part_1(chore_assignments) -> int:
    """Find the elves whose chores are a subset of their partner's."""
    complete_overlaps = 0
    for pair in chore_assignments:
        elf1, elf2 = pair
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            complete_overlaps += 1
    return complete_overlaps
    # 500 elves have assignments that are completely contained in their partner's chore assignments. Correct!
    # That was almost too easy...


def solve_part_2(chore_assignments):
    """Find the chore assignment pairs containing any duplicate work."""
    partial_overlaps = 0
    for pair in chore_assignments:
        elf1, elf2 = pair
        if elf1.intersection(elf2):
            partial_overlaps += 1
    return partial_overlaps
    # 815 is correct! another gold star!
    # If the potentially-overlapping ranges were truly enormous, I'd use a less memory-intensive technique,
    # but for today's puzzle this works fine.


def solution(filename):
    """Help the elves reduce duplication of cleanup efforts."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_data(filename)
    chore_assignments = parse_input(raw_data)

    duplicates = solve_part_1(chore_assignments)
    print(f"{duplicates} elves have completely redundant chore assignments.")

    overlaps = solve_part_2(chore_assignments)
    print(f"{overlaps} pairs of chore assignments contain some duplicated work.")


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
