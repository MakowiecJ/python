from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 < x2, y1 < y2.
        if x1 > x2 or y1 > y2:
            raise ValueError
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return '[({}, {}), ({}, {})]'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle({}, {}, {}, {})'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1.__eq__(other.pt1) and self.pt2.__eq__(other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

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
        if 
        return Rectangle(other.pt1.x, other.pt1.y, self.pt2.x, self.pt2.y)

    def cover(self, other):     # prostąkąt nakrywający oba
        return Rectangle(self.pt1.x, self.pt1.y, other.pt2.x, other.pt2.y)

    def make4(self):           # zwraca krotkę czterech mniejszych
        center = center(self)
        return(Rectangle(self.pt1.x, self.pt1.y, center.x, center.y), Rectangle(center.x, self.pt1.y, self.pt2.x, center.y), Rectangle(self.pt1.x, center.y, center.x, self.pt2.y), Rectangle(center.x, center.y, self.pt2.x, self.pt2.y))
# A-------B   po podziale  A---+---B
# |       |                |   |   |
# |       |                +---+---+
# |       |                |   |   |
# D-------C                D---+---C

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def testStr(self):
        rec = Rectangle(0, 0, 4, 4)
        self.assertEqual('[(0, 0), (4, 4)]', rec.__str__())

    def testRepr(self):
        rec = Rectangle(0, 0, 4, 4)
        self.assertEqual('Rectangle(0, 0, 4, 4)', rec.__repr__())

    def testEq(self):
        rec1 = Rectangle(0, 0, 4, 4)
        rec2 = Rectangle(0, 0, 4, 4)
        rec3 = Rectangle(0, 0, 5, 5)
        self.assertTrue(rec1.__eq__(rec2))
        self.assertTrue(rec1 == rec2)
        self.assertFalse(rec1.__eq__(rec3))
        self.assertFalse(rec1 == rec3)
    
    def testNe(self):
        rec1 = Rectangle(0, 0, 4, 4)
        rec2 = Rectangle(0, 0, 4, 4)
        rec3 = Rectangle(0, 0, 5, 5)
        self.assertFalse(rec1.__ne__(rec2))
        self.assertTrue(rec1.__ne__(rec3))
    
    def testCenter(self):
        rec = Rectangle(2, 2, 4, 4)
        self.assertEqual(Point(3, 3), rec.center())
    
    def testArea(self):
        rec = Rectangle(0, 0, 4, 4)
        self.assertEqual(16, rec.area())
    
    def testMove(self):
        rec = Rectangle(0, 0, 4, 4)
        rec.move(2, 2)
        self.assertEqual(Rectangle(2, 2, 6, 6), rec)

    def testIntersection(self):
        rec1 = Rectangle(0, 0, 4, 4)
        rec2 = Rectangle(2, 2, 6, 6)
        self.assertEqual(Rectangle(2, 2, 4, 4), rec1.intersection(rec2))
        self.assertEqual(Rectangle(2, 2, 4, 4), rec2.intersection(rec1))


if __name__ == '__main__':
    unittest.main()