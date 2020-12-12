def get_input(filename):
    return [(instruction[0], int(instruction[1:])) for instruction in open(filename, "r")]

def get_manhattan_distance(north_south_pos: int, east_west_pos: int):
    return abs(north_south_pos) + abs(east_west_pos)

DIRECTIONS = ["N","E","S","W"]

def turn_ship(direction, current_heading, degrees):
    steps = int(degrees) // 90
    current_heading = DIRECTIONS.index(current_heading) #get a number
    if direction == 'R':
        current_heading += steps
    elif direction == 'L':
        current_heading -= steps
    else:
        raise Exception("illegal turn direction")
    return DIRECTIONS[current_heading % 4]

def move_ship(north_south_pos, east_west_pos, direction, current_heading, steps):
    if direction == 'F':
        # if we're going forward, direction is actually current heading
        return move_ship(north_south_pos, east_west_pos, current_heading, current_heading, steps)        
    elif direction == 'N':
        return north_south_pos + steps, east_west_pos
    elif direction == 'S':
        return north_south_pos - steps, east_west_pos
    elif direction == 'E':
        return north_south_pos, east_west_pos + steps
    elif direction == 'W':
        return north_south_pos, east_west_pos - steps
    else:
        raise Exception("Illegal go direction")

def move_to_waypoint(north_south_pos, east_west_pos, waypoint_ns_pos, waypoint_ew_pos, number_of_moves):
    return north_south_pos + (waypoint_ns_pos * number_of_moves), east_west_pos + (waypoint_ew_pos * number_of_moves)


def rotate_waypoint_one_step(waypoint_ns_pos, waypoint_es_pos, direction):
    if direction == 'R':
        return -waypoint_es_pos, waypoint_ns_pos
    elif direction == 'L':
        return waypoint_es_pos, -waypoint_ns_pos
    else:
        raise Exception("Illegal waypoint rotation: {}".format(direction))

def rotate_waypoint(waypoint_ns_pos, waypoint_es_pos, direction, steps):
    for step in range(steps // 90):
        waypoint_ns_pos, waypoint_es_pos = rotate_waypoint_one_step(waypoint_ns_pos, waypoint_es_pos, direction)
    return waypoint_ns_pos, waypoint_es_pos


if __name__== "__main__":
    instructions = get_input("input.txt")

    facing = "E"
    north_south_pos = 0
    east_west_pos = 0

    # puzzle 1 solution
    for heading, steps in instructions:
        if heading in ['L','R']:
            facing = turn_ship(heading, facing, steps)
        else:
            north_south_pos, east_west_pos = move_ship(north_south_pos, east_west_pos, heading, facing, steps)
#        print("facing: {}, n-s: {}, e-w: {}, manhattan: {}".format(facing, north_south_pos, east_west_pos, get_manhattan_distance(north_south_pos, east_west_pos)))
    print("The manhattan distance is {}".format(get_manhattan_distance(north_south_pos, east_west_pos)))

    #puzzle 2
    waypoint_ns_pos = 1
    waypoint_ew_pos = 10
    north_south_pos = 0
    east_west_pos = 0

    for heading, steps in instructions:
        if heading in ['L','R']:
            waypoint_ns_pos, waypoint_ew_pos = rotate_waypoint(waypoint_ns_pos, waypoint_ew_pos, heading, steps)
        elif heading in DIRECTIONS:
            waypoint_ns_pos, waypoint_ew_pos = move_ship(waypoint_ns_pos, waypoint_ew_pos, heading, "", steps)
        else:
            north_south_pos, east_west_pos = move_to_waypoint(north_south_pos, east_west_pos, waypoint_ns_pos, waypoint_ew_pos, steps)
#        print("facing: {}, n-s: {}, e-w: {}, manhattan: {}".format(facing, north_south_pos, east_west_pos, get_manhattan_distance(north_south_pos, east_west_pos)))
    print("The manhattan distance is {}".format(get_manhattan_distance(north_south_pos, east_west_pos)))
