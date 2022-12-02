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
    score += HAND_SCORE[snd]
    match fst, snd:
        case "A", "X":
            outcome = "draw"
        case "A", "Y":
            outcome = "win"
        case "A", "Z":
            outcome = "loss"
        case "B", "X":
            outcome = "loss"
        case "B", "Y":
            outcome = "draw"
        case "B", "Z":
            outcome = "win"
        case "C", "X":
            outcome = "win"
        case "C", "Y":
            outcome = "loss"
        case "C", "Z":
            outcome = "draw"
    score += OUTCOME_SCORE[outcome]

print(score)
