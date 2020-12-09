from itertools import combinations

def get_input(filename):
	return [int(line.strip()) for line in open(filename, "r")]

def find_first_failure(sequence, preamble_length):
	for index in range(preamble_length, len(sequence)):
		preamble = set(sequence[index-preamble_length:index])
		if sequence[index] not in [sum(combination) for combination in combinations(preamble, 2)]:
			return sequence[index]

def find_sum_range(sequence, target):
	for starting_point in range(len(sequence)):
		contiguous_set = set()
		current_index = starting_point
		while sum(contiguous_set) < target:
			contiguous_set.add(sequence[current_index])
			current_index += 1
		if sum(contiguous_set) == target and len(contiguous_set) > 1:
			return min(contiguous_set) + max(contiguous_set)


if __name__ == "__main__":
	preamble_length = 25
	sequence = get_input("input.txt")

	# part 1 solution
	failure = find_first_failure(sequence, preamble_length)
	print("The first number that is not a sum of two of the {} previous numbers is {}".format(preamble_length, failure))

	#part 2 solution
	print("The sum of the minimum and maximum of the contiguous set of two or more numbers summing up to {} is {}".format(failure, find_sum_range(sequence, failure)))