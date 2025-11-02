from geom2d.point import Point
from geom2d.size import Size
from geom2d.open_interval import OpenInterval
from geom2d.polygon import Polygon

class Rect:
    '''表示二维空间中的矩形'''
    def __init__(self, origin: Point, size: Size):
        self.origin = origin
        self.size = size
    
    def __str__(self) -> str:
        '''返回矩形的字符串表示'''
        return f'[Rect] (origin={self.origin}, size={self.size})'
            
    def __eq__(self, other) -> bool:
        '''判断两个矩形是否相等'''
        if self is other:
            return True 
        if not isinstance(other, Rect):
            return False
        return self.origin == other.origin and self.size == other.size

    @property
    def left(self) -> float:
        '''矩形左边界的x坐标'''
        return self.origin.x
    
    @property
    def right(self) -> float:
        '''矩形右边界的x坐标'''
        return self.origin.x + self.size.width
    

    @property
    def bottom(self) -> float:
        '''矩形下边界的y坐标'''
        return self.origin.y
    
    @property
    def top(self) -> float:
        '''矩形上边界的y坐标'''
        return self.origin.y + self.size.height

    @property
    def area(self) -> float:
        '''计算矩形的面积'''
        return self.size.width * self.size.height
    
    @property
    def perimeter(self) -> float:
        '''计算矩形的周长'''
        return 2 * (self.size.width + self.size.height)

    def contains_point(self, point: Point) -> bool:
        '''判断点是否在矩形内'''
        return self.left <= point.x <= self.right and \
               self.bottom <= point.y <= self.top

    def intersection_with(self, other):
        '''计算两个矩形的交集'''
        inter_left = max(self.left, other.left)
        inter_right = min(self.right, other.right)
        inter_bottom = max(self.bottom, other.bottom)
        inter_top = min(self.top, other.top)

        if inter_left < inter_right and inter_bottom < inter_top:
            return Rect(
                origin=Point(inter_left, inter_bottom),
                size=Size(inter_right - inter_left, inter_top - inter_bottom)
            )
        else:
            return None
        
    def to_polygon(self) -> Polygon:
        '''将矩形转换为多边形表示'''
        return Polygon([
            Point(self.left, self.bottom),
            Point(self.right, self.bottom),
            Point(self.right, self.top),
            Point(self.left, self.top)
        ])