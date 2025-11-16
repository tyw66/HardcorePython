import unittest
from geom2d.segment import Segment
from geom2d.point import Point
from geom2d.vector import Vector
from geom2d import tparam

class TestSegment(unittest.TestCase):
    segment = Segment(Point(0, 400), Point(400, 0))

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

    def test_length(self):
        segment = Segment(Point(1, 2), Point(4, 6))
        actual = segment.length
        expected = 5.0
        self.assertEqual(expected, actual)

    def test_middle(self):
        segment = Segment(Point(1, 2), Point(9, 60))
        actual = segment.middle
        expected = Point(5, 31)
        self.assertEqual(expected, actual)

    def test_point_at_wrong_t(self):
        self.assertRaises(
            tparam.TParamError,
            self.segment.point_at,
            56.7
        )

    def test_point_at(self):
        t = tparam.make(0.25)
        expected = Point(100, 300)
        actual = self.segment.point_at(t)
        self.assertEqual(expected, actual)

    def test_closest_point_to(self):
        point = Point(400, 400)
        expected = Point(200, 200)
        actual = self.segment.closest_point_to(point)
        self.assertEqual(expected, actual)
        point = Point(0, 600)
        expected = Point(0, 400)
        actual = self.segment.closest_point_to(point)
        self.assertEqual(expected, actual)
        point = Point(600, 0)
        expected = Point(400, 0)
        actual = self.segment.closest_point_to(point)
        self.assertEqual(expected, actual)

    def test_parallel_segments_no_interaction(self):
        other = Segment(Point(200, 0), Point(0, 200))
        actual = self.segment.interacts_with(other)
        self.assertIsNone(actual)

    def test_segment_intersection(self):
        other = Segment(Point(0, 0), Point(400, 400))
        actual = self.segment.interacts_with(other)
        expected = Point(200, 200)
        self.assertEqual(expected, actual)
    
    def test_segment_not_intersection(self):
        other1= Segment(Point(0, 0), Point(50, 50))
        actual1= self.segment.interacts_with(other1)
        self.assertIsNone(actual1)
        other2= Segment(Point(0, 0), Point(-10, 100))
        actual2= self.segment.interacts_with(other2)
        self.assertIsNone(actual2)
        other3= Segment(Point(0, 0), Point(-100, 500))
        actual3= self.segment.interacts_with(other3)
        self.assertIsNone(actual3)