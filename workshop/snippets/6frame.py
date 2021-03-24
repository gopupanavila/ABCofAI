import tkinter as tk


class Page(tk.Frame):

    def __init__(self, master, title):
        super().__init__(master, relief='flat', borderwidth=20)
        self.init_ui(title)

    def btn_click(self):
        print('Button Clicked')

    def init_ui(self, title):
        self.master.title(title)
        self.pack(fill=None, expand=False)
        tk.Label(self, text='Test Frame',
                 font='Helvetica 12 bold').grid(
            row=0, columnspan=2, sticky='NW')
        tk.Entry(self).grid(row=1, column=0, sticky='NW')
        tk.Button(self, text='Click Me', command=self.btn_click).grid(
            row=1, column=1, sticky='NW')


if __name__ == '__main__':
    root = tk.Tk()
    Page(root, title='Frame Example')
    root.mainloop()
