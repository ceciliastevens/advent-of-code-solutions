# take input
terrain_map = [ list(line.strip()) for line in open("input.txt","r")]

#define a function to calculate the trees
def how_many_trees(x_slope, y_slope, terrain_map):
	x_position = 0
	y_position = 0
	trees_encountered = 0
	while y_position < len(terrain_map):
		if terrain_map[y_position][x_position % len(terrain_map[y_position])] == '#':
			trees_encountered += 1
		x_position += x_slope
		y_position += y_slope
	return trees_encountered

#puzzle 1 solution
print("Solution 1: You will encounter {} trees.".format(how_many_trees(3, 1, terrain_map)))

#puzzle 2 solution
print("Solution 2: The multiple is: {}".format(
	how_many_trees(1,1, terrain_map) * 
	how_many_trees(3,1, terrain_map) * 
	how_many_trees(5,1,terrain_map) *
	how_many_trees(7,1,terrain_map) *
	how_many_trees(1,2, terrain_map)
	))