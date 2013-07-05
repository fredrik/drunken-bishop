# coding: utf-8
import itertools
from collections import Counter

"""
The bishop wakes up in the center of a room. He is drunk and stumbles around,
putting down coins at each position he passes. The bishop only walks diagonally
much like bishops normally found on chess boards. The fingerprint determines
his steps.

The room is 17 positions wide and 9 positions long. The bishop starts in the
center of the room.
"""

"""
Because the bishop can only move one of four valid ways, we can represent this in binary.

“00″ means our bishop takes one move diagonally to the north-west.
“01″ means our bishop takes one move diagonally to the north-east.
“10″ means our bishop takes one move diagonally to the south-west.
“11″ means our bishop takes one move diagonally to the south-east.
"""

# keep track of where the coins are at
coins = Counter()

# the bishop starts in the center of the room
STARTING_POSITION = (8, 4)
ROOM_DIMENSIONS = (17, 9)


def hex_byte_to_binary(hex_byte):
    """
    Convert a hex byte (such as d4) into a string representation of its bits,
    e.g. d4 =>
    """
    assert len(hex_byte) == 2
    dec = int(hex_byte, 16)
    return bin(dec)[2:].zfill(8)


def bit_pairs(binary):
    """
    Convert a word into bit pairs little-endian style.
    '10100011' => ['11', '00', '10', '10']
    """
    def take(n, iterable):
        "Return first n items of the iterable as a list"
        return list(itertools.islice(iterable, n))
    def all_pairs(iterable):
        while True:
            pair = take(2, iterable)
            if not pair:
                break
            yield ''.join(pair)
    pairs = list(all_pairs(iter(binary)))
    return list(reversed(pairs))


class Direction(object):
    """Encode a sense of direction."""
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


NW = Direction(dx=-1, dy=-1)
NE = Direction(dx=1, dy=-1)
SW = Direction(dx=-1, dy=1)
SE = Direction(dx=1, dy=1)

direction_lookup = {
    '00': NW,
    '01': NE,
    '10': SW,
    '11': SE,
}

def directions_from_fingerprint(fingerprint):
    """
    Convert the fingerprint (16 hex-encoded bytes separated by colons)
    to steps (one of four directions: NW, NE, SW, SE).
    """
    for hex_byte in fingerprint.split(':'):
        binary = hex_byte_to_binary(hex_byte)
        # read each bit-pair in each word right-to-left (little endian)
        for bit_pair in bit_pairs(binary):
            direction = direction_lookup[bit_pair]
            yield direction


MAX_X = ROOM_DIMENSIONS[0] -1
MAX_Y = ROOM_DIMENSIONS[1] -1

def move(position, direction):
    """
    Returns new position given current position and direction to move in.
    """
    x, y = position
    assert 0 <= x <= MAX_X
    assert 0 <= y <= MAX_Y
    nx, ny = x + direction.dx, y + direction.dy
    # the drunk bishop is hindered by the wall.
    nx = 0 if nx <= 0 else min(nx, MAX_X)
    ny = 0 if ny <= 0 else min(ny, MAX_Y)
    return nx, ny


def drunken_bishop(fingerprint):
    position = STARTING_POSITION
    for direction in directions_from_fingerprint(fingerprint):
        position = move(position, direction)
        coins[position] += 1  # drop coin
