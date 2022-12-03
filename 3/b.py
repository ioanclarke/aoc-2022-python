from string import ascii_lowercase, ascii_uppercase
from typing import TypeAlias

strset: TypeAlias = set[str]

priorities = {ch: ord(ch) - ord("a") + 1 for ch in ascii_lowercase} | {
    ch: ord(ch) - ord("A") + 27 for ch in ascii_uppercase
}

with open("input.txt") as f:
    content = f.readlines()

rucksacks: list[str] = [line.strip() for line in content]

rucksack_triplets: list[tuple[strset, strset, strset]] = [
    (set(rucksacks[i]), set(rucksacks[i + 1]), set(rucksacks[i + 2]))
    for i in range(0, len(rucksacks), 3)
]

common_items: list[str] = [list(a & b & c)[0] for a, b, c in rucksack_triplets]
total_priorities = sum(priorities[item] for item in common_items)

print(total_priorities)
