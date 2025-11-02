from geom2d.nums import are_close_enough

class OpenInterval:
    '''表示二维空间中的开区间'''
    def __init__(self, start, end):
        if start >= end:
            raise ValueError("Start must be less than end for an open interval.")
        self.start = start
        self.end = end
    
    def __str__(self) -> str:
        '''返回开区间的字符串表示'''
        return f'[OpenInterval] (start={self.start}, end={self.end})'

    @property
    def length(self):
        '''计算开区间的长度'''
        return self.end - self.start
    
    def contains(self, point):
        '''判断点是否在开区间内'''
        return self.start < point < self.end

    def overlaps_interval(self, other):
        '''判断两个开区间是否重叠'''
        if are_close_enough(self.start, other.start) and \
              are_close_enough(self.end, other.end):
            return True
        
        return self.contains(other.start) or \
                self.contains(other.end) or \
                other.contains(self.start) or \
                other.contains(self.end)
    
    def compute_overlap_with(self, other):
        '''计算两个开区间的重叠部分'''
        if not self.overlaps_interval(other):
            return None
        
        return OpenInterval(
            max(self.start, other.start),
            min(self.end, other.end)
        )