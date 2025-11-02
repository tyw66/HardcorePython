from geom2d.point import Point
from geom2d.size import Size
from geom2d.rect import Rect

def make_rect_containing(points:list[Point]):
    '''创建一个包含所有给定点的最小矩形'''
    if not points:
        raise ValueError("Point list is empty, cannot create bounding rectangle.")
    first_point = points[0]
    min_x, max_x = first_point.x, first_point.x
    min_y, max_y = first_point.y, first_point.y

    for point in points[1:]:
        max_x, max_y = max(max_x, point.x), max(max_y, point.y)
        min_x, min_y = min(min_x, point.x), min(min_y, point.y)
    
    return Rect(
        Point(min_x, min_y), 
        Size(max_x - min_x, max_y - min_y)
    )

def make_rect_containing_with_margin(points:list[Point], margin:float):
    '''创建一个包含所有给定点并带有边距的最小矩形'''
    bounding_rect = make_rect_containing(points)
    return Rect(
        Point(bounding_rect.origin.x - margin, bounding_rect.origin.y - margin),
        Size(bounding_rect.size.width + 2 * margin, bounding_rect.size.height + 2 * margin)
    )

def make_rect_centered(center:Point, width:float, height:float) -> Rect:
    '''创建一个以指定中心点和大小的矩形'''
    origin = Point(
        center.x - width / 2,
        center.y - height / 2
    )
    return Rect(origin, Size(width, height))