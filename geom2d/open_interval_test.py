import unittest

from geom2d.open_interval import OpenInterval

class TestOpenInterval(unittest.TestCase):
    def test_length(self):
        interval = OpenInterval(2, 5)
        expected_length = 3
        actual_length = interval.length
        self.assertEqual(expected_length, actual_length)

    def test_contains(self):
        interval = OpenInterval(1, 4)
        self.assertFalse(interval.contains(0))
        self.assertFalse(interval.contains(1))
        self.assertTrue(interval.contains(2))
        self.assertTrue(interval.contains(3))
        self.assertFalse(interval.contains(4))
        self.assertFalse(interval.contains(5))
    
    def test_overlaps_interval(self):
        interval = OpenInterval(1, 4)
        interval1 = OpenInterval(-3, 1)
        self.assertFalse(interval.overlaps_interval(interval1))
        interval2 = OpenInterval(-3, 2)
        self.assertTrue(interval.overlaps_interval(interval2))
        interval3 = OpenInterval(1, 2)
        self.assertTrue(interval.overlaps_interval(interval3))
        interval4 = OpenInterval(2, 6)
        self.assertTrue(interval.overlaps_interval(interval4))
        interval5 = OpenInterval(4, 6)
        self.assertFalse(interval.overlaps_interval(interval5))