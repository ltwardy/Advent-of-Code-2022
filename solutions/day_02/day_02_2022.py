# Advent of Code 2022
# Day 02: Rock Paper Scissors

import sys

sys.path.append("../")
from ..shared_functions import fetch_string_data


def parse_input(raw_input: list) -> list[tuple]:
    """Reformat the puzzle input to make it easier to handle."""
    strategy_guide = []
    for line in raw_input:
        elf, me = line.split()
        elf_choices = {"A": "Rock", "B": "Paper", "C": "Scissors"}
        my_choices = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}
        strategy_guide.append((elf_choices[elf], my_choices[me]))
    return strategy_guide


def correct_input(wrong_input: list[tuple]) -> list[tuple]:
    """Update my puzzle input to reflect a new interpretation of symbols."""
    correct_guide = []
    update = {"Rock": "lose", "Paper": "draw", "Scissors": "win"}
    for line in wrong_input:
        correct_guide.append((line[0], update[line[1]]))
    return correct_guide


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
    round_score = shape_score[move_pair[1]] + outcome_score[winner]
    return round_score


def calculate_move(opponent, strategy) -> str:
    """Decode the secret strategy to choose my next move in 'rock, paper, scissors'. """
    if strategy == "draw":
        move = opponent
    elif strategy == "win":
        winning_move = {"Scissors": "Rock", "Paper": "Scissors", "Rock": "Paper"}
        move = winning_move[opponent]
    else:
        losing_move = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
        move = losing_move[opponent]
    return move


def solve_part_1(strategy_guide: list[tuple]) -> int:
    """Calculate the total score of a game, based on my interpretation of the strategy guide."""
    score = 0
    for line in strategy_guide:
        score += score_per_round(line)
    return score
    # 15422 was correct! Gold star! This took a little longer, than yesterday, but I'm happy with my work.


def solve_part_2(strategy_guide) -> int:
    """Describe the total score of a game, based on the elf's interpretation of their guide."""
    strategy_guide = correct_input(strategy_guide)
    score = 0
    for line in strategy_guide:
        elf_move, strategy = line
        my_move = calculate_move(elf_move, strategy)
        score += score_per_round((elf_move, my_move))
    return score
    # 15442 is correct! Another gold star!
    # It occurs to me that a more streamlined solver function could be made from an ordered list of moves,
    # with the winning/losing move found by increasing/decreasing the index via a modulo operator.
    # Oh, well.  Maybe I'll write that solution later for fun.


def solution(filename):
    """Play 'rock, paper, scissors' with the elves."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_string_data(filename)
    strategy_guide = parse_input(raw_data)

    score1 = solve_part_1(strategy_guide)
    print(f"If everything goes exactly according to this strategy guide, my score will be {score1}.")

    print("But I see that I've misunderstood the problem.  Let me try again.")
    score2 = solve_part_2(strategy_guide)
    print(f"If everything goes exactly according to this strategy guide, my score will be {score2}.")


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
