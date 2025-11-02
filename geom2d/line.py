from geom2d.point import Point
from geom2d.vector import Vector
from geom2d.vectors import make_vector_between

class Line:
    '''表示二维空间中的直线'''
    def __init__(self, base: Point, direction: Vector):
        self.base = base
        self.direction = direction

    def __str__(self) -> str:
        '''返回直线的字符串表示'''
        return f'[Line] (base={self.base}, direction={self.direction})'

    def is_parallel_to(self, other) -> bool:
        '''判断两条直线是否平行'''
        return self.direction.is_parallel_to(other.direction)
    
    def is_perpendicular_to(self, other) -> bool:
        '''判断两条直线是否垂直'''
        return self.direction.is_perpendicular_to(other.direction)

    def perpendicular_through(self, point: Point):
        '''通过一点作直线的垂线'''
        perp_direction = self.direction.perpendicular()
        return Line(point, perp_direction)
    
    def parallel_through(self, point: Point):
        '''通过一点作直线的平行线'''
        return Line(point, self.direction)
    
    def intersection_with(self, other):
        '''计算两条直线的交点'''
        if self.is_parallel_to(other):
            return None 
        
        d1,d2 = self.direction, other.direction
        cross_prod = d1.cross(d2)
        delta = make_vector_between(self.base, other.base)
        t1 = (delta.u * d2.v -delta.v * d2.u) / cross_prod
        return self.base.displaced(d1, t1)
