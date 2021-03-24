import tkinter as tk


def btn_click():
    print("Command clicked")


root = tk.Tk()
root.title("Button Widget")
root.resizable(0, 0)  # resize based on width and height
root.geometry('300x300')
btn = tk.Button(root, text='Click Me', command=btn_click)
btn.grid(row=0, column=0, sticky='NW')
root.mainloop()