import math
from geom2d.affine_transf import AffineTransform
from geom2d.interpolation import ease_in_out_t_sequence, interpolate
from geom2d.point import Point

def make_scale(sx:float, sy:float, center=Point(0,0)):
    '''创建一个以指定点为中心的缩放变换矩阵'''
    return AffineTransform(
        sx = sx,
        sy = sy,
        tx = center.x * (1.0 - sx),
        ty = center.y * (1.0 - sy)
    )

def make_rotation(radians:float, center=Point(0,0)):
    '''创建一个以指定点为中心的旋转变换矩阵'''
    cos = math.cos(radians)
    sin = math.sin(radians)
    one_minus_cos = 1.0 - cos    
    return AffineTransform(
        sx = cos,
        sy = cos,
        tx = center.x * one_minus_cos + center.y * sin,
        ty = center.y * one_minus_cos - center.x * sin,
        shx = -sin,
        shy = sin
    )

def ease_in_out_interpolation(start: AffineTransform, end: AffineTransform, steps):
    '''使用缓入缓出插值在指定步数内从start插值到end'''
    t_sequence = ease_in_out_t_sequence(steps)
    return [AffineTransform(
                sx = interpolate(start.sx, end.sx, t),
                sy = interpolate(start.sy, end.sy, t),
                shx = interpolate(start.shx, end.shx, t),
                shy = interpolate(start.shy, end.shy, t),
                tx = interpolate(start.tx, end.tx, t),
                ty = interpolate(start.ty, end.ty, t),
            ) for t in t_sequence]