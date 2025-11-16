from geom2d.point import Point
from geom2d.segment import Segment
from geom2d.polygon import Polygon
from geom2d.rect import Rect
from geom2d.circle import Circle
from geom2d.nums import are_close_enough

class AffineTransform:
    '''表示二维空间中的仿射变换'''
    def __init__(self, sx=1.0, sy=1.0, tx=0.0, ty=0.0, shx=0.0, shy=0.0):
        self.sx = sx  
        self.sy = sy
        self.tx = tx  
        self.ty = ty  
        self.shx = shx
        self.shy = shy

    def __str__(self) -> str:
        '''返回仿射变换的字符串表示'''
        return f'[AffineTransform] (sx={self.sx}, sy={self.sy}, shx={self.shx}, shy={self.shy}, tx={self.tx}, ty={self.ty},) '

    def __eq__(self, other: object) -> bool:
        '''重载等于操作符'''
        if self is other:
            return True
        
        if not isinstance(other, AffineTransform):
            return False
        
        return are_close_enough(self.sx, other.sx) and \
               are_close_enough(self.sy, other.sy) and \
               are_close_enough(self.tx, other.tx) and \
               are_close_enough(self.ty, other.ty) and \
               are_close_enough(self.shx, other.shx) and \
               are_close_enough(self.shy, other.shy)               
        

    def apply_to_point(self, point: Point) -> Point:
        '''对点应用仿射变换'''
        if not isinstance(point, Point):
            raise TypeError("Argument must be a Point")
        
        return Point(
            self.sx * point.x + self.shx * point.y + self.tx,
            self.shy * point.x + self.sy * point.y + self.ty
        )
    
    def apply_to_segment(self, segment: Segment) -> Segment:
        '''对线段应用仿射变换'''
        if not isinstance(segment, Segment):
            raise TypeError("Argument must be a Segment")
        
        new_start = self.apply_to_point(segment.start)
        new_end = self.apply_to_point(segment.end)
        return Segment(new_start, new_end)
    
    def apply_to_polygon(self, polygon: Polygon) -> Polygon:
        '''对多边形应用仿射变换'''
        if not isinstance(polygon, Polygon):
            raise TypeError("Argument must be a Polygon")
        
        return Polygon(
            [self.apply_to_point(v) for v in polygon.vertices]
        )
    
    def apply_to_rect(self, rect: Rect) -> Polygon:
        '''对矩形应用仿射变换'''
        if not isinstance(rect, Rect):
            raise TypeError("Argument must be a Rect")
        
        return self.apply_to_polygon(
            rect.to_polygon()
        )
    
    def apply_to_circle(self, circle: Circle, division=30) -> Polygon:
        '''对圆应用仿射变换，返回近似的多边形'''
        if not isinstance(circle, Circle):
            raise TypeError("Argument must be a Circle")
        
        return self.apply_to_polygon(
            circle.to_polygon(division)
        )
    
    def then(self, other: 'AffineTransform') -> 'AffineTransform':
        '''组合两个仿射变换'''
        if not isinstance(other, AffineTransform):
            raise TypeError("Argument must be an AffineTransform")
        
        return AffineTransform(
            sx = other.sx * self.sx + other.shx* self.shy,
            sy = other.shy * self.shx + other.sy* self.sy,
            tx = other.sx * self.tx + other.shx * self.ty + other.tx,
            ty = other.shy * self.tx + other.sy * self.ty + other.ty,
            shx = other.sx * self.shx + other.shx * self.sy,
            shy = other.shy * self.sx + other.sy * self.shy
        )

    def inverse(self) -> 'AffineTransform':
        '''计算仿射变换的逆变换'''
        denom = self.sx * self.sy - self.shx * self.shy
        if are_close_enough(denom, 0):
            raise ValueError("Affine transform is not invertible")
        
        return AffineTransform(
            sx = self.sy /denom,
            sy = self.sx /denom,
            tx = (self.ty * self.shx - self.tx * self.sy) / denom,
            ty = (self.tx * self.shy - self.ty * self.sx) / denom,
            shx = -self.shx / denom,
            shy = -self.shy / denom
        )