import re
from typing import NamedTuple
from copy import deepcopy


def build_stack(n: int, rows: list[str]):
    pos = (3 * n) + n + 1
    stack = []
    for row in rows[:-1]:
        stack.insert(0, row[pos])
    return [el for el in stack if el != " "]


class Instruction(NamedTuple):
    src: int
    dest: int
    amount: int


def parse_inst_inp(inst_inp: str) -> list[Instruction]:
    insts = []
    for inst in inst_inp.splitlines():
        res = re.search(r"move (\d+) from (\d) to (\d)", inst)
        insts.append(
            Instruction(src=int(res.group(2)) - 1, dest=int(res.group(3)) - 1, amount=int(res.group(1)))
        )
    return insts


def perform(stacks: list[list[str]], insts: list[Instruction]) -> list[list[str]]:
    for src, dest, amount in insts:
        print(f"{src=} {dest=} {amount=}")
        src_stack = stacks[src]
        dest_stack = stacks[dest]
        crates = src_stack[-amount:]
        src_stack = src_stack[:-amount]
        dest_stack = dest_stack + crates

        stacks[src] = src_stack
        stacks[dest] = dest_stack
        # print(f"{crates=}")

        # for _ in range(amount):
        #     elem = src_stack.pop()
        #     dest_stack.append(elem)
        # for stack in stacks:
        #     print(stack)
    return stacks


def main():
    with open("input.txt") as f:
        content = f.read()

    stacks_inp, inst_inp = content.split("\n\n")
    rows = stacks_inp.split("\n")
    for row in rows:
        print(row)

    # hard-coded number of stacks. not great
    num_of_stacks = 9
    # print(f"building {num_of_stacks} stacks...")
    # if input stacks are 1..9, we label them as 0..8
    stacks: list[list[str]] = [build_stack(i, rows) for i in range(0, num_of_stacks)]
    instructions: list[Instruction] = parse_inst_inp(inst_inp)

    stacks = perform(deepcopy(stacks), instructions)
    # for stack in stacks:
    #     print(stack)

    tops = "".join([stack[-1] for stack in stacks])
    # tops = ""
    # for stack in stacks:
    #     if len(stack) > 0:
    #         tops += stack[-1]
    print(tops)


main()

# WNTFTZNTT wrong
