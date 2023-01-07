import tkinter as tk
from myframe import MyFrame

root = tk.Tk()
frame = MyFrame(root)
frame.pack(fill='both')
root.geometry("290x450")
root.mainloop()