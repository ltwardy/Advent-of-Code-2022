# Advent of Code 2022
# Day 02: Rock Paper Scissors


from shared_functions import fetch_data


def parse_input(raw_input: list) -> list[tuple]:
    """Reformat the puzzle input to make it easier to handle."""
    strategy_guide = []
    for line in raw_input:
        elf, me = line.split()
        elf_choices = {"A": "Rock", "B": "Paper", "C": "Scissors"}
        my_choices = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
        strategy_guide.append((elf_choices[elf], my_choices[me]))
    return strategy_guide


def find_winner(move_pair: tuple) -> str:
    """Find the winner of a round of 'rock, paper, scissors', in which the opponent's move is given first."""
    win_cases = {("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock")}
    if move_pair in win_cases:
        return "lose"
    elif move_pair[0] == move_pair[1]:
        return "draw"
    else:
        return "win"


def score_per_round(move_pair: tuple) -> int:
    """Use the elves' arcane rules to calculate the score for a single round of 'rock, paper, scissors'."""
    shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}
    outcome_score = {"win": 6, "draw": 3, "lose": 0}
    winner = find_winner(move_pair)
    round_score = shape_score[winner] + outcome_score[winner]
    return round_score


def solve_part_1(strategy_guide: list[tuple]) -> int:
    """Calculate the total score of an extended game of 'rock, paper, scissors'."""
    score = 0
    for line in strategy_guide:
        score += score_per_round(line)
    print(f"If everything goes exactly according to this strategy guide, my score will be {score}.")
    return score


def solve_part_2(input_data) -> int:
    """Describe the next puzzle."""
    pass


def solution(filename):
    """Play 'rock, paper, scissors' with the elves."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_data(filename)
    strategy_guide = parse_input(raw_data)

    solve_part_1(strategy_guide)
    solve_part_2(strategy_guide)


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
