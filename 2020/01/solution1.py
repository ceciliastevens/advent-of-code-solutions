with open("input.txt", "r") as file:
	numbers = file.readlines()

for number in numbers:
	for multiplier in numbers:
		if(int(number) + int(multiplier) == 2020):
			solution = int(number) * int(multiplier)
			print(solution)
			exit()