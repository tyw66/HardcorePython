from geom2d import Segment, Rect, Circle, Polygon, Vector, Point
from graphic.svg.attributes import attrs_to_str
from graphic.svg.read import read_template

__segment_template = read_template('line')
__rect_template = read_template('rect')
__circle_template = read_template('circle')
__polygon_template = read_template('polygon')
__polyline_template = read_template('polyline')
__text_template = read_template('text')
__group_template = read_template('group')

def segment(seg:Segment, attributes=()):
    '''生成SVG中的线段元素'''
    return __segment_template \
        .replace('{{x1}}', str(seg.start.x)) \
        .replace('{{y1}}', str(seg.start.y)) \
        .replace('{{x2}}', str(seg.end.x)) \
        .replace('{{y2}}', str(seg.end.y)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def rectangle(rect:Rect, attributes=()):
    '''生成SVG中的矩形元素'''
    return __rect_template \
        .replace('{{x}}', str(rect.origin.x)) \
        .replace('{{y}}', str(rect.origin.y)) \
        .replace('{{width}}', str(rect.size.width)) \
        .replace('{{height}}', str(rect.size.height)) \
        .replace('{{attrs}}', attrs_to_str(attributes))    

def circle(circle:Circle, attributes=()):
    '''生成SVG中的圆元素'''
    return __circle_template \
        .replace('{{cx}}', str(circle.center.x)) \
        .replace('{{cy}}', str(circle.center.y)) \
        .replace('{{r}}', str(circle.radius)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def polygon(polygon:Polygon, attributes=()):
    '''生成SVG中的多边形元素'''
    point_list = [f'{pt.x},{pt.y}' for pt in polygon.vertices]
    return __polygon_template \
        .replace('{{points}}', ' '.join(point_list)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def polyline(points:list[Point], attributes=()):
    '''生成SVG中的多段线元素'''
    point_list = [f'{pt.x},{pt.y}' for pt in points]
    return __polyline_template \
        .replace('{{points}}', ' '.join(point_list)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def text(txt:str, pos:Point, disp:Vector, attributes=()):
    '''生成SVG中的文本元素'''
    return __text_template \
        .replace('{{x}}', str(pos.x)) \
        .replace('{{y}}', str(pos.y)) \
        .replace('{{dx}}', str(disp.u)) \
        .replace('{{dy}}', str(disp.v)) \
        .replace('{{text}}', txt) \
        .replace('{{attrs}}', attrs_to_str(attributes)) 

def group(primitives:list[str], attributes=()):
    '''生成SVG中的群组元素'''
    return __group_template \
        .replace('{{content}}', '\n    '.join(primitives)) \
        .replace('{{attrs}}', attrs_to_str(attributes))

def arrow(
        _segment:Segment,
        length:float,
        height:float,
        attributes=()
):
    '''生成SVG中的箭头元素'''
    director = _segment.direction_vector
    v_l = director.opposite().with_length(length)
    v_h1 = director.perpendicular().with_length(height / 2)
    v_h2 = v_h1.opposite()

    return group(
        [
            segment(_segment),
            polyline([
                _segment.end.displaced(v_l + v_h1),
                _segment.end,
                _segment.end.displaced(v_l + v_h2)
            ])
        ],
        attributes            
    )


