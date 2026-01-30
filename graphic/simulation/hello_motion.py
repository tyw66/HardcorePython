import time
from tkinter import Tk, Canvas, StringVar, Label

FPS = 30.0

frame_rate_s = 1.0 / FPS
frame_count = 1
max_frames = 300

tk = Tk()
tk.title("Hello Motion")    
canvas = Canvas(tk, width=400, height=400, bg="white")
canvas.grid(row=0, column=0)
label = StringVar()
label.set("Frame: ? of ?")
Label(tk, textvariable=label).grid(row=1, column=0)

def update_system():
    pass

def redraw():
    label.set(f"Frame: {frame_count} of {max_frames}")

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


