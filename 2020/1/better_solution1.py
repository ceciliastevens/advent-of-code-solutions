from itertools import combinations
with open("input.txt", "r") as file:
	numbers = [ int(number) for number in file.readlines() ]

print(next(pair[0] * pair[1] for pair in combinations(numbers, 2) if pair[0] + pair[1] == 2020))