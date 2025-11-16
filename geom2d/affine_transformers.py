from geom2d.affine_transf import AffineTransform
from geom2d.point import Point

def make_scale(sx:float, sy:float, center=Point(0,0)):
    '''创建一个以指定点为中心的缩放变换'''
    return AffineTransform(
        sx = sx,
        sy = sy,
        tx = center.x * (1.0 - sx),
        ty = center.y * (1.0 - sy)
    )
