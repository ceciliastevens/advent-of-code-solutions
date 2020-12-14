from itertools import product

def get_input(filename):
	output_list = []
	with open(filename, "r") as input_file:
		current_index = -1
		for line in input_file.readlines():
			if line[:3] == "mas":
				current_index+=1
				output_list.append({"mask":line.strip()[7:],"memory_values":[]})
			else:
				parsed_line = line.replace("mem[","").replace("]","").split()
				output_list[current_index]["memory_values"].append((int(parsed_line[0]), int(parsed_line[2])))
	return output_list

def replace_char_in_string(string, char, index):
	return string[:index] + char + string[index+1:]

#my busted interpretation. Not sure why it's broken
def apply_mask(input: int, mask: str) -> int:
	binary_input = bin(input)
	# we need to extend with leading zeroes if the binary is too short
	while len(binary_input) - 2 < len(mask):
		binary_input = '0b0' + binary_input[2:]
	for index in range(2, len(binary_input)-1):
		current_index = -index
		if mask[current_index] != 'X':
			binary_input = replace_char_in_string(binary_input, mask[current_index], current_index)
	try:
		return int(binary_input, 2)
	except Exception as e:
		print("input: {}".format(input))
		print("mask: {}".format(mask))
		raise e

def write_to_memory(memory: tuple, address: int, value: int, mask: str) -> tuple:
	memory[address] = apply_mask(value, mask)
	return memory

def initialize_memory():
	return dict()

def sum_memory(memory):
	return sum([memory[key] for key in memory.keys()])


# better solutions from https://github.com/maarten-dp/adventofcode2020/blob/master/solvers/day14.py
class Mask:
    def __init__(self, mask):
        self.or_mask = int(mask.replace('X', '0'), 2)
        self.and_mask = int(mask.replace('X', '1'), 2)

    def apply(self, val):
        val |= self.or_mask
        val &= self.and_mask
        return val


class AddressDecoder:
    def __init__(self, mask):
        self.masks = []
        self.or_mask = int(mask.replace('X', '0'), 2)
        template = mask.replace('X', '{}').replace('0', 'X').replace('1', 'X')
        variations = mask.count('X')
        for perm in product('01', repeat=variations):
            self.masks.append(Mask(template.format(*perm)))

    def apply(self, val):
        to_write = []
        val |= self.or_mask
        for mask in self.masks:
            to_write.append(mask.apply(val))
        return to_write


if __name__ == "__main__":
	puzzle_input = get_input("input.txt")

	#puzzle1 solution
	memory = initialize_memory()
	for mask_and_values in puzzle_input:
		current_mask = Mask(mask_and_values["mask"])
		for memory_application in mask_and_values["memory_values"]:
			memory[memory_application[0]] = current_mask.apply(memory_application[1])
	print(sum_memory(memory))

	#puzzle2 solution
	memory = initialize_memory()
	decoder = None
	for mask_and_values in puzzle_input:
		decoder = AddressDecoder(mask_and_values["mask"])
		for memory_application in mask_and_values["memory_values"]:
			for application in decoder.apply(memory_application[0]):
				memory[application] = memory_application[1]

	print(sum_memory(memory))