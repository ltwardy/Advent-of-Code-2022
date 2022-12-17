# Advent of Code 2022
# Day 09: Rope Bridge

from dataclasses import dataclass
import sys
from math import sqrt

sys.path.append("../")
from shared_functions import *


@dataclass
class Rope:
    head_x: int = 0
    head_y: int = 0
    tail_x: int = 0
    tail_y: int = 0

    @property
    def head(self):
        return self.head_x, self.head_y

    @property
    def tail(self):
        return self.tail_x, self.tail_y

    @property
    def length(self):
        return sqrt((self.head_x - self.tail_x) ** 2 + (self.head_y - self.tail_y) ** 2)

    def move_head(self, direction):
        old_head = (self.head_x, self.head_y)
        if direction == "U":
            self.head_x += 1
        elif direction == "D":
            self.head_x -= 1
        elif direction == "R":
            self.head_y += 1
        elif direction == "L":
            self.head_y -= 1
        else:
            print(f"Invalid direction {direction}")

        if self.length > sqrt(0.5):
            self.tail_x, self.tail_y = old_head


def parse(raw_data: list):
    """Make our input more useful for problem-solving."""
    instructions = []
    for line in raw_data:
        line = line.split()
        print(line)
        direction, moves = line
        instructions.append((direction, int(moves)))
    return instructions


def solve_part_1(instructions):
    """Find all the points visited by the tail of the rope."""
    my_rope = Rope()
    tail_track = []
    tail_track.append(my_rope.tail)

    for (direction, moves) in instructions:
        for _repeat in range(moves):
            my_rope.move_head(direction)
            tail_track.append(my_rope.tail)
            print(my_rope)

    points_visited = len(set(tail_track))
    return points_visited


def solve_part_2(input_data):
    """Describe the next puzzle."""
    pass


def solution(filename):
    """Simulate the movement of tiny, somewhat-elastic ropes."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_raw_data(filename)
    string_movement = parse(raw_data)

    number_of_points = solve_part_1(string_movement)
    print(f"The tail of the rope visits {number_of_points} different locations.")

    solve_part_2(string_movement)


# This can be run as a script from the command line, with data filename as argument.
# if __name__ == "__main__":
#     import sys
#
#     try:
#         arg = sys.argv[1]
#     except IndexError:
#         raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")
#
#     print(f"Data file = '{arg}'.")  # debug
#     solution(arg)

solution("testing.txt")
