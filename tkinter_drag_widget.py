# python 3.11.6
import tkinter as tk

root = tk.Tk()
root.geometry('600x600')

class DragableLabel(tk.Label):
# replace any widget from tkinter library for make it dragable
    
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, **kwargs)
        
        self.bind('<ButtonPress-1>', self.on_drag_start)
        self.bind('<B1-Motion>', self.on_drag_motion)
    
    def on_drag_start(self, event: tk.Event):
        self.start_x = event.x
        self.start_y = event.y
    
    def on_drag_motion(self, event: tk.Event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        
        self.place(x=self.winfo_x()+dx, y=self.winfo_y()+dy)

label = DragableLabel(root, text='drag')
label.pack()

root.mainloop()
