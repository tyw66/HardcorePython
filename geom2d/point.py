import math 
from geom2d.vector import Vector

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other) -> float:
        '''计算两点之间的距离'''
        if not isinstance(other, Point):
            raise TypeError("Argument must be a Point")
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def __add__(self, other):
        '''点加法'''
        if not isinstance(other, Point):
            raise TypeError("Argument must be a Point")
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        '''点减法'''
        if not isinstance(other, Point):
            raise TypeError("Argument must be a Point")
        return Vector(self.x - other.x, self.y - other.y)
    
    def displaced_by(self, vector: Vector, times=1):
        '''点平移'''
        if not isinstance(vector, Vector):
            raise TypeError("Argument must be a Vector")
        scaled_vec = vector.scaled_by(times)
        return Point(self.x + scaled_vec.u, self.y + scaled_vec.v)

