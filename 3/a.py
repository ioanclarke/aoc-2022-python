from string import ascii_lowercase, ascii_uppercase
from typing import TypeAlias

strset: TypeAlias = set[str]

priorities = {ch: ord(ch) - ord("a") + 1 for ch in ascii_lowercase} | {
    ch: ord(ch) - ord("A") + 27 for ch in ascii_uppercase
}

with open("input.txt") as f:
    content = f.readlines()

rucksacks: list[str] = [line.strip() for line in content]

compartments: list[tuple[strset, strset]] = [
    (set(rucksack[: len(rucksack) // 2]), set(rucksack[len(rucksack) // 2 :]))
    for rucksack in rucksacks
]

common_items: list[str] = [list(a & b)[0] for a, b in compartments]
total_priorities = sum(priorities[item] for item in common_items)

print(total_priorities)
