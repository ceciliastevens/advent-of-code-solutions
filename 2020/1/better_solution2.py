from itertools import combinations
with open("input.txt", "r") as file:
	numbers = [ int(number) for number in file.readlines() ]

print(next(triple[0] * triple[1] * triple[2] for triple in combinations(numbers, 3) if triple[0] + triple[1] + triple[2] == 2020))