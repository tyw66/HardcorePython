from geom2d.point import Point
from geom2d.circle import Circle
from geom2d.segment import Segment

def make_circle_from_points(a:Point, b:Point, c:Point) -> Circle:
    '''通过三点确定一个圆'''
    chord_one_bisec = Segment(a, b).bisector
    chord_two_bisec = Segment(b, c).bisector
    center = chord_one_bisec.intersection_with(chord_two_bisec)
    if center is None:
        raise ValueError("The bisectors do not intersect; cannot determine the circle.")
    radius = center.distance_to(a)
    return Circle(center, radius)