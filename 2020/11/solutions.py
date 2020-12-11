from copy import deepcopy

def get_input(filename):
	return [list(line.strip()) for line in open(filename, "r")]

def is_seat(seat_map, x_pos, y_pos):
	# if seat is out of bounds, it is not a seat
	if 0 > x_pos or 0 > y_pos or y_pos >= len(seat_map) or x_pos >= len(seat_map[0]):
		return False
	elif seat_map[y_pos][x_pos] in ['L','#']:
		return True
	return False

def is_seat_occupied(seat_map: list, x_pos: int, y_pos: int):
	return is_seat(seat_map, x_pos, y_pos) and seat_map[y_pos][x_pos] == '#'

def is_seat_available(seat_map: list, x_pos: int, y_pos: int):
	return not is_seat_occupied(seat_map, x_pos, y_pos) and seat_map[y_pos][x_pos] == 'L'

def get_adjacent_seats(seat_map, x_pos, y_pos):
	adjacent_occupied_seat_count = 0
	for y_coordinate in range(y_pos-1, y_pos+2):
		for x_coordinate in range(x_pos-1, x_pos+2):
			if is_seat_occupied(seat_map, x_coordinate, y_coordinate) and not (x_coordinate == x_pos and y_coordinate == y_pos):
				adjacent_occupied_seat_count += 1
	return adjacent_occupied_seat_count


def get_next_seat_state(seat_map: list, x_pos: int, y_pos: int): #assumes it is actually a seat
	if is_seat_available(seat_map, x_pos, y_pos) and get_adjacent_seats(seat_map, x_pos, y_pos) == 0:
		return '#'
	elif seat_map[y_pos][x_pos] == '#' and get_adjacent_seats(seat_map, x_pos, y_pos) >= 4:
		return 'L'
	else:
		return seat_map[y_pos][x_pos]

def get_state(seat_map):
	next_seat_map = deepcopy(seat_map)
	for y_pos in range(len(seat_map)):
		for x_pos in range(len(seat_map[y_pos])):
			if seat_map[y_pos][x_pos] != '.':
				next_seat_map[y_pos][x_pos] = get_next_seat_state(seat_map, x_pos, y_pos)
	return next_seat_map

def count_occupied_seats(seat_map):
	counter = 0
	for row in seat_map:
		for item in row:
			if item == '#':
				counter += 1
	return counter

def print_seat_map(seat_map):
	for row in seat_map:
		print("")
		for item in row:
			print(item, end="")
	print("")
		


if __name__ == '__main__':
	seat_map = get_input("input.txt")

	#puzzle 1 solution
	previous_seat_map = []
	while seat_map != previous_seat_map:
		previous_seat_map = deepcopy(seat_map)
		seat_map = get_state(seat_map)
	print("At first, there are {} occupied seats.".format(count_occupied_seats(seat_map)))