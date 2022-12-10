import sys
from enum import Enum
from typing import NamedTuple


class Direction(Enum):
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"

    @staticmethod
    def from_str(label: str):
        match label:
            case "U":
                return Direction.UP
            case "R":
                return Direction.RIGHT
            case "D":
                return Direction.DOWN
            case "L":
                return Direction.LEFT


class Instruction(NamedTuple):
    direction: Direction
    steps: int


def main():
    with open("test.txt") as f:
        lines = f.read().splitlines()

    insts = parse_input(lines)
    num_of_visited_positions = len(simulate(insts))

    print(num_of_visited_positions)


def parse_input(lines: list[str]) -> list[Instruction]:
    return [
        Instruction(Direction.from_str(direction), int(steps))
        for direction, steps in (line.split() for line in lines)
    ]


class Position(NamedTuple):
    x: int
    y: int


def simulate(insts: list[Instruction]) -> list[Position]:
    visited_positions: list[Position] = []
    h_pos = Position(0, 0)
    t_pos = Position(0, 0)
    for direction, steps in insts:
        print(f"{direction=}")
        print(f"{steps=}")
        match direction:
            case Direction.UP:
                # if t_pos == h_pos:
                #     pass
                # if t_pos.x == h_pos.x and t_pos.y == h_pos.y - 1:
                #     pass
                # if t_pos.x == h_pos.x + 1 and t_pos.y == h_pos.y - 1:
                #     pass
                if t_pos.y == h_pos.y + 1:
                    if t_pos.x == h_pos.x - 1:
                        t_pos = Position(t_pos.x + 1, t_pos.y - 1)
                    elif t_pos.x == h_pos.x:
                        t_pos = Position(t_pos.x, t_pos.y - 1)
                    elif t_pos.x == h_pos.x + 1:
                        t_pos = Position(t_pos.x - 1, t_pos.y - 1)
                    else:
                        print("SOMETHING HAS GONE HORRIBLY WRONG")
                        sys.exit(1)
                h_pos = Position(h_pos.x, h_pos.y - steps)
            case Direction.RIGHT:
                if t_pos.x == h_pos.x - 1:
                    """
                    T..
                    .H.
                    ...
                    """
                    if t_pos.y == h_pos.y - 1:
                        t_pos = Position(t_pos.x + 1, t_pos.y + 1)
                        """
                        ...
                        TH.
                        ...
                        """
                    elif t_pos.y == h_pos.y:
                        t_pos = Position(t_pos.x + 1, t_pos.y)
                        """
                        ...
                        .H.
                        T..
                        """
                    elif t_pos.y == h_pos.y + 1:
                        t_pos = Position(t_pos.x + 1, t_pos.y - 1)


                h_pos = Position(h_pos.x + steps, h_pos.y)
            case Direction.DOWN:
                h_pos = Position(h_pos.x, h_pos.y + steps)
            case Direction.LEFT:
                h_pos = Position(h_pos.x - steps, h_pos.y)
        print(h_pos)
        print()
    return visited_positions


main()
