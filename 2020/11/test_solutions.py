import pytest
from solutions import *

def test_is_seat_occupied_returns_false_for_out_of_bounds():
	test_map = [
		['L']
	]
	assert is_seat_occupied(test_map, 1, 1) == False

def test_is_seat_occupied_returns_true_if_seat_is_occupied():
	test_map = [
		['#']
	]
	assert is_seat_occupied(test_map, 0, 0) == True

def test_is_seat_occupied_returns_false_if_seat_is_empty():
	test_map = [
		['L']
	]
	assert is_seat_occupied(test_map, 0, 0) == False

def test_is_seat_available_returns_false_if_not_seat():
	test_map = [
		['.']
	]
	assert is_seat_available(test_map, 0, 0) == False

def test_is_seat_available_returns_true_if_empty():
	test_map = [
		['L']
	]
	assert is_seat_available(test_map, 0, 0) == True

def test_adjacent_seats_returns_zero_when_no_adjacent_seats():
	test_map = [
		['#']
	]
	assert get_adjacent_seats(test_map, 0, 0) == 0

def test_adjacent_seats_returns_correct_number():
	test_map = [
		['.','.','.'],
		['#','L','#'],
		['.','.','.'],		
	]
	assert get_adjacent_seats(test_map, 1, 1) == 2

def test_get_next_seat_state_returns_occupied_when_seat_surroundings_are_empty():
 	test_map = [
 		['L']
 	]
 	assert get_next_seat_state(test_map, 0, 0) == '#'

