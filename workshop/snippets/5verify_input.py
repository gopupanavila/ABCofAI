import tkinter as tk

root = tk.Tk()


def btn_click():
    print("Command clicked")
    top = tk.Toplevel(root)
    top.geometry('200x200')
    top.grab_set()
    top.wait_window()


def verify_int(event):
    try:
        int(entry.get())
        btn.configure(state=tk.ACTIVE)
    except ValueError as err:
        print(err)
        if not event.char.isdigit():
            entry.delete(0, tk.END)
            entry.insert(0, entry.get()[:-1])
            btn.configure(state=tk.DISABLED)


if __name__ == '__main__':
    root.title("Button Widget")
    root.resizable(0, 0)  # resize based on width and height
    entry = tk.Entry(root)
    entry.grid(row=0, column=0, sticky='NW')
    entry.bind('<KeyRelease>', verify_int)
    btn = tk.Button(root, text='Click Me', command=btn_click)
    btn.grid(row=0, column=1, sticky='NW')
    btn.configure(state=tk.DISABLED)
    root.mainloop()
