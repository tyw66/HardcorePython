import time
from tkinter import Tk, Canvas, StringVar, Label
from geom2d import AffineTransform, Point, Circle
from graphic.simulation.draw import CanvasDrawing

FPS = 10.0
frame_rate_s = 1.0 / FPS
frame_count = 1
max_frames = 300

tk = Tk()
tk.title("Hello Motion")    
canvas = Canvas(tk, width=600, height=600, bg="white")
canvas.grid(row=0, column=0)
label = StringVar()
label.set("Frame: ? of ?")
Label(tk, textvariable=label).grid(row=1, column=0)

transform = AffineTransform(sx=1, sy=1,tx=0, ty=0, shx=0, shy=0)
drawing = CanvasDrawing(canvas, transform)
circle = Circle(Point(300, 300), 1)


def update_system():
    circle.radius = (circle.radius + 15) % 450
    #tk.update()

def redraw():
    label.set(f"Frame: {frame_count} of {max_frames}")
    #drawing.clear_drawing()
    drawing.draw_circle(circle, 50)

while frame_count <= max_frames:
    update_start = time.time()
    update_system()
    redraw()
    tk.update()
    update_end = time.time()

    update_duration = update_end - update_start
    remaining_time = frame_rate_s - update_duration

    if remaining_time > 0:
        time.sleep(remaining_time)
    
    frame_count += 1

tk.mainloop()


