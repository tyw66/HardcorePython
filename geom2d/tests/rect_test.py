import unittest
from geom2d.point import Point
from geom2d.size import Size
from geom2d.rect import Rect

class TestRect(unittest.TestCase):
    def test_properties(self):
        rect = Rect(origin=Point(10, 20), size=Size(30, 40))
        self.assertEqual(rect.left, 10)
        self.assertEqual(rect.right, 40)
        self.assertEqual(rect.bottom, 20)
        self.assertEqual(rect.top, 60)
        self.assertEqual(rect.area, 1200)
        self.assertEqual(rect.perimeter, 140)

    def test_contains_point(self):
        rect = Rect(origin=Point(0, 0), size=Size(100, 100))
        inside_point = Point(50, 50)
        outside_point = Point(150, 150)
        self.assertTrue(rect.contains_point(inside_point))
        self.assertFalse(rect.contains_point(outside_point))

    def test_intersection_with(self):
        rect1 = Rect(origin=Point(0, 0), size=Size(100, 100))
        rect2 = Rect(origin=Point(50, 50), size=Size(100, 100))
        expected_intersection = Rect(origin=Point(50, 50), size=Size(50, 50))
        intersection = rect1.intersection_with(rect2)
        self.assertEqual(intersection, expected_intersection)

        rect3 = Rect(origin=Point(200, 200), size=Size(50, 50))
        intersection_none = rect1.intersection_with(rect3)
        self.assertIsNone(intersection_none)