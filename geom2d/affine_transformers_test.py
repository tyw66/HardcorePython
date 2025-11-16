import unittest

from geom2d.affine_transformers import make_scale
from geom2d.affine_transformers import make_rotation
from geom2d.affine_transformers import ease_in_out_interpolation
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
        
    def test_make_rotation_default_center(self):
        '''测试原点为中心的旋转变换'''
        rotation = make_rotation(-3.141592653589 / 2)  # -90度
        actual = rotation.apply_to_segment(self.seg)
        expected = Segment(Point(4.0, -1.0), Point(1.0, -3.0))
        self.assertEqual(actual, expected)

    def test_make_rotation_custom_center(self):
        '''测试自定义中心点的旋转变换'''
        center = Point(2, 2.5)
        rotation = make_rotation(3.141592653589 / 2, center)  # 90度
        actual = rotation.apply_to_segment(self.seg)
        expected = Segment(Point(0.5, 1.5), Point(3.5,3.5))
        self.assertEqual(actual, expected)

    def test_ease_in_out_interpolation(self):
        '''测试缓入缓出插值变换'''
        start = make_scale(1.0, 1.0)
        end = make_scale(3.0, 2.0, Point(2, 2))
        steps = 4
        actual_transformations = ease_in_out_interpolation(start, end, steps)
        
        expected_transforms = [
            make_scale(1.0, 1.0, Point(2, 2)),
            make_scale(1.2, 1.1, Point(2, 2)),
            make_scale(2.0, 1.5, Point(2, 2)),
            make_scale(2.8, 1.9, Point(2, 2)),
            make_scale(3.0, 2.0, Point(2, 2)),
        ]

        for actual, expected in zip(actual_transformations, expected_transforms):
            self.assertEqual(actual, expected)

