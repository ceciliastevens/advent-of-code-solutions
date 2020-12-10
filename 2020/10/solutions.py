def get_input(filename):
	return {int(adapter) for adapter in open(filename, "r")}

def count_joltage_differences(set_of_adapter_joltages, outlet_joltage, device_input_joltage):
	current_joltage = outlet_joltage
	set_of_adapter_joltages.add(device_input_joltage)
	joltage_differences = {1:0,3:0}
	for adapter in sorted(set_of_adapter_joltages):
		if current_joltage >= adapter - 3:
			joltage_differences[adapter - current_joltage] += 1
			current_joltage = adapter
		else:
			raise Exception("No available adapter.")
	return joltage_differences

def find_all_possible_joltage_paths(set_of_adapter_joltages, outlet_joltage, device_input_joltage):
	set_of_adapter_joltages.add(outlet_joltage)
	set_of_adapter_joltages.add(device_input_joltage)
	number_of_paths = 0
	list_of_joltages = sorted(set_of_adapter_joltages)
	
	def get_paths(current_list_of_joltages): # I can't take credit for this, I had to look it up. I was still trying to actually calculate all the sets instead of just how many there were
		if len(current_list_of_joltages) == 0:
			return 0 # no paths exist
		if len(current_list_of_joltages) < 3:
			return 1 # only one possible path exists
		current_paths = 0
		current_paths += get_paths(current_list_of_joltages[1:]) 
		current_paths += get_paths(current_list_of_joltages[2:])
		current_paths += get_paths(current_list_of_joltages[3:]) #try dropping the first few
		return current_paths # int of how many paths we got

	start = 0
	paths = 1
	for index in range(len(list_of_joltages)):
		current_joltage = list_of_joltages[index]
		if list_of_joltages[index - 1] + 3 == current_joltage:
			paths_to_here = get_paths(list_of_joltages[start:index])
			paths *= paths_to_here # this is the smart bit, where they multiply by how many paths there could be without knowing exactly the details of every path
			start = index

	return paths



if __name__ == "__main__":
	set_of_adapter_joltages = get_input("input.txt")
	outlet_joltage = 0
	device_input_joltage = max(set_of_adapter_joltages) + 3
	count_of_joltage_differences = count_joltage_differences(set_of_adapter_joltages, outlet_joltage, device_input_joltage)
	#solution 1
	print(count_of_joltage_differences[1] * count_of_joltage_differences[3])

	#solution 2
	print(find_all_possible_joltage_paths(set_of_adapter_joltages, outlet_joltage, device_input_joltage))

