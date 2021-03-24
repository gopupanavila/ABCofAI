from tkinter import messagebox, Tk, Checkbutton, BOTH, END, BooleanVar, NORMAL, ACTIVE, DISABLED, Toplevel, Text
from tkinter.ttk import Frame, Button, Label, Entry


class MyDialog(Frame):

    def __init__(self, parent, master, data, unit_prices):
        super().__init__()
        top = self.top = Toplevel(parent)
        self.master = master
        self.pack(fill=BOTH, expand=True)
        self.txt_area = Text(top, height=50, width=50)
        self.txt_area.place(x=10, y=10, width=350, height=250)
        total = 0
        quote = 'Commodity UnitPrice Quantity Total\n'
        quote += '---------------------------------\n'
        for c, q in enumerate(data):
            if q:
                quote += f'Commodity{c+1}  {unit_prices[c]} {q} {q*unit_prices[c]}\n'
                total += q*unit_prices[c]
        quote += f"""
        ---------------------------------\n
        GRANT TOTAL:   ₹{total}
        \n
        """
        self.txt_area.insert(END, quote)
        self.mySubmitButton = Button(top, text='Pay Now', command=self.pay_now)
        self.mySubmitButton.place(x=370, y=200)

    def pay_now(self):
        print('Payment Done')
        self.top.destroy()
        self.destroy()
        self.master.clear_all()

    def show(self):
        self.top.geometry("500x300+20+30")
        self.top.grab_set()
        self.top.wait_window()


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def onclick(self):
        if self.var.get() == True:
            self.e1.configure(state=NORMAL)
        else:
            self.e1.configure(state=DISABLED)
        self.enable_btn()

    def onclick2(self):
        if self.var2.get() == True:
            self.e2.configure(state=NORMAL)
            self.submit_btn.configure(state=NORMAL)
        else:
            self.e2.configure(state=DISABLED)
        self.enable_btn()

    def enable_btn(self):
        if any((self.var2.get(), self.var.get(), self.var3.get())):
            self.submit_btn.configure(state=NORMAL)
        else:
            self.submit_btn.configure(state=DISABLED)

    def onclick3(self):
        if self.var3.get() == True:
            self.e3.configure(state=NORMAL)
        else:
            self.e3.configure(state=DISABLED)
        self.enable_btn()

    def keybind1(self, event):
        self.validate_for_int(event, self.e1)

    def keybind2(self, event):
        self.validate_for_int(event, self.e2)

    def keybind3(self, event):
        self.validate_for_int(event, self.e3)


    def validate_for_int(self, event, widget):
        val = widget.get()
        try:
            float(widget.get())
        except ValueError as verr:
            if not event.char.isdigit():
                widget.delete(0, END)
                widget.insert(0, val[:-1])

    def initUI(self):
        self.master.title("ABC of AI")
        self.pack(fill=BOTH, expand=True)

        # self.columnconfigure(1, weight=1)
        # self.columnconfigure(3, pad=7)
        # self.rowconfigure(3, weight=1)
        # self.rowconfigure(5, pad=7)

        l1 = Label(self, text="Commodities")
        l1.place(x=10, y=30)
        l2 = Label(self, text="Unit Price")
        l2.place(x=130, y=30)
        l3 = Label(self, text="Qty")
        l3.place(x=210, y=30)

        self.var = BooleanVar()
        self.var2 = BooleanVar()
        self.var3 = BooleanVar()

        self.cb = Checkbutton(self, text="Commodity1",
                         variable=self.var, command=self.onclick)
        #cb.select()
        self.cb.place(x=10, y=50)

        self.cb2 = Checkbutton(self, text="Commodity2",
                         variable=self.var2, command=self.onclick2)
        #cb2.select()
        self.cb2.place(x=10, y=80)

        self.cb3 = Checkbutton(self, text="Commodity3",
                          variable=self.var3, command=self.onclick3)
        # cb2.select()
        self.cb3.place(x=10, y=110)

        lbl1 = Label(self, text="1024₹")
        lbl1.place(x=130, y=50)

        lbl2 = Label(self, text="674₹")
        lbl2.place(x=130, y=80)

        lbl3 = Label(self, text="974₹")
        lbl3.place(x=130, y=110)

        self.e1 = Entry(self, state=DISABLED)
        self.e2 = Entry(self, state=DISABLED)
        self.e3 = Entry(self, state=DISABLED)
        self.e1.place(x=210, y=50)
        self.e2.place(x=210, y=80)
        self.e3.place(x=210, y=110)

        self.e1.bind('<KeyRelease>', self.keybind1)
        self.e2.bind('<KeyRelease>', self.keybind2)
        self.e3.bind('<KeyRelease>', self.keybind3)

        self.submit_btn = Button(self, text="Submit", command=self.on_btn_click)
        self.submit_btn.place(x=130, y=140)
        self.submit_btn.configure(state=DISABLED)

        self.cancel_btn = Button(self, text="Clear", command=self.on_cancel_btn_click)
        self.cancel_btn.place(x=230, y=140)

    def on_cancel_btn_click(self):
        self.clear_all()

    def on_btn_click(self):
        data = None
        qty1 = self.e1.get().strip()
        qty2 = self.e2.get().strip()
        qty3 = self.e3.get().strip()
        if any((qty1, qty2, qty3)):
            data = []
            for q in qty1, qty2, qty3:
                if bool(q):
                    data.append(float(q))
                else:
                    data.append(None)
            unit_prices = (1024, 674, 974)
            inputDialog = MyDialog(self.master, self, data, unit_prices).show()
        else:
            messagebox.showwarning("Quantities", "Required an entry in quantities")
        #self.master.wait_window(inputDialog.top)

    def clear_all(self):
        self.cb.deselect()
        self.cb3.deselect()
        self.cb2.deselect()
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e1.configure(state=DISABLED)
        self.e2.configure(state=DISABLED)
        self.e3.configure(state=DISABLED)
        self.submit_btn.configure(state=DISABLED)


def main():

    root = Tk()
    root.geometry("400x250+100+200")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
