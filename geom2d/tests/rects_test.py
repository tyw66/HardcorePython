import unittest
from geom2d.rects import make_rect_containing, make_rect_containing_with_margin, make_rect_centered
from geom2d.point import Point
from geom2d.size import Size

class TestRects(unittest.TestCase):
    def test_make_rect_containing(self):
        points = [Point(1, 2), Point(3, 4), Point(0, -1)]
        rect = make_rect_containing(points)
        self.assertEqual(rect.origin, Point(0, -1))
        self.assertEqual(rect.size, Size(3, 5))
    
    def test_make_rect_containing_with_margin(self):
        points = [Point(1, 2), Point(3, 4), Point(0, -1)]
        margin = 1.0
        rect = make_rect_containing_with_margin(points, margin)
        self.assertEqual(rect.origin, Point(-1, -2))
        self.assertEqual(rect.size, Size(5, 7))
    
    def test_make_rect_centered(self):
        center = Point(2, 3)
        width = 4
        height = 6
        rect = make_rect_centered(center, width, height)
        self.assertEqual(rect.origin, Point(0, 0))
        self.assertEqual(rect.size, Size(4, 6))