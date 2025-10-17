import unittest
from geom2d.segment import Segment
from geom2d.point import Point
from geom2d.vector import Vector

class TestSegment(unittest.TestCase):
    def test_direction_vector(self):
        segment = Segment(Point(1, 2), Point(4, 6))        
        actual = segment.direction_vector
        expected = Vector(3, 4)
        self.assertEqual(expected, actual)

    def test_direction_versor(self):
        segment = Segment(Point(0, 0), Point(3, 4))
        actual = segment.direction_versor
        expected = Vector(0.6, 0.8)
        self.assertEqual(expected, actual)

    def test_normal_versor(self):
        segment = Segment(Point(0, 0), Point(3, 4))
        actual = segment.normal_versor
        expected = Vector(-0.8, 0.6)  
        self.assertEqual(expected, actual)