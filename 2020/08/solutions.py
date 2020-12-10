def execute_program(program):
	accumulator = 0
	location = 0
	visited = set()
	while location != len(program) and location not in visited:
		visited.add(location)
		if program[location]["instruction"] == "acc":
			accumulator += program[location]["value"]
			location += 1
		elif program[location]["instruction"] == "jmp":
			location += program[location]["value"]
		elif program[location]["instruction"] == "nop":
			location += 1
		else:
			raise Exception("Illegal instruction")
	return (accumulator, location)

def get_input(filename):
	with open(filename, "r") as input_file:
		return [{"instruction":line.strip().split()[0], "value": int(line.strip().split()[1])} for line in input_file.readlines()]
	
def repair_program(program):
	for instruction in program:
		current_index = program.index(instruction)
		test_program = [instruction.copy() for instruction in program]
		if instruction["instruction"] == "jmp":
			test_program[current_index]["instruction"] = "nop"
		if instruction["instruction"] == "nop":
			test_program[current_index]["instruction"] = "jmp"
		accumulator, location = execute_program(test_program)
		if location == len(program):
			return accumulator



if __name__ == "__main__":
	program = get_input("input.txt")

	#puzzle 1 solution
	try:
		accumulator, instruction = execute_program(program)
		print("The program encountered an infinite loop after instruction {}: {}. The accumulator's value is {}.".format(instruction, program[instruction], accumulator))
	except Exception as e:
		print(e)

	print("After fixing the program, the accumulator is {}".format(repair_program(program)))
	

