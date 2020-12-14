import pytest
from solutions import *

def test_replace_char_in_string():
	assert replace_char_in_string("test", "x", -2) == "text"

def test_apply_mask():
	mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
	assert apply_mask(11, mask) == 73
	assert apply_mask(101, mask) == 101
	assert apply_mask(0, mask) == 64