from tkinter import Tk, Canvas

from geom2d import AffineTransform, Point, Circle
from graphic.simulation.draw import CanvasDrawing
from graphic.simulation.loop import main_loop

FPS = 30.0
frame_rate_s = 1.0 / FPS

tk = Tk()
tk.title("Hello Motion")    

canvas = Canvas(tk, width=600, height=600, bg="white")
canvas.grid(row=0, column=0)

max_frames = 200

transform = AffineTransform(sx=1, sy=1, tx=0, ty=0, shx=0.1, shy=0.1)
drawing = CanvasDrawing(canvas, transform)
circle = Circle(Point(300, 300), 1)

def update_system():
    circle.radius = (circle.radius + 15) % 450    
    tk.update()

def redraw():
    drawing.clear_drawing()
    drawing.draw_circle(circle, 20)

def should_continue(frame, time_s):
    return frame <= max_frames


main_loop(update_system, redraw, should_continue,frame_rate_s)
tk.mainloop()



