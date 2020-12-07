def parse_rule(rule: str):
	#first, split on contains. This gives us the strings "adjective color bags" and a comma-separated list of contents
	bag_type, contents = rule.split("contain")
	# next, split contents on ',' to get a list of others
	contents = contents.split(",")
	return {remove_bags_from_string(bag_type): {remove_bags_from_string(bag_type)[2:]: remove_bags_from_string(bag_type)[:1] for bag_type in contents}}

def remove_bags_from_string(string):
	return string.replace("no other bags.","").replace("bags", "").replace("bag", "").replace(".","").strip()

def get_input(filename):
	with open(filename, "r") as input_file:
		rules_dict = dict()
		for line in input_file.readlines():
			rules_dict.update(parse_rule(line))
	return rules_dict


def is_there_a_path(current: str, target: str, visited: set, graph: dict):
	visited.add(current),
	if target in graph[current].keys():
		return True
	else:
		for contents_item in graph[current]:
			if contents_item not in visited and contents_item != '':
				if is_there_a_path(contents_item, target, visited, graph):
					return True
	return False

def get_total_bags(contents, rules):
	contents.pop("", None) #clear out nulls
	total = 0
	for bag in contents.keys():
		#print("adding {} bags of type {}".format(contents[bag], bag))
		total+=int(contents[bag])
		if bag != '':
			#print("adding the contents of {} which should be {} * {}".format(bag, get_total_bags(rules[bag], rules), contents[bag]))
			total+= (get_total_bags(rules[bag], rules) * int(contents[bag])) #this has problems
	#print("returning {}".format(total))
	return total
	


if __name__ == "__main__":
	rules = get_input("input.txt")
	#part 1 solution
	bags_that_contain_shiny_gold = set()
	for bag_type in rules.keys():
		if is_there_a_path(bag_type, "shiny gold", set(), rules):
			bags_that_contain_shiny_gold.add(bag_type)
	print(len(bags_that_contain_shiny_gold))

	#part 2
	print(get_total_bags(rules["shiny gold"], rules))