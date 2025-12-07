from geom2d import AffineTransform,Rect,Point,Size
from graphic.svg.read import read_template

def svg_content(size:Size,
                primitives:list[str],
                viewbox_rect=None,
                transform=None
                )->str:
    '''生成SVG图像内容字符串'''
    viewbox_rect = viewbox_rect or __default_viewbox_rect(size)
    transform = transform or AffineTransform()
    template = read_template('img')
    return template \
        .replace('{{width}}', str(size.width)) \
        .replace('{{height}}', str(size.height)) \
        .replace('{{content}}','\n\t'.join(primitives)) \
        .replace('{{viewBox}}', __viewbox_from_rect(viewbox_rect)) \
        .replace('{{transf}}',__transf_matrix_vals(transform))

def __default_viewbox_rect(size:Size)->Rect:
    return Rect(Point(0,0),size)

def __viewbox_from_rect(rect:Rect)->str:
    return f"{rect.origin.x} {rect.origin.y} {rect.size.width} {rect.size.height}"

def __transf_matrix_vals(t:AffineTransform)->str:
    return f"matrix({t.sx} {t.shy} {t.shx} {t.sy} {t.tx} {t.ty})"