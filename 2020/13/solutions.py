import math

def get_input(filename):
    with open(filename, "r") as input_file:
        earliest_departure_time = int(input_file.readline().strip())
        bus_list = [item for item in input_file.readline().strip().split(',')]
    return earliest_departure_time, bus_list

def remove_letters_from_from_list(list):
    return [int(item) for item in list if item.isnumeric()]

def get_earliest_bus(departure_time, bus_list):
    bus_to_take = max(bus_list)
    smallest_wait_time = max(bus_list) * departure_time
    for bus in bus_list:
        current_time = bus
        while current_time <= departure_time:
            current_time += bus
        difference = current_time - departure_time
        if difference < smallest_wait_time:
            smallest_wait_time = difference
            bus_to_take = bus
    return bus_to_take, smallest_wait_time

def does_shedule_satisfy_condition(schedule, start_time):
    current_time = start_time - 1
    for bus in schedule:
        current_time += 1
        if bus == 'x':
            continue #we don't care, no restriction on this minute
        if int(bus) % current_time != 0: #the bus we're on doesn't depart at this time
            return False
    return True

def find_earliest_time_stamp(schedule):
    buses = [(bus, int(time)) for bus,time in enumerate(schedule) if time != 'x']
    current_least_common_multiple = buses[0][1]
    timestamp = - buses[0][0]
    for delay, bus in buses[1:]:
        # normalize delay
        delay = -delay % bus
        k = (delay - timestamp) * pow(current_least_common_multiple, -1, bus) % bus
        new_least_common_multiple = abs(current_least_common_multiple * bus) // math.gcd(current_least_common_multiple, bus)
        timestamp = (current_least_common_multiple * k + timestamp) % new_least_common_multiple
        current_least_common_multiple = new_least_common_multiple
    return timestamp

# from https://topaz.github.io/paste/#XQAAAQDnBgAAAAAAAAARiEJHiiMzw3cPM/1Vl+2nx/DqKkM2yi+HVdpp+qLh9Jwh+ZECcFH/z2ezeBhLAAlXqL8dinkTJIQhuZMH73+dkdSjscwmffdV6cqa61BCB7CldrqNrR2QHGOlysYcvD2LvLAroBVLTU+CAz/FfzHpYDNhRjlYYJsH2lkufgqG4xMDB8ubXRP99/gqEFcJCRsLGOe8NPQoZ71a50UXEkBwifHBw30t3OpjGzUSD9w3ksgLLhkOHmN4M/gNNcbTOtLzbRnAN4xEcyidH6HjnXd2VZuOtgJ9G0UUA+dSrlBCil6QAUcLBAsGl3z3g8G/A8ae2WKfwEuSQf4yxf4sRBvLt+kRki5Yk1uALppHOYPAXDNvLKyI5IhJ0jAizVUMjK03UHDEZBN7+9bIYaJhMcxZLAkE1wlasvMvkRj4jCrpTV9OkglkKsMI2njeVhIGLvafiP7cpwC3pTvM8Vb7gSIdV7b5b2WbY2zXKC3kjYJzFDJS7H2Q43zVXRxdsaLYUj3vDqh2jbiyIkxH3avrxdftJjDu14SXMKis1JWr7QlG42LIa7Lno9jwbGq3bJRKYT293YiAeK4opEP5nPh+t1krm5JAbawPvVyYEwXXgByoHaqI7bAzJYJavxjYipoTDLIfOay6umUalgtoENAsHPO5tD0Fg1pp2xw1E7bq8NGZMZD+qCwf4FlhjxZoCq2/f2p2bY6HJltDYeWVsDWUmdoc75rgbNNHf3Z+SS0b8cvLIKc+M3vYlTplsbOZ6oU9BVUDVJ1g5bO5W9QcC4L9hWmBRfGELwIZjfvAE3QKV7a2NTvFMNxTF2WischDWPxrPUidU/VD5dyxq8I+WM5zb0oP2mp+09+mJzDMl5/OE0BRioe1TA5cuZvrYrqFGdn39FkHsvmFunaP9h86g66m4rq/k/ger0+aUKc429RyBrSO4MeBJIcXeaN4qaTpHiHMeOwUQeV6Idkz8uIzNF0ccXhef9nAkNvS/2zrx/VFgoRna+uMdyPercln0W/LsqADwGtcxha0B6vWTOKD44YpMeQzbK2yvTOfWrNh5uG6Ua+dlFIFDTxxrZU4+LCRPoM1s0enQN4UgqTlZJJ+VlzP5X6LdChd/+rGa/Q=
def bezout_coefficients(a: int, b: int):
    os, s = (1, 0)
    ot, t = (0, 1)

    while b != 0:
        q = a // b
        a, b = b, a - q * b

        os, s = s, os - q * s
        ot, t = t, ot - q * t

    return os, ot


def find_contest_departure(busses) -> int:
    modulos = [(bus, (bus - i) % bus) for i, bus in enumerate(busses) if bus > 0]

    # Chinese remainder theorem from
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    mod, time = modulos[0]

    for next_mod, offset in modulos[1:]:
        m1, m2 = bezout_coefficients(mod, next_mod)
        time = time * m2 * next_mod + offset * m1 * mod
        mod = mod * next_mod
        time %= mod
    return time


if __name__ == "__main__":
    departure_time, bus_list = get_input("input.txt")
    
    #puzzle1 solution
    running_bus_list = remove_letters_from_from_list(bus_list)
    bus_to_take, wait_time = get_earliest_bus(departure_time, running_bus_list)
    print("Taking bus {} after a {} minute wait. ID * wait time = {}".format(bus_to_take, wait_time, bus_to_take * wait_time))

    #puzzle2 solution
    bus_list_with_zeros = [0 if bus == 'x' else int(bus) for bus in bus_list]
    print("The earliest start time meeting the conditions is {}".format(find_contest_departure(bus_list_with_zeros)))