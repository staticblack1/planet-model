import jupyturtle

class P oint:
    """Represents a point in 2D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

class Line:
    """Represents a line segment defined by two points."""
    def __init__(self, p1:Point, p2:Point):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f'Line({self.p1}, {self.p2})'










def main():


if __name__ == '__main__':