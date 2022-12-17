# Advent of Code 2022
# Day 09: Rope Bridge

from dataclasses import dataclass
import sys
from math import copysign

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
            self.head_y += 1
        elif direction == "D":
            self.head_y -= 1
        elif direction == "R":
            self.head_x += 1
        elif direction == "L":
            self.head_x -= 1
        else:
            print(f"Invalid direction {direction}")

        if self.length > sqrt(2):
            self.tail_x, self.tail_y = old_head


class LongRope:

    def __init__(self):
        self.body = [(0, 0) for _n in range(10)]
        # self.body = [(0, 0) for _n in range(2)]     # can we get the same answer as part 1? yes, after some work

    @property
    def tail(self):
        return self.body[-1]

    @property
    def head(self):
        return self.body[0]

    def move_head(self, direction):
        translate = {"U": (0, 1),
                     "D": (0, -1),
                     "R": (1, 0),
                     "L": (-1, 0)}
        move_x, move_y = translate[direction]
        new_body = [(self.head[0] + move_x, self.head[1] + move_y)]
        for i in range(len(self.body)):
            if i == 0:
                continue
            if distance(*self.body[i], *new_body[i - 1]) <= sqrt(2):
                new_body.append(self.body[i])
            else:
                x1, y1 = self.body[i]
                x2, y2 = new_body[i - 1]
                delta_x = x2 - x1
                delta_y = y2 - y1
                if delta_x == 0:
                    new_x = x1
                    new_y = y1 + copysign(1, y2 - y1)
                elif delta_y == 0:
                    new_x = x1 + copysign(1, x2 - x1)
                    new_y = y1
                else:
                    new_x = x1 + copysign(1, x2 - x1)
                    new_y = y1 + copysign(1, y2 - y1)
                new_body.append((new_x, new_y))
        self.body = new_body


def parse(raw_data: list):
    """Make our input more useful for problem-solving."""
    instructions = []
    for line in raw_data:
        direction, moves = line.split()
        instructions.append((direction, int(moves)))
    return instructions


def solve_part_1(instructions):
    """Find all the points visited by the tail of the rope."""
    my_rope = Rope()
    tail_track = [my_rope.tail]

    for (direction, moves) in instructions:
        for _repeat in range(moves):
            my_rope.move_head(direction)
            tail_track.append(my_rope.tail)
    points_visited = len(set(tail_track))
    return points_visited
    # yay! it works! Gold star!


def solve_part_2(instructions):
    """Find all the points visited by the tail of a ten-segment rope."""
    my_rope = LongRope()
    tail_track = [my_rope.tail]
    for (direction, moves) in instructions:
        for _repeat in range(moves):
            my_rope.move_head(direction)
            tail_track.append(my_rope.tail)
    points_visited = len(set(tail_track))
    return points_visited
    # Yay! Another gold star!


def solution(filename):
    """Simulate the movement of tiny, somewhat-elastic ropes."""
    # process data from filename to make it usable by our solving functions
    raw_data = fetch_raw_data(filename)
    string_movement = parse(raw_data)

    tail_movement = solve_part_1(string_movement)
    print(f"The tail of the rope visits {tail_movement} different locations.")

    print("Oh no! A rope from the bridge snapped and is whipping around you as you fall!")
    longer_tail_movement = solve_part_2(string_movement)
    print(f"The end of the long rope will visit {longer_tail_movement} different locations.")


# This can be run as a script from the command line, with data filename as argument.
if __name__ == "__main__":
    import sys

    try:
        arg = sys.argv[1]
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <data file for this puzzle>")

    print(f"Data file = '{arg}'.")  # debug
    solution(arg)
