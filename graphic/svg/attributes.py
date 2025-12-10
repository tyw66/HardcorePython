from geom2d.affine_transf import AffineTransform

def stroke_color(color:str):
    return f'stroke="{color}"'

def stroke_width(width:float):
    return f'stroke-width="{str(width)}"'

def fill_color(color:str):
    return f'fill="{color}"'

def fill_opacity(opacity:float):
    return f'fill-opacity="{str(opacity)}"'

def affine_transform(t:AffineTransform):
    return f'transform="matrix({t.sx} {t.shy} {t.shx} {t.sy} {t.tx} {t.ty})"'

def font_size(size:float):
    return f'font-size="{str(size)}"'

def font_family(family:str):
    return f'font-family="{family}"'

def attrs_to_str(attrs:list[str])->str:
    return ' '.join(attrs)  