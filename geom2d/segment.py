from geom2d.point import Point
from geom2d.vectors import make_vector_between, make_versor, make_versor_between

class Segment:
    def __init__(self, start: Point, end: Point):
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise TypeError("Arguments must be Points")
        self.start = start
        self.end = end

    def __str__(self) -> str:
        '''重载打印操作符'''
        return f'[Segment] {self.start} to {self.end}, direction is {self.direction_vector}'  

    @property
    def direction_vector(self):
        '''线段的方向向量'''
        return make_vector_between(self.end, self.start)    
    
    @property
    def direction_versor(self):
        '''线段方向的单位向量'''
        return make_versor_between(self.end, self.start)
    
    @property
    def normal_versor(self):
        '''线段法向的单位向量'''
        return self.direction_versor.perpendicular()