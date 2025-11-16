import unittest

from geom2d.affine_transf import AffineTransform
from geom2d.point import Point
from geom2d.segment import Segment
from geom2d.rect import Rect
from geom2d.size import Size
from geom2d.circle import Circle
from geom2d.polygon import Polygon

class TestAffineTransform(unittest.TestCase):
    point = Point(2, 3)
    scale = AffineTransform(2, 5)
    trans = AffineTransform(1, 1, 10, 15)
    shear = AffineTransform(1, 1, 0, 0, 3, 4)
    affine = AffineTransform(2, 2, 5, 7, 3, 0.5)

    def test_scale_point(self):
        scaled_point = self.scale.apply_to_point(self.point)
        self.assertTrue(scaled_point == Point(4, 15))

    def test_translate_point(self):
        translated_point = self.trans.apply_to_point(self.point)
        self.assertTrue(translated_point == Point(12, 18))
    
    def test_shear_point(self):
        sheared_point = self.shear.apply_to_point(self.point)
        self.assertTrue(sheared_point == Point(11, 11))

    def test_affine_transform_segment(self):
        segment = Segment(Point(2, 3), Point(5, 7))
        actual = self.affine.apply_to_segment(segment)
        self.assertTrue(actual == Segment(Point(18, 14), Point(36, 23.5)))

    def test_affine_transform_rect(self):
        rect = Rect(Point(2, 3), Size(3, 4))
        actual = self.affine.apply_to_rect(rect)
        self.assertTrue(actual == Polygon([Point(18,14), Point(24,15.5), Point(36,23.5), Point(30,22)]))    

    # def test_affine_transform_circle(self):
    #     circle = Circle(Point(2, 3), 5)
    #     actual = self.affine.apply_to_circle(circle, 8)
    #TODO
    #     self.assertTrue(actual == Polygon([Point(0,0),Point(0,0),Point(0,0),Point(0,0), 
    #                                        Point(0,0),Point(0,0),Point(0,0),Point(0,0)])) 

    def test_concatenate_scale_translate(self):
        actual = self.scale.then(self.trans)
        expected = AffineTransform(2, 5, 10, 15)
        self.assertEqual(expected, actual)

    def test_concatenate_translate_then_scale(self):
        actual = self.trans.then(self.scale)
        expected = AffineTransform(2, 5, 20, 75)
        self.assertEqual(expected, actual)
        
        
    def test_inverse(self):
        transf = AffineTransform(1,2,3,4,5,6)
        expected = AffineTransform()
        actual = transf.then(transf.inverse())
        self.assertTrue(expected == actual)
        