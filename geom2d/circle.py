import math
from geom2d.point import Point
from geom2d.polygon import Polygon
from geom2d.nums import are_close_enough

class Circle:
    '''表示二维空间中的圆'''
    def __init__(self, center: Point, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.center = center
        self.radius = radius
    
    def __str__(self) -> str:
        '''返回圆的字符串表示'''
        return f'[Circle] (center={self.center}, radius={self.radius})'
            
    def __eq__(self, other) -> bool:
        '''判断两个圆是否相等'''
        if self is other:
            return True 
        if not isinstance(other, Circle):
            return False
        return self.center == other.center and are_close_enough(self.radius, other.radius)

    @property
    def area(self) -> float:
        '''计算圆的面积'''
        return math.pi * (self.radius ** 2)

    @property
    def circumference(self) -> float:
        '''计算圆的周长'''
        return 2 * math.pi * self.radius

    def contains_point(self, point: Point) -> bool:
        '''判断点是否在圆内'''
        return self.center.distance_to(point) < self.radius  
    
    def to_polygon(self, division) -> Polygon:
        '''将圆近似为多边形'''
        angle_delta = 2 * math.pi / division
        return Polygon(
            [self.__point_at_angle(i * angle_delta) 
             for i in range(division)]
        )       
    
    def __point_at_angle(self, angle: float) -> Point:
        '''计算圆上指定角度的点'''
        return Point(
            self.center.x + self.radius * math.cos(angle),
            self.center.y + self.radius * math.sin(angle)
        )
