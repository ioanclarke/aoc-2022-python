from enum import Enum
from typing import NamedTuple, Callable, TypeAlias


class Position(NamedTuple):
    x: int
    y: int


class Direction(Enum):
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"


class Instruction(NamedTuple):
    direction: Direction
    steps: int


StepHandler: TypeAlias = Callable[[Position, Position], tuple[Position, Position]]


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    insts = parse_input(lines)
    num_of_visited_positions = len(simulate(insts))

    print(num_of_visited_positions)


def parse_input(lines: list[str]) -> list[Instruction]:
    return [
        Instruction(Direction(direction), int(steps))
        for direction, steps in (line.split() for line in lines)
    ]


def simulate(insts: list[Instruction]) -> set[Position]:
    visited_positions: set[Position] = {Position(0, 0)}
    h_pos = Position(0, 0)
    t_pos = Position(0, 0)
    for direction, steps in insts:
        match direction:
            case Direction.UP:
                step_handler = handle_up_step
            case Direction.RIGHT:
                step_handler = handle_right_step
            case Direction.DOWN:
                step_handler = handle_down_step
            case Direction.LEFT:
                step_handler = handle_left_step
        h_pos, t_pos, positions = handle_instruction(h_pos, t_pos, steps, step_handler)
        visited_positions |= positions
    return visited_positions


def handle_instruction(
    h_pos: Position, t_pos: Position, steps: int, handle_step: StepHandler
) -> tuple[Position, Position, set[Position]]:
    visited_positions = set()
    for _ in range(steps):
        h_pos, t_pos = handle_step(h_pos, t_pos)
        visited_positions.add(t_pos)
    return h_pos, t_pos, visited_positions


def handle_up_step(h_pos: Position, t_pos: Position) -> tuple[Position, Position]:
    if t_pos.y == h_pos.y + 1:
        if t_pos.x == h_pos.x - 1:
            t_pos = Position(t_pos.x + 1, t_pos.y - 1)
        elif t_pos.x == h_pos.x:
            t_pos = Position(t_pos.x, t_pos.y - 1)
        elif t_pos.x == h_pos.x + 1:
            t_pos = Position(t_pos.x - 1, t_pos.y - 1)

    h_pos = Position(h_pos.x, h_pos.y - 1)

    return h_pos, t_pos


def handle_right_step(h_pos: Position, t_pos: Position) -> tuple[Position, Position]:
    if t_pos.x == h_pos.x - 1:
        if t_pos.y == h_pos.y - 1:
            t_pos = Position(t_pos.x + 1, t_pos.y + 1)
        elif t_pos.y == h_pos.y:
            t_pos = Position(t_pos.x + 1, t_pos.y)
        elif t_pos.y == h_pos.y + 1:
            t_pos = Position(t_pos.x + 1, t_pos.y - 1)

    h_pos = Position(h_pos.x + 1, h_pos.y)

    return h_pos, t_pos


def handle_down_step(h_pos: Position, t_pos: Position) -> tuple[Position, Position]:
    if t_pos.y == h_pos.y - 1:
        if t_pos.x == h_pos.x - 1:
            t_pos = Position(t_pos.x + 1, t_pos.y + 1)
        elif t_pos.x == h_pos.x:
            t_pos = Position(t_pos.x, t_pos.y + 1)
        elif t_pos.x == h_pos.x + 1:
            t_pos = Position(t_pos.x - 1, t_pos.y + 1)

    h_pos = Position(h_pos.x, h_pos.y + 1)

    return h_pos, t_pos


def handle_left_step(h_pos: Position, t_pos: Position) -> tuple[Position, Position]:
    if t_pos.x == h_pos.x + 1:
        if t_pos.y == h_pos.y - 1:
            t_pos = Position(t_pos.x - 1, t_pos.y + 1)
        elif t_pos.y == h_pos.y:
            t_pos = Position(t_pos.x - 1, t_pos.y)
        elif t_pos.y == h_pos.y + 1:
            t_pos = Position(t_pos.x - 1, t_pos.y - 1)

    h_pos = Position(h_pos.x - 1, h_pos.y)
    return h_pos, t_pos


main()
