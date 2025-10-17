import unittest
from geom2d.point import Point
from geom2d.vector import Vector

class TestVector(unittest.TestCase):
    u = Vector(1, 2)
    v = Vector(4, 6)

    def test_equality(self):
        v1 = Vector(1.00000000001, 2.00000000001)
        v2 = Vector(1.00000000002, 2.00000000002)
        self.assertTrue(v1 == v2)
        v3 = Vector(1.01, 2.01)
        v4 = Vector(1.02, 2.02)
        self.assertFalse(v3 == v4)

    def test_addition(self):
        expected = Vector(5, 8)
        actual = self.u + self.v
        self.assertEqual(expected, actual)

    def test_subtraction(self):
        expected = Vector(3, 4)
        actual = self.v - self.u
        self.assertEqual(expected, actual)

    def test_scaling(self):
        expected = Vector(8, 12)
        actual = self.v.scaled_by(2)
        self.assertEqual(expected, actual)

    def test_dot_product(self):
        expected = 16
        actual = self.u.dot(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_cross_product(self):
        expected = -2
        actual = self.u.cross(self.v)
        self.assertAlmostEqual(expected, actual)

    def test_norm(self):
        expected = (1**2 + 2**2)**0.5
        actual = self.u.norm
        self.assertAlmostEqual(expected, actual)
    
    def test_is_normal(self):
        self.assertFalse(self.u.is_normal)
        self.assertTrue(Vector(1/(2**0.5), 1/(2**0.5)).is_normal)

    def test_are_parallel(self):
        self.assertTrue(self.u.is_parallel_to(self.u))

    def test_are_not_parallel(self):
        self.assertFalse(self.u.is_parallel_to(self.v)) 

    def test_are_perpendicular(self):
        perp = Vector(-2, 1)
        self.assertTrue(self.u.is_perpendicular_to(perp))
    
    def test_are_not_perpendicular(self):
        self.assertFalse(self.u.is_perpendicular_to(self.v))    