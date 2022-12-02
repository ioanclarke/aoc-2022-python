print(max(sum(map(int, calories_indv.split("\n"))) for calories_indv in open("input").read().split("\n\n")))
