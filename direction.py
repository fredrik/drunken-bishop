
class Direction(object):
    """Encode a sense of direction."""
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy


NW = Direction(dx=-1, dy=-1)
NE = Direction(dx=1, dy=-1)
SW = Direction(dx=-1, dy=1)
SE = Direction(dx=1, dy=1)
