import unittest
from geom2d.point import Point
from geom2d.vector import Vector

class TestPoint(unittest.TestCase):
    def test_distance_to(self):
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        expected = 5.0
        actual = p1.distance_to(p2)
        self.assertAlmostEqual(expected, actual)

    def test_addition(self):
        p1 = Point(1, 2)
        p2 = Point(3, 4)
        expected = Point(4, 6)
        actual = p1 + p2
        self.assertEqual(expected, actual)

    def test_subtraction(self):
        p1 = Point(5, 7)
        p2 = Point(2, 3)
        expected = Vector(3, 4)
        vector = p1 - p2
        self.assertEqual(expected.u, vector.u)
        self.assertEqual(expected.v, vector.v)

    def test_displacement(self):
        p = Point(1, 2)
        v = Vector(3, 4)
        expected = Point(4, 6)
        actual = p.displaced(v)
        self.assertEqual(expected, actual)
        expected_scaled = Point(7, 10)
        actual_scaled = p.displaced(v, times=2)
        self.assertEqual(expected_scaled, actual_scaled)
        
    def test_equality(self):
        p1 = Point(1.00000000001, 2.00000000001)
        p2 = Point(1.00000000002, 2.00000000002)
        self.assertTrue(p1 == p2)
        p3 = Point(1.01, 2.01)
        p4 = Point(1.02, 2.02)
        self.assertFalse(p3 == p4)