import unittest

from geom2d.point import Point
from geom2d.segment import Segment
from geom2d.polygon import Polygon

class TestPolygon(unittest.TestCase):
    vertices = [
        Point(0, 0),
        Point(30,0),
        Point(0,30)
    ]
    polygon = Polygon(vertices)

    def test_sides(self):
        exprcted = [
            Segment(self.vertices[0], self.vertices[1]),
            Segment(self.vertices[1], self.vertices[2]),
            Segment(self.vertices[2], self.vertices[0])
        ]
        actual = self.polygon.sides()
        self.assertEqual(exprcted, actual)

    def test_centriod(self):
        expected = Point(10, 10)
        actual = self.polygon.centroid
        self.assertEqual(expected, actual)

    def test_doesnt_contain_point(self):
        point = Point(15, 20)
        self.assertFalse(self.polygon.contains_point(point))

    def test_contain_point(self):
        point = Point(15,10)
        self.assertTrue(self.polygon.contains_point(point))
    
    def test_contain_vertec(self):
        self.assertTrue(
            self.polygon.contains_point(self.vertices[1])
        )