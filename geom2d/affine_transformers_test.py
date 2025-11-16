import unittest

from geom2d.affine_transformers import make_scale
from geom2d.segment import Segment
from geom2d.point import Point

class TestAffineTransformers(unittest.TestCase):
    seg = Segment(Point(1, 4), Point(3,1))

    def test_make_scale_default_center(self):
        '''测试原点为中心的缩放变换'''
        scale = make_scale(2.0, 3.0)
        actual = scale.apply_to_segment(self.seg)
        expected = Segment(Point(2, 12), Point(6, 3))
        self.assertEqual(actual, expected)

    def test_make_scale_custom_center(self):
        '''测试自定义中心点的缩放变换'''
        center = Point(2, 2.5)
        scale = make_scale(2.0, 3.0, center)
        actual = scale.apply_to_segment(self.seg)
        expected = Segment(Point(0, 7), Point(4, -2))
        self.assertEqual(actual, expected)
        
       

