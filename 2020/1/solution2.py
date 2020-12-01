with open("input.txt", "r") as file:
	numbers = file.readlines()

for number1 in numbers:
	for number2 in numbers:
		for number3 in numbers:
			if(int(number1) + int(number2) + int(number3) == 2020):
				solution = int(number1) * int(number2) * int(number3)
				print(solution)
				exit()