with open("input.txt", "r") as file:
	puzzle_input = [line.strip().split() for line in file.readlines()]

def isPasswordValid(first_location, second_location, character, password):
	return (password[int(first_location)-1] == character) !=  (password[int(second_location)-1] == character)

totalValidPasswords = 0
for password in puzzle_input:
	if isPasswordValid(password[0].split("-")[0], password[0].split("-")[1], password[1].strip(":"), password[2]):
		totalValidPasswords += 1

print(totalValidPasswords)