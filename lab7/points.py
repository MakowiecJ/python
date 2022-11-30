import math

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):        # zwraca string "Point(x, y)"
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):  # v1 - v2
        self.x -= other.x
        self.y -= other.y

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):          # długość wektora
        return math.sqrt(self.x**2 + self.y**2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 

    def testStr(self):
        point = Point(1, 2)
        self.assertEqual('(1, 2)', point.__str__())
    
    def testRepr(self):
        point = Point(2, 4)
        self.assertEqual('Point(2, 4)', point.__repr__())
    
    def testEq(self):
        point1 = Point(1, 2)
        point2 = Point(1, 2)
        point3 = Point(4, 6)
        self.assertTrue(point1.__eq__(point2))
        self.assertTrue(point1 == point2)
        self.assertFalse(point1.__eq__(point3))
        self.assertFalse(point1 == point3)
    
    def testNe(self):
        point1 = Point(1, 2)
        point2 = Point(1, 2)
        point3 = Point(4, 6)
        self.assertFalse(point1.__ne__(point2))
        self.assertTrue(point1.__ne__(point3))
    
    def testAdd(self):
        point1 = Point(1, 2)
        point2 = Point(1, 2)
        point1.__add__(point2)
        self.assertEqual(2, point1.x)
        self.assertEqual(4, point1.y)

    def testSub(self):
        point1 = Point(2, 4)
        point2 = Point(1, 1)
        point1.__sub__(point2)
        self.assertEqual(1, point1.x)
        self.assertEqual(3, point1.y)
    
    def testMul(self):
        point1 = Point(2, 4)
        point2 = Point(1, 1)
        self.assertEqual(6, point1.__mul__(point2))

    def testCoss(self):
        point1 = Point(3, 1)
        point2 = Point(3, 3)
        self.assertEqual(6, point1.cross(point2))
    
    def testLength(self):
        point1 = Point(3, 4)
        self.assertEqual(5, point1.length())
    
    def testHash(self):
        point = Point(1, 2)
        self.assertEqual(hash((1, 2)), point.__hash__())

if __name__ == '__main__':
    unittest.main()