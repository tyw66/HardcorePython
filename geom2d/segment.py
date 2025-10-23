from geom2d import tparam
from geom2d.line import Line
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
        return f'[Segment] from {self.start} to {self.end}, length is {self.length}, direction is {self.direction_versor}'  

    @property
    def direction_vector(self):
        '''线段的方向向量'''
        return make_vector_between(self.start, self.end)    
    
    @property
    def direction_versor(self):
        '''线段方向的单位向量'''
        return make_versor_between(self.start, self.end)
    
    @property
    def normal_versor(self):
        '''线段法向的单位向量'''
        return self.direction_versor.perpendicular()
    
    @property
    def length(self):
        '''线段的长度'''
        return self.start.distance_to(self.end)
        
    def point_at(self, t: float) -> Point:
        '''返回线段上参数为 t 的点，t ∈ [0, 1]'''
        tparam.ensure_valid(t)
        return self.start.displaced(self.direction_vector,t)
    
    @property
    def middle(self) -> Point:
        '''线段的中点'''
        return self.point_at(tparam.MIDDLE)
    
    def closest_point_to(self, point: Point) -> Point:
        '''返回线段上距离指定点最近的点'''
        v = make_vector_between(self.start, point)
        d = self.direction_versor
        vs = v.project_over(d)

        if vs < 0:
            return self.start
        elif vs > self.length:
            return self.end
        else:
            return self.start.displaced(d, vs)
        
    def distance_to(self, point: Point) -> float:
        '''返回线段到指定点的最短距离'''
        closest = self.closest_point_to(point)
        return closest.distance_to(point)
    
    def interacts_with(self, other):
        '''两线段的交点'''
        d1,d2=self.direction_vector,other.direction_vector
        if d1.is_parallel_to(d2):
            return None
        
        cross_prod=d1.cross(d2)
        delta =other.start - self.start
        t1 = (delta.u * d2.v - delta.v * d2.u) / cross_prod
        t2 = (delta.u * d1.v - delta.v * d1.u) / cross_prod

        if tparam.is_valid(t1) and tparam.is_valid(t2):
            return self.point_at(t1)
        else:
            #print(f't1:{t1} t2:{t2}')
            return None
        
    def __eq__(self, other) -> bool:
        '''重载等于操作符'''
        if self is other:
            return True
        if not isinstance(other, Segment):
            return False
        return (self.start == other.start and self.end == other.end)
    
    def bisector(self):
        '''返回线段的垂直平分线'''
        return Line(self.middle, self.normal_versor)