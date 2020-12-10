with open("input.txt", "r") as file:
	puzzle_input = [line.strip().split() for line in file.readlines()]

def isPasswordValid(min_count, max_count, substring, password):
	return int(min_count) <= password.count(substring) <= int(max_count)

totalValidPasswords = 0
for password in puzzle_input:
	if isPasswordValid(password[0].split("-")[0], password[0].split("-")[1], password[1].strip(":"), password[2]):
		totalValidPasswords += 1

print(totalValidPasswords)