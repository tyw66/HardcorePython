from geom2d.nums import are_close_enough

class Size:
    '''表示二维空间中的尺寸'''
    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")
        self.width = width
        self.height = height
    
    def __str__(self) -> str:
        '''返回尺寸的字符串表示'''
        return f'[Size] (width={self.width}, height={self.height})'

    def __eq__(self, other) -> bool:
        if self is other:
            return True 
        if not isinstance(other, Size):
            return False
        return (are_close_enough(self.width, other.width) and 
                are_close_enough(self.height, other.height))