from enum import Enum

HAND_SCORE = {"X": 1, "Y": 2, "Z": 3}


class Outcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


matchup_results: dict[tuple[str, str], Outcome] = {
    ("A", "X"): Outcome.DRAW,
    ("A", "Y"): Outcome.WIN,
    ("A", "Z"): Outcome.LOSS,
    ("B", "X"): Outcome.LOSS,
    ("B", "Y"): Outcome.DRAW,
    ("B", "Z"): Outcome.WIN,
    ("C", "X"): Outcome.WIN,
    ("C", "Y"): Outcome.LOSS,
    ("C", "Z"): Outcome.DRAW,
}

with open("input.txt") as f:
    content = f.readlines()

rounds = [line.strip() for line in content]
matchups: list[tuple[str, str]] = [tuple(rnd.split()) for rnd in rounds]

score = sum(
    matchup_results[matchup].value + HAND_SCORE[matchup[1]] for matchup in matchups
)
print(score)
