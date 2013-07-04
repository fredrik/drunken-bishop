# coding: utf-8
import itertools

"""



The bishop wakes up in the center of a room. He is drunk and stumbles around,
putting down coins at each position he passes. The fingerprint determines his
steps.
"""

"""
Because the bishop can only move one of four valid ways, we can represent this in binary.

“00″ means our bishop takes one move diagonally to the north-west.
“01″ means our bishop takes one move diagonally to the north-east.
“10″ means our bishop takes one move diagonally to the south-west.
“11″ means our bishop takes one move diagonally to the south-east.
"""

# the bishop starts in the center of the room
STARTING_POSITION = 76


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

def steps_from_fingerprint(fingerprint):
    """
    Convert the fingerprint (16 hex-encoded bytes separated by colons)
    to steps (one of four directions: NW, NE, SW, SE).
    """
    position = STARTING_POSITION
    for hex_byte in fingerprint.split(':'):
        binary = hex_byte_to_binary(hex_byte)
        # read each bit-pair in each word right-to-left (little endian)
        for bit_pair in bit_pairs(binary):
            direction = direction_lookup[bit_pair]
            # ..



def drunken_bishop(fingerprint):
    for step in steps_from_fingerprint(fingerprint):
        pass
