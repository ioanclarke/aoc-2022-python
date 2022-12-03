from enum import Enum

HAND_SCORE = {"X": 1, "Y": 2, "Z": 3}


class Outcome(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


matchup_results: dict[tuple[str, str], tuple[Outcome, str]] = {
    ("A", "X"): (Outcome.LOSS, "Z"),
    ("A", "Y"): (Outcome.DRAW, "X"),
    ("A", "Z"): (Outcome.WIN, "Y"),
    ("B", "X"): (Outcome.LOSS, "X"),
    ("B", "Y"): (Outcome.DRAW, "Y"),
    ("B", "Z"): (Outcome.WIN, "Z"),
    ("C", "X"): (Outcome.LOSS, "Y"),
    ("C", "Y"): (Outcome.DRAW, "Z"),
    ("C", "Z"): (Outcome.WIN, "X"),
}
with open("input.txt") as f:
    rounds = f.readlines()

rounds = map(str.strip, rounds)
matchups = [tuple(rnd.split()) for rnd in rounds]

score = sum(
    (result := matchup_results[matchup])[0].value + HAND_SCORE[result[1]]
    for matchup in matchups
)

print(score)
