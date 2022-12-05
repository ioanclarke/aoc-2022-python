from typing import NamedTuple
from typing import Self

with open("input.txt") as f:
    lines = f.read().splitlines()


class Range(NamedTuple):
    lo: int
    hi: int

    @staticmethod
    # rnge is of the form "a-b"
    def of(rnge: str) -> Self:
        return Range(*map(int, rnge.split("-")))

    def contains(self, other: Self) -> Self:
        return self.lo <= other.lo and self.hi >= other.hi


pairs: list[list[str]] = [line.split(",") for line in lines]
pairs: list[tuple[Range, Range]] = [
    (Range.of(pair[0]), Range.of(pair[1])) for pair in pairs
]
overlap_count = sum(fst.contains(snd) or snd.contains(fst) for fst, snd in pairs)

print(overlap_count)
