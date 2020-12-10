ROW_SLICE = 7

def get_half(space: list, key: list, upper_half_indicator: str):
    if len(key) == 1:
        #print("returning {}".format(space[-1] if key[0] == upper_half_indicator else space[-1]))
        return space[-1] if key[0] == upper_half_indicator else space[0]
    else:
        #print("returning half of {}, which is {}".format(space,
        #space[len(space) // 2:] if key[0] == upper_half_indicator else space[:len(space) // 2]))
        return get_half(
            space[len(space) // 2:] if key[0] == upper_half_indicator else space[:len(space) // 2],
            key[1:],
            upper_half_indicator            
        )

def get_seat_id(row, column, multiplier):
    return row * multiplier + column

with open("input.txt", "r") as input_file:
    puzzle_input = [line.strip() for line in input_file.readlines()]


max_id = 0
all_seat_ids = []
for ticket in puzzle_input:
    row = get_half(range(128), ticket[:ROW_SLICE], "B")
    column = get_half(range(8), ticket[ROW_SLICE:], "R")
    
    all_seat_ids.append(get_seat_id(row, column, 8))
    if get_seat_id(row, column, 8) > max_id:
        max_id = get_seat_id(row, column, 8)


print("Puzzle 1 solution: {}".format(max_id))

print("Puzzle 2 solution: {}".format(max([seat for seat in range(max(all_seat_ids)+1) if seat not in all_seat_ids]))) #this is such bad code oh my god