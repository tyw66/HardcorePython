import math
from geom2d import nums

class Vector:
    def __init__(self,u, v) -> None:
        self.u = u
        self.v = v

    def __add__(self, other):
        '''向量加法'''
        if not isinstance(other, Vector):
            raise TypeError("Argument must be a Vector")
        return Vector(self.u + other.u, self.v + other.v)
    
    def __sub__(self, other):
        '''向量减法'''
        if not isinstance(other, Vector):
            raise TypeError("Argument must be a Vector")
        return Vector(self.u - other.u, self.v - other.v)
    
    def scaled_by(self, factor):
        '''向量数乘'''
        if not isinstance(factor, (int, float)):
            raise TypeError("Argument must be a number")
        return Vector(self.u * factor, self.v * factor)
    
    @property
    def norm(self) -> float:
        '''向量的模'''
        return math.sqrt(self.u ** 2 + self.v ** 2)
    
    @property
    def is_normal(self) -> bool:
        '''判断向量是否单位化'''
        return nums.is_close_to_one(self.norm)
    
