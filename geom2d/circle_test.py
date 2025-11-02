import unittest
from geom2d.circle import Circle
from geom2d.point import Point

class TestPolygon(unittest.TestCase):
    def test_area(self):
        circle = Circle(center=Point(0,0), radius=10)
        expected = 314.1592653589793
        actual = circle.area
        self.assertAlmostEqual(expected, actual)

    def test_circumference(self):
        circle = Circle(center=Point(0,0), radius=10)
        expected = 62.83185307179586
        actual = circle.circumference
        self.assertAlmostEqual(expected, actual)

    def test_contains_point_inside(self):
        circle = Circle(center=Point(0,0), radius=10)
        point = Point(5,5)
        self.assertTrue(circle.contains_point(point))

    def test_contains_point_outside(self):
        circle = Circle(center=Point(0,0), radius=10)
        point = Point(15,15)
        self.assertFalse(circle.contains_point(point))

    def test_to_polygon(self):
        circle = Circle(center=Point(0,0), radius=10)
        polygon = circle.to_polygon(12) 
        expected_vertices = [
            Point(10.0, 0.0),
            Point(8.660254037844387, 5.0),
            Point(5.0, 8.660254037844387),
            Point(0, 10.0),
            Point(-5.0, 8.660254037844387),
            Point(-8.660254037844387, 5.0),
            Point(-10.0, 0.0),
            Point(-8.660254037844387, -5.0),
            Point(-5.0, -8.660254037844387),
            Point(0, -10.0),
            Point(5.0, -8.660254037844387),
            Point(8.660254037844387, -5.0),
        ]  
        self.assertEqual(polygon.vertices, expected_vertices)
