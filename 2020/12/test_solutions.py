import pytest
from solutions import *

def test_turn_ship():
    assert turn_ship("R","N",90) == "E"
    assert turn_ship("L","N",90) == "W"
    assert turn_ship("R","N",180) == "S"
    assert turn_ship("R","W",90) == "N"
    assert turn_ship("R","N",360) == "N"
    assert turn_ship("L","N",360) == "N"

def test_move_to_waypoint():
    assert move_to_waypoint(0,0,1,10,10) == (10, 100)

def test_rotate_waypoint_one_step():
    assert rotate_waypoint_one_step(4,10,'R') == (-10,4)
    assert rotate_waypoint_one_step(-10,4,'L') == (4,10)
