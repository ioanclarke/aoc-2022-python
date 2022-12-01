
with open("input") as f:
	content = f.read()

totals = []

calories_counts = content.split("\n\n")
for counts in calories_counts:
    total = sum(map(int, counts.split("\n")))
    totals.append(total)

totals.sort()
print(totals[-1] + totals[-2] + totals[-3])    
    