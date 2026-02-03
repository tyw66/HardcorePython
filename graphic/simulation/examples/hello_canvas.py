from tkinter import Tk, Canvas
tk = Tk()
tk.title("Hello Canvas")

canvas = Canvas(tk, width=600, height=600)
canvas.pack()

canvas.create_line(100, 420, 500, 420, fill="#3e8c0a", width=5)
canvas.create_oval(50, 50, 300, 250, fill="#a1dfed",outline="#000000", width=2)
canvas.create_rectangle(350, 50, 550, 250, fill="#f4a261", outline="#000000", width=2)
canvas.create_text(300, 400, text="Hello, Canvas!", font="Arial 20 bold",fill="#E39F00")
canvas.create_polygon(150, 300, 100, 500, 200, 500, fill="#e76f51", outline="#000000", width=2)
help(canvas.create_polygon)

tk.mainloop()