import math 
from geom2d.vector import Vector
from geom2d import nums 

class Point:
    '''表示二维空间中的点'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        '''返回点的字符串表示'''
        return f'[Point] ({self.x}, {self.y})'

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
    
    def displaced(self, vector: Vector, times=1.0):
        '''点平移'''
        if not isinstance(vector, Vector):
            raise TypeError("Argument must be a Vector")
        scaled_vec = vector.scaled_by(times)
        return Point(self.x + scaled_vec.u, self.y + scaled_vec.v)
    
    def __eq__(self, other: object) -> bool:
        '''重载等于操作符'''
        if self is other:
            return True
        if not isinstance(other, Point):
            print("not isinstance(other, Point)")
            return False
        return nums.are_close_enough(self.x, other.x) and \
                nums.are_close_enough(self.y, other.y)
    
