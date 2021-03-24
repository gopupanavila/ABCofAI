import tkinter as tk


root = tk.Tk()
root.geometry('300x300')
top = tk.Toplevel(root)
top.geometry('200x200')
top.grab_set()
top.wait_window()
root.mainloop()