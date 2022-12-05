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

    def overlaps(self, other: Self) -> Self:
        return self.lo <= other.lo <= self.hi or self.lo <= other.hi <= self.hi


pairs: list[list[str]] = [line.split(",") for line in lines]
pairs: list[tuple[Range, Range]] = [
    (Range.of(pair[0]), Range.of(pair[1])) for pair in pairs
]
overlap_count = sum(fst.overlaps(snd) or snd.overlaps(fst) for fst, snd in pairs)

print(overlap_count)
