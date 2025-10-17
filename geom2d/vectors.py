from geom2d.point import Point
from geom2d.vector import Vector

def make_vector_between(p1: Point, p2: Point) -> Vector:
    '''创建一个从p1指向p2的向量'''
    return p1 - p2 

def make_versor(u:float, v:float) -> Vector:
    '''创建一个单位向量'''
    return Vector(u, v).normalized()

def make_versor_between(p1: Point, p2: Point) -> Vector:
    '''创建一个从p1指向p2的单位向量'''
    return make_vector_between(p1, p2).normalized()