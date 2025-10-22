import math
from geom2d import nums

class Vector:
    def __init__(self,u, v) -> None:
        self.u = u        
        self.v = v

    def __str__(self) -> str:
        '''重载打印操作符'''
        return f'[Vector] ({self.u}, {self.v}) with norm {self.norm}'
    
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
    
    def normalized(self):
        '''单位化向量'''
        return self.scaled_by(1 / self.norm) if self.norm != 0 else Vector(0, 0)
    
    def with_length(self, length):
        '''将向量调整为指定长度'''
        return self.normalized().scaled_by(length) if length != 0 else Vector(0, 0)
    
    def dot(self, other):
        '''向量点积'''  
        return self.u * other.u + self.v * other.v if isinstance(other, Vector) else NotImplemented
    
    def project_over(self, direction):
        '''向量在另一个向量上的投影'''
        return self.dot(direction.normalized()) if isinstance(direction, Vector) else NotImplemented

    def cross(self, other):
        '''向量叉积'''  
        return (self.u * other.v - self.v * other.u) if isinstance(other, Vector) else NotImplemented

    def is_parallel_to(self, other):
        '''判断向量是否平行'''
        return nums.is_close_to_zero(self.cross(other)) if isinstance(other, Vector) else NotImplemented
    
    def is_perpendicular_to(self, other):
        '''判断向量是否垂直'''
        return nums.is_close_to_zero(self.dot(other)) if isinstance(other, Vector) else NotImplemented
        
    def angle_value_to(self, other):
        '''计算向量与另一个向量的夹角'''    
        dot_product = self.dot(other)
        norm_product = self.norm * other.norm
        return math.acos(dot_product / norm_product) if norm_product != 0 else float('nan')
    
    def angle_to(self, other):
        '''计算向量与另一个向量的夹角（弧度）'''
        value = self.angle_value_to(other)
        cross_product = self.cross(other)
        return math.copysign(value, cross_product) if not nums.is_close_to_zero(cross_product) else value
    
    def rotate_radians(self, radians): 
        '''将向量逆时针旋转指定弧度'''
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(self.u * cos - self.v * sin, self.u * sin + self.v * cos)
    
    def perpendicular(self):
        '''返回垂直于当前向量的向量'''
        return Vector(-self.v, self.u)
    
    def opposite(self):
        '''返回当前向量的反向向量'''
        return Vector(-self.u, -self.v) 
    
    def sine(self):
        '''返回向量的正弦值'''
        return self.v / self.norm if self.norm != 0 else float('nan')
    
    def cosine(self):
        '''返回向量的余弦值'''
        return self.u / self.norm if self.norm != 0 else float('nan')
    
    def __eq__(self, other) -> bool:
        '''重载等于操作符'''
        if self is other:
            return True
        if not isinstance(other, Vector):
            print("not isinstance(other, Vector)")
            return False
        return nums.are_close_enough(self.u, other.u) and \
               nums.are_close_enough(self.v, other.v)
    
