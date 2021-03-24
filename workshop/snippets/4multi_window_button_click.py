import tkinter as tk

root = tk.Tk()


def btn_click(event):
    print("Command clicked")
    top = tk.Toplevel(root)
    top.geometry('200x200')
    top.grab_set()
    top.wait_window()


root.title("Button Widget")
root.resizable(0, 0)  # resize based on width and height
root.geometry('300x300')
btn = tk.Button(root, text='Click Me', command=btn_click)
btn.grid(row=0, column=0, sticky='NW')
root.mainloop()
