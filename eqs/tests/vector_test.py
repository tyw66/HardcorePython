from typing import Any
import unittest
from eqs.vector import Vector


class VectorTest(unittest.TestCase):
    def test_init(self):
        v = Vector(3)
        self.assertEqual(v.length, 3)
        self.assertEqual(v._Vector__data, [0.0, 0.0, 0.0])

    def test_init_empty(self):
        v = Vector(0)
        self.assertEqual(v.length, 0)
        self.assertEqual(v._Vector__data, [])

    def test_length_property(self):
        v = Vector(5)
        self.assertEqual(v.length, 5)

    def test_set_value(self):
        v = Vector(3)
        v.set_value(2.5, 1)
        self.assertEqual(v._Vector__data, [0.0, 2.5, 0.0])

    def test_set_value_chained(self):
        v = Vector(3)
        result = v.set_value(1.0, 0).set_value(2.0, 1).set_value(3.0, 2)
        self.assertIs(result, v)
        self.assertEqual(v._Vector__data, [1.0, 2.0, 3.0])

    def test_add_to_value(self):
        v = Vector(3)
        v.set_value(1.0, 0)
        v.add_to_value(2.5, 0)
        self.assertEqual(v._Vector__data, [3.5, 0.0, 0.0])

    def test_add_to_value_chained(self):
        v = Vector(3)
        result = v.add_to_value(1.0, 0).add_to_value(2.0, 1)
        self.assertIs(result, v)
        self.assertEqual(v._Vector__data, [1.0, 2.0, 0.0])

    def test_set_data(self):
        v = Vector(3)
        v.set_data([1.0, 2.0, 3.0])
        self.assertEqual(v._Vector__data, [1.0, 2.0, 3.0])

    def test_set_data_chained(self):
        v = Vector(3)
        result = v.set_data([1.0, 2.0, 3.0])
        self.assertIs(result, v)

    def test_set_data_length_mismatch(self):
        v = Vector(3)
        with self.assertRaises(ValueError):
            v.set_data([1.0, 2.0])

    def test_set_data_preserves_independence(self):
        v = Vector(3)
        external_data = [1.0, 2.0, 3.0]
        v.set_data(external_data)
        external_data[0] = 999.0
        self.assertEqual(v._Vector__data, [1.0, 2.0, 3.0])

    def test_eq_same_object(self):
        v = Vector(3)
        self.assertEqual(v, v)

    def test_eq_equal_vectors(self):
        v1 = Vector(3)
        v1.set_data([1.0, 2.0, 3.0])
        v2 = Vector(3)
        v2.set_data([1.0, 2.0, 3.0])
        self.assertEqual(v1, v2)

    def test_eq_different_length(self):
        v1 = Vector(2)
        v2 = Vector(3)
        self.assertNotEqual(v1, v2)

    def test_eq_different_values(self):
        v1 = Vector(3)
        v1.set_data([1.0, 2.0, 3.0])
        v2 = Vector(3)
        v2.set_data([1.0, 2.0, 4.0])
        self.assertNotEqual(v1, v2)

    def test_value_at(self):
        v = Vector(3)
        v.set_data([1.0, 2.0, 3.0])
        self.assertEqual(v.value_at(0), 1.0)
        self.assertEqual(v.value_at(1), 2.0)
        self.assertEqual(v.value_at(2), 3.0)

    def test_eq_not_vector(self):
        v = Vector(3)
        self.assertNotEqual(v, [0.0, 0.0, 0.0])
        self.assertNotEqual(v, dict({1:3.6, 2:2.3}))
