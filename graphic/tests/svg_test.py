import unittest
from geom2d import Size, Point, Segment, Rect, Circle, Polygon, Vector, AffineTransform

from graphic.svg import attributes
from graphic.svg.primitives import segment
from graphic.svg.primitives import rectangle
from graphic.svg.primitives import circle
from graphic.svg.primitives import polygon
from graphic.svg.primitives import polyline
from graphic.svg.primitives import text
from graphic.svg.primitives import group

class TestSvg(unittest.TestCase):
    def test_line(self):
        '''测试SVG线段元素的生成'''
        expected = '<line x1="0" y1="0" x2="2" y2="8" stroke="red" stroke-width="2.0"/>'
        seg = Segment(Point(0,0), Point(2,8))
        attr = [attributes.stroke_color("red"), attributes.stroke_width(2.0)]
        actual = segment(seg, attr)
        self.assertEqual(expected, actual)  

    def test_rectangle(self):
        '''测试SVG矩形元素的生成'''
        expected = '<rect x="1" y="2" width="3" height="4" fill="#FF0024" fill-opacity="0.5"/>'
        rect = Rect(Point(1,2), Size(3,4))
        attr = [attributes.fill_color("#FF0024"), attributes.fill_opacity(0.5)]
        actual = rectangle(rect, attr)
        self.assertEqual(expected, actual)

    def test_circle(self):
        '''测试SVG圆元素的生成'''
        expected = '<circle cx="5" cy="6" r="7" transform="matrix(1 6 5 2 3 4)"/>'
        cc = Circle(Point(5,6), 7)
        attr = [attributes.affine_transform(AffineTransform(1,2,3,4,5,6))]
        actual = circle(cc,attr)
        self.assertEqual(expected, actual)

    def test_polygon(self):
        '''测试SVG多边形元素的生成'''
        expected = '<polygon points="1,2 3,4 5,6" />'
        poly = Polygon([Point(1,2), Point(3,4), Point(5,6)])
        actual = polygon(poly, [])
        self.assertEqual(expected, actual)

    def test_polyline(self):
        '''测试SVG多段线元素的生成'''
        expected = '<polyline points="1,2 3,4 5,6" />'
        actual = polyline(Polygon([Point(1,2), Point(3,4), Point(5,6)]))
        self.assertEqual(expected, actual)

    def test_text(self):
        '''测试SVG文本元素的生成'''
        expected = '<text x="10" y="20" dx="1" dy="2" font-size="12" font-family="Arial">Hello</text>'
        actual = text("Hello", Point(10,20), Vector(1,2), \
                      [attributes.font_size(12), attributes.font_family("Arial")])
        self.assertEqual(expected, actual)

    def test_group(self):
        '''测试SVG群组元素的生成'''
        expected = '<g stroke="blue">\n    <line x1="0" y1="0" x2="1" y2="1" />\n    <circle cx="2" cy="2" r="3" />\n</g>'
        line_elem = segment(Segment(Point(0,0), Point(1,1)))
        circle_elem = circle(Circle(Point(2,2), 3))
        actual = group([line_elem, circle_elem], [attributes.stroke_color("blue")])
        self.assertEqual(expected, actual)