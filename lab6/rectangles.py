from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)    # lewy dolny
        self.pt2 = Point(x2, y2)    # prawy gorny

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return '[({}, {}), ({}, {})]'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle({}, {}, {}, {})'.format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1.__eq__(other.pt1) and self.pt2.__eq__(other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        return Point(self.pt2.x - self.pt1.x, self.pt2.y - self.pt1.y)

    def area(self):            # pole powierzchni
        return abs(self.pt1.x - self.pt2.x) * abs(self.pt1.y - self.pt2.y)

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt1.y += y
        self.pt2.y += y

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
        rec = Rectangle(0, 0, 4, 4)
        self.assertTrue(Point(2, 2), rec.center())
    
    def testArea(self):
        rec = Rectangle(0, 0, 4, 4)
        self.assertTrue(16, rec.area())
    
    def testMove(self):
        rec = Rectangle(0, 0, 4, 4)
        rec.move(2, 2)
        self.assertTrue(Rectangle(2, 2, 6, 6), rec)


if __name__ == '__main__':
    unittest.main()