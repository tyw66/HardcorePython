from geom2d.point import Point
from geom2d.polygon import Polygon

def make_polygon_from_coords(coords: list[float]):
    '''从坐标列表创建多边形对象'''
    if len(coords) %2 !=0:
        raise ValueError("Coordinate list must contain an even number of values.")  
    
    indices = range(0, len(coords), 2)
    return Polygon(
        [Point(coords[i], coords[i+1]) for i in indices]
    )
    

