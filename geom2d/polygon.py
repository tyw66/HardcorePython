import math
import operator
from functools import reduce

from geom2d.nums import are_close_enough
from geom2d.point import Point
from geom2d.segment import Segment
from geom2d.vectors import make_vector_between
from utils.pairs import make_round_pairs

class Polygon:
    def __init__(self, vertices: list[Point]):
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        self.vertices = vertices    

    def sides(self):
        '''生成多边形的边列表'''
        vertex_pairs = make_round_pairs(self.vertices)
        return [
            Segment(pair[0], pair[1])
            for pair in vertex_pairs
        ]
    
    @property
    def centroid(self) -> Point:
        '''计算多边形的重心'''
        vtx_count = len(self.vertices)
        vtx_sum = reduce(operator.add, self.vertices)
        return Point(
            vtx_sum.x / vtx_count, 
            vtx_sum.y / vtx_count
            )
        
    def contains_point(self, point: Point) -> bool:
        '''判断点是否在多边形内部'''
        if point in self.vertices:
            return True
        
        vecs = [make_vector_between(point, vertex) 
                for vertex in self.vertices]
        paired_vecs = make_round_pairs(vecs)
        #在内部：angles求和为2pi；在外部：angles求和为0;
        angles = [v1.angle_to(v2) for v1, v2 in paired_vecs] 
        angle_sum = reduce(operator.add, angles)

        return are_close_enough(angle_sum, 2 * math.pi)

    def __eq__(self, other: object) -> bool:
        '''重载等于操作符'''
        if self is other:
            return True
        if not isinstance(other, Polygon):
            return False
        return self.vertices == other.vertices