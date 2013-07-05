import pytest

from drunken_bishop import hex_byte_to_binary
from drunken_bishop import bit_pairs
from drunken_bishop import move
from drunken_bishop import Direction
from drunken_bishop import NW, NE, SW, SE


def test_hex_byte_to_binary():
    assert hex_byte_to_binary('00') == '00000000'
    assert hex_byte_to_binary('01') == '00000001'
    assert hex_byte_to_binary('10') == '00010000'
    assert hex_byte_to_binary('d4') == '11010100'
    assert hex_byte_to_binary('ff') == '11111111'


def test_bit_pairs():
    assert bit_pairs('10101100') == ['00', '11', '10', '10']
    assert bit_pairs('00011011') == ['11', '10', '01', '00']


def test_move_refuses_bad_position():
    any_direction = Direction(dx=0, dy=1)
    with pytest.raises(AssertionError):
        move((-1, 0), any_direction)
    with pytest.raises(AssertionError):
        move((200, 0), any_direction)
    with pytest.raises(AssertionError):
        move((0, -10), any_direction)
    with pytest.raises(AssertionError):
        move((0, 300), any_direction)

def test_move_in_corners():
    assert move((0, 0), NW) == (0, 0)
    assert move((16, 0), NE) == (16, 0)
    assert move((0, 8), SW) == (0, 8)
    assert move((16, 8), SE) == (16, 8)

def test_move():
    assert move((8, 4), NW) == (7, 3)
    assert move((8, 4), NE) == (9, 3)
    assert move((8, 4), SW) == (7, 5)
    assert move((8, 4), SE) == (9, 5)

def test_move_slides_along_the_wall():
    left_side = (0, 1)
    assert move(left_side, NW) == (0, 0)
    assert move(left_side, SW) == (0, 2)

    left_side = (16, 1)
    assert move(left_side, NE) == (16, 0)
    assert move(left_side, SE) == (16, 2)
