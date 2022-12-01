print((sorted_cals := sorted((sum(map(int, calories_indv.split("\n"))) for calories_indv in open("input").read().split("\n\n"))))[-1] + sorted_cals[-2] + sorted_cals[-3])
