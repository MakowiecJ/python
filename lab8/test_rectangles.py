import pytest

from points import Point
from rectangles import Rectangle

class TestRectangles:
    def testInit(self):
        with pytest.raises(ValueError):
            rec = Rectangle(4, 4, 0, 0)

    def testStr(self):
        rec = Rectangle(0, 0, 4, 4)
        assert '[(0, 0), (4, 4)]' == rec.__str__()

    def testRepr(self):
        rec = Rectangle(0, 0, 4, 4)
        assert 'Rectangle(0, 0, 4, 4)' == rec.__repr__()

    def testEq(self):
        rec1 = Rectangle(0, 0, 4, 4)
        rec2 = Rectangle(0, 0, 4, 4)
        rec3 = Rectangle(0, 0, 5, 5)
        assert rec1.__eq__(rec2) == True
        assert rec1 == rec2
        assert rec1.__eq__(rec3) == False
        assert rec1 != rec3
    
    def testNe(self):
        rec1 = Rectangle(0, 0, 4, 4)
        rec2 = Rectangle(0, 0, 4, 4)
        rec3 = Rectangle(0, 0, 5, 5)
        assert rec1.__ne__(rec2) == False
        assert rec1.__ne__(rec3) == True
    
    def testCenter(self):
        rec = Rectangle(2, 2, 4, 4)
        point = Point(3, 3)
        assert point == rec.center
    
    def testArea(self):
        rec = Rectangle(0, 0, 4, 4)
        assert 16 == rec.area()
    
    def testMove(self):
        rec = Rectangle(0, 0, 4, 4)
        rec.move(2, 2)
        assert Rectangle(2, 2, 6, 6) == rec

    def testIntersection(self):
        rec1 = Rectangle(0, 0, 4, 4)
        rec2 = Rectangle(2, 2, 6, 6)
        rec3 = Rectangle(0, 2, 4, 4)
        assert Rectangle(2, 2, 4, 4) == rec1.intersection(rec2)
        assert Rectangle(2, 2, 4, 4) == rec2.intersection(rec1)
        assert Rectangle(0, 2, 4, 4) == rec1.intersection(rec3)

    def testCover(self):
        rec1 = Rectangle(0, 0, 4, 4)
        rec2 = Rectangle(2, 2, 6, 6)
        assert Rectangle(0, 0, 6, 6) == rec1.cover(rec2)
        assert Rectangle(0, 0, 6, 6) == rec2.cover(rec1)
    
    def testMake4(self):
        rec = Rectangle(0, 0, 4, 4)
        rects = rec.make4()
        assert (Rectangle(0,0,2,2) in rects) == True
        assert (Rectangle(2,0,4,2) in rects) == True
        assert (Rectangle(2,2,4,4) in rects) == True
        assert (Rectangle(0,2,2,4) in rects) == True
    
    def testFromPoints(self):
        point1 = Point(0, 0)
        point2 = Point(4, 4)
        assert Rectangle(0, 0, 4, 4) == Rectangle.from_points((point1, point2))
    
    def testProperties(self):
        rec = Rectangle(0, 0, 4, 2)
        assert 2 == rec.top
        assert 0 == rec.left
        assert 0 == rec.bottom
        assert 4 == rec.right
        assert 4 == rec.width
        assert 2 == rec.height

        assert Point(0, 2) == rec.topLeft
        assert Point(0, 0) == rec.bottomLeft
        assert Point(4, 2) == rec.topRight
        assert Point(4, 0) == rec.bottomRight

if __name__ == "__main__":
    pytest.main()