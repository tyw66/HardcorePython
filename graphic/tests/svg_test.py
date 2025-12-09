import unittest
from geom2d import Size, Point, Segment, Rect, Circle, Polygon, Vector

from graphic.svg.primitives import segment
from graphic.svg.primitives import rectangle
from graphic.svg.primitives import circle
from graphic.svg.primitives import polygon
from graphic.svg.primitives import polyline
from graphic.svg.primitives import text

class TestSvg(unittest.TestCase):
    def test_line(self):
        '''测试SVG线段元素的生成'''
        actual = segment(Segment(Point(0,0), Point(2,8)))
        expected = '<line x1="0" y1="0" x2="2" y2="8" />'
        self.assertEqual(expected, actual)  

    def test_rectangle(self):
        '''测试SVG矩形元素的生成'''
        actual = rectangle(Rect(Point(1,2), Size(3,4)))
        expected = '<rect x="1" y="2" width="3" height="4" />'
        self.assertEqual(expected, actual)

    def test_circle(self):
        '''测试SVG圆元素的生成'''
        actual = circle(Circle(Point(5,6), 7))
        expected = '<circle cx="5" cy="6" r="7" />'
        self.assertEqual(expected, actual)

    def test_polygon(self):
        '''测试SVG多边形元素的生成'''
        actual = polygon(Polygon([Point(1,2), Point(3,4), Point(5,6)]))
        expected = '<polygon points="1,2 3,4 5,6" />'
        self.assertEqual(expected, actual)

    def test_polyline(self):
        '''测试SVG多段线元素的生成'''
        actual = polyline(Polygon([Point(1,2), Point(3,4), Point(5,6)]))
        expected = '<polyline points="1,2 3,4 5,6" />'
        self.assertEqual(expected, actual)

    def test_text(self):
        '''测试SVG文本元素的生成'''
        actual = text("Hello", Point(10,20), Vector(1,2))
        expected = '<text x="10" y="20" dx="1" dy="2" >Hello</text>'
        self.assertEqual(expected, actual)