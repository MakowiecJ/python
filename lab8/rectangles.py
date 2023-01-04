from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if x1 > x2 or y1 > y2:
            raise ValueError("Values should be x1 < x2 and y1 < y2")
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
    
    @staticmethod
    def from_points(points):
        return Rectangle(points[0].x, points[0].y, points[1].x, points[1].y)
    
    @property
    def top(self):
        return self.pt2.y
    
    @property
    def left(self):
        return self.pt1.x
    
    @property
    def bottom(self):
        return self.pt1.y
    
    @property
    def right(self):
        return self.pt2.x
    
    @property
    def width(self):
        return self.pt2.x - self.pt1.x
    
    @property
    def height(self):
        return self.pt2.y - self.pt1.y
    
    @property
    def topLeft(self):
        return Point(self.pt1.x, self.pt2.y)
    
    @property
    def bottomLeft(self):
        return self.pt1
    
    @property
    def topRight(self):
        return self.pt2
    
    @property
    def bottomRight(self):
        return Point(self.pt2.x, self.pt1.y)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return '[({}, {}), ({}, {})]'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle({}, {}, {}, {})'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1.__eq__(other.pt1) and self.pt2.__eq__(other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    @property
    def center(self):          # zwraca środek prostokąta
        return Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)

    def area(self):            # pole powierzchni
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

    def intersection(self, other):  # część wspólna prostokątów
        return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y), min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

    def cover(self, other):     # prostąkąt nakrywający oba
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y), max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self):           # zwraca krotkę czterech mniejszych
        center = self.center
        return(Rectangle(self.pt1.x, self.pt1.y, center.x, center.y), Rectangle(center.x, self.pt1.y, self.pt2.x, center.y), Rectangle(self.pt1.x, center.y, center.x, self.pt2.y), Rectangle(center.x, center.y, self.pt2.x, self.pt2.y))
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C