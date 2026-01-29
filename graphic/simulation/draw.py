from tkinter import Canvas
from functools import reduce

from geom2d import Segment, Polygon, Circle, Rect, AffineTransform

class CanvasDrawing:
    def __init__(self, canvas:Canvas, transform:AffineTransform):
        self.__canvas = canvas
        self.outline_color = '#aa3355'
        self.outline_width = 3
        self.fill_color = ''
        self.transform = transform

    def clear_drawing(self):
        '''清除画布内容'''
        self.__canvas.delete('all')

    def draw_segment(self, segment:Segment):
        '''绘制线段'''
        segment_t = self.transform.apply_to_segment(segment)
        self.__canvas.create_line(
            segment_t.start.x,
            segment_t.start.y,
            segment_t.end.x,
            segment_t.end.y,
            fill=self.outline_color,
            width=self.outline_width
        )
            
    def __draw_polygon(self, polygon:Polygon):
        '''多边形'''
        points = reduce(
            list.__add__,
            [[v.x, v.y] for v in polygon.vertices]
        )
        self.__canvas.create_polygon(
            points,
            outline=self.outline_color,
            width=self.outline_width,
            fill=self.fill_color
        )

    def draw_circle(self, circle:Circle, divisions = 30):
        '''绘制圆'''
        self.__draw_polygon(
            self.transform.apply_to_circle(circle, divisions)
        )

    def draw_rect(self, rect:Rect):
        '''绘制矩形'''
        self.__draw_polygon(
            self.transform.apply_to_rect(rect)
        )

    def draw_polygon(self, polygon:Polygon):
        '''绘制多边形'''    
        self.__draw_polygon(
            self.transform.apply_to_polygon(polygon)
        )

    def draw_arrow(self, segment:Segment, length:float, height:float):
        '''绘制箭头'''
        director = segment.direction_vector
        v_l = director.opposite().with_length(length)
        v_h1 = director.perpendicular().with_length(height / 2.0)
        v_h2 = v_h1.opposite()

        self.draw_segment(segment)
        self.draw_segment(
            Segment(segment.end, segment.end.displaced(v_l + v_h1))
        )
        self.draw_segment(
            Segment(segment.end, segment.end.displaced(v_l + v_h2))
        )