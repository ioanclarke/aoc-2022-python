HAND_SCORE = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

OUTCOME_SCORE = {
    "loss": 0,
    "draw": 3,
    "win": 6
}

with open("input.txt") as f:
    rounds = f.readlines()

rounds = map(str.strip, rounds)
round_pairs = [round.split() for round in rounds]

score = 0
for fst, snd in round_pairs:
    match fst, snd:
        case "A", "X":
            outcome = "loss"
            hand = "Z"

        case "A", "Y":
            outcome = "draw"
            hand = "X"

        case "A", "Z":
            outcome = "win"
            hand = "Y"

        case "B", "X":
            outcome = "loss"
            hand = "X"

        case "B", "Y":
            outcome = "draw"
            hand = "Y"

        case "B", "Z":
            outcome = "win"
            hand = "Z"

        case "C", "X":
            outcome = "loss"
            hand = "Y"

        case "C", "Y":
            outcome = "draw"
            hand = "Z"

        case "C", "Z":
            outcome = "win"
            hand = "X"
    score += OUTCOME_SCORE[outcome]
    score += HAND_SCORE[hand]

print(score)
