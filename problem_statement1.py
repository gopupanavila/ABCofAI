from tkinter import (messagebox,
                     Tk, Checkbutton,
                     END, BooleanVar, NORMAL,
                     DISABLED, Toplevel)
from tkinter.ttk import Frame, Button, Label, Entry

from logic import BusinessLogic


class Page2(Frame):

    def __init__(self, parent, main_page):
        super().__init__(parent, relief='flat', borderwidth=20)
        self.top = Toplevel(parent)
        self.main_page = main_page
        self.pack(fill=None, expand=False)
        self.set_header()
        self.set_body()

    def set_header(self):
        Label(self.top, text='Receipt',
              font='Helvetica 12 bold').grid(row=0,
                                             columnspan=4)
        Label(self.top, text='SI No',
              font='Helvetica 9 bold').grid(row=1,
                                             column=0, sticky='NW')
        for col, item in enumerate(self.main_page.business_logic.header[1:]):
            column = col + 1
            Label(self.top, text=item,
                  font='Helvetica 9 bold').grid(row=1,
                                                 column=column, sticky='NW')
        Label(self.top, text='TOTAL',
              font='Helvetica 9 bold').grid(row=1,
                                            column=4, sticky='NW')

    def set_body(self):
        si_no = 2
        for row, item in enumerate(self.main_page.business_logic.selected_items):
            si_no += row
            Label(self.top, text=str(row + 1)).grid(row=si_no, column=0, sticky='NW')
            Label(self.top, text=item).grid(row=si_no, column=1, sticky='NW')
            Label(self.top,
                  text=str(self.main_page.business_logic.items.get(item))).grid(
                row=si_no, column=2, sticky='NW')
            qty = self.main_page.business_logic.selected_items.get(item)
            Label(self.top, text=str(qty)).grid(row=si_no, column=3, sticky='NW')
            total = self.main_page.business_logic.total(item, qty)
            Label(self.top, text=str(total)).grid(row=si_no, column=4, sticky='NW')
        si_no += 1
        Label(self.top, text='Cost').grid(row=si_no, column=3, sticky='NW')
        Label(self.top, text=str(self.main_page.business_logic.grant_total())).grid(
            row=si_no, column=4, sticky='NW')
        si_no += 1
        Label(self.top, text='Tax(10%)').grid(row=si_no, column=3, sticky='NW')
        Label(self.top, text=str(self.main_page.business_logic.tax())).grid(
            row=si_no, column=4, sticky='NW')
        si_no += 1
        Label(self.top, text='TOTAL').grid(row=si_no, column=3, sticky='NW')
        Label(self.top, text=str(self.main_page.business_logic.final_amount())).grid(
            row=si_no, column=4, sticky='NW')
        si_no += 2
        pay_now_btn = Button(self.top, text='Payment Done', command=self.on_pay_now_btn_click)
        pay_now_btn.grid(row=si_no, column=4, sticky='NW')

    def on_pay_now_btn_click(self):
        self.top.destroy()
        self.destroy()
        self.main_page.clear_all()

    def show(self):
        self.top.resizable(0, 0)
        self.top.grab_set()
        self.top.wait_window()


class Page1(Frame):

    def __init__(self, master):
        super().__init__(master, relief='flat', borderwidth=20)
        self.business_logic = BusinessLogic()
        self.init_ui()

    def chk_btn1_onclick(self):
        checked = self.chk_btn_var1.get()
        if checked:
            self.qty_entry1.configure(state=NORMAL)
        else:
            self.qty_entry1.configure(state=NORMAL)
        self.enable_btn()

    def chk_btn2_onclick(self):
        checked = self.chk_btn_var2.get()
        if checked:
            self.qty_entry2.configure(state=NORMAL)
        else:
            self.qty_entry2.configure(state=NORMAL)
        self.enable_btn()

    def chk_btn3_onclick(self):
        checked = self.chk_btn_var3.get()
        if checked:
            self.qty_entry3.configure(state=NORMAL)
        else:
            self.qty_entry3.configure(state=NORMAL)
        self.enable_btn()

    def chk_btn4_onclick(self):
        checked = self.chk_btn_var4.get()
        if checked:
            self.qty_entry4.configure(state=NORMAL)
        else:
            self.qty_entry4.configure(state=NORMAL)
        self.enable_btn()

    def chk_btn5_onclick(self):
        checked = self.chk_btn_var5.get()
        if checked:
            self.qty_entry5.configure(state=NORMAL)
        else:
            self.qty_entry5.configure(state=NORMAL)
        self.enable_btn()

    def enable_btn(self):
        if any((self.chk_btn_var1.get(), self.chk_btn_var2.get(),
                self.chk_btn_var3.get(), self.chk_btn_var4.get(),
                self.chk_btn_var5.get())):
            self.gen_receipt_btn.configure(state=NORMAL)
        else:
            self.gen_receipt_btn.configure(state=DISABLED)

    def qty_entry1_keybind(self, event):
        self.validate_for_int(event, self.qty_entry1)

    def qty_entry2_keybind(self, event):
        self.validate_for_int(event, self.qty_entry2)

    def qty_entry3_keybind(self, event):
        self.validate_for_int(event, self.qty_entry3)

    def qty_entry4_keybind(self, event):
        self.validate_for_int(event, self.qty_entry4)

    def qty_entry5_keybind(self, event):
        self.validate_for_int(event, self.qty_entry5)

    def validate_for_int(self, event, widget):
        val = widget.get()
        try:
            float(widget.get())
        except ValueError as verr:
            print(str(verr))
            if not event.char.isdigit():
                widget.delete(0, END)
                widget.insert(0, val[:-1])

    def _set_header(self):
        for col, item in enumerate(self.business_logic.header):
            Label(self, text=item,
                  font='Helvetica 12 bold').grid(row=0,
                                                 column=col, sticky='NW')

    def _set_body(self):
        self.chk_btn_var1 = BooleanVar()
        self.chk_btn_var2 = BooleanVar()
        self.chk_btn_var3 = BooleanVar()
        self.chk_btn_var4 = BooleanVar()
        self.chk_btn_var5 = BooleanVar()

        # order column
        self.chk_btn1 = Checkbutton(self, text="", variable=self.chk_btn_var1,
                                    command=self.chk_btn1_onclick)
        self.chk_btn1.grid(row=1, column=0, sticky='NW')
        self.chk_btn2 = Checkbutton(self, text="", variable=self.chk_btn_var2,
                                    command=self.chk_btn2_onclick)
        self.chk_btn2.grid(row=2, column=0, sticky='NW')
        self.chk_btn3 = Checkbutton(self, text="", variable=self.chk_btn_var3,
                                    command=self.chk_btn3_onclick)
        self.chk_btn3.grid(row=3, column=0, sticky='NW')
        self.chk_btn4 = Checkbutton(self, text="", variable=self.chk_btn_var4,
                                    command=self.chk_btn4_onclick)
        self.chk_btn4.grid(row=4, column=0, sticky='NW')
        self.chk_btn5 = Checkbutton(self, text="", variable=self.chk_btn_var5,
                                    command=self.chk_btn5_onclick)
        self.chk_btn5.grid(row=5, column=0, sticky='NW')

        # item column
        for row, item in enumerate(self.business_logic.items.keys()):
            _row = row + 1
            Label(self, text=f"{item}").grid(row=_row, column=1, sticky='NW')

        # unit price column
        for row, unit_price in enumerate(self.business_logic.items.values()):
            _row = row + 1
            Label(self, text=f"{unit_price}₹").grid(row=_row, column=2, sticky='NW')

        # quantity column
        self.qty_entry1 = Entry(self, state=DISABLED)
        self.qty_entry1.grid(row=1, column=3)
        self.qty_entry2 = Entry(self, state=DISABLED)
        self.qty_entry2.grid(row=2, column=3)
        self.qty_entry3 = Entry(self, state=DISABLED)
        self.qty_entry3.grid(row=3, column=3)
        self.qty_entry4 = Entry(self, state=DISABLED)
        self.qty_entry4.grid(row=4, column=3)
        self.qty_entry5 = Entry(self, state=DISABLED)
        self.qty_entry5.grid(row=5, column=3)
        self.qty_entry1.bind('<KeyRelease>', self.qty_entry1_keybind)
        self.qty_entry2.bind('<KeyRelease>', self.qty_entry2_keybind)
        self.qty_entry3.bind('<KeyRelease>', self.qty_entry3_keybind)
        self.qty_entry4.bind('<KeyRelease>', self.qty_entry4_keybind)
        self.qty_entry5.bind('<KeyRelease>', self.qty_entry5_keybind)

        self.gen_receipt_btn = Button(self, text="Generate Receipt",
                                      command=self.on_gen_receipt_btn_click)
        self.gen_receipt_btn.grid(row=8, column=2, padx=20, pady=20)
        self.gen_receipt_btn.configure(state=DISABLED)

        self.cancel_btn = Button(self, text="Clear", command=self.on_cancel_btn_click)
        self.cancel_btn.grid(row=8, column=3, padx=20, pady=20)

        Label(self, text='(Select your orders and then enter the quantities)',
              font='Helvetica 8 italic').grid(row=9, columnspan=4, sticky='NW')

    def init_ui(self):
        self.master.title(self.business_logic.title)
        self.pack(fill=None, expand=False)
        self._set_header()
        self._set_body()

    def on_cancel_btn_click(self):
        self.clear_all()

    def on_gen_receipt_btn_click(self):
        qty1 = self.qty_entry1.get().strip()
        qty2 = self.qty_entry2.get().strip()
        qty3 = self.qty_entry3.get().strip()
        qty4 = self.qty_entry4.get().strip()
        qty5 = self.qty_entry5.get().strip()
        if any((qty1, qty2, qty3, qty4, qty5)):

            for item, qty in zip(self.business_logic.items,
                                 (qty1, qty2, qty3, qty4, qty5)):
                if bool(qty):
                    self.business_logic.set(item, qty)

            Page2(self.master, self).show()
        else:
            messagebox.showwarning("Quantities", "Empty quantity fields")

    def clear_all(self):
        self.chk_btn1.deselect()
        self.chk_btn2.deselect()
        self.chk_btn3.deselect()
        self.chk_btn4.deselect()
        self.chk_btn5.deselect()

        self.qty_entry1.delete(0, END)
        self.qty_entry2.delete(0, END)
        self.qty_entry3.delete(0, END)
        self.qty_entry4.delete(0, END)
        self.qty_entry5.delete(0, END)

        self.qty_entry1.configure(state=DISABLED)
        self.qty_entry2.configure(state=DISABLED)
        self.qty_entry3.configure(state=DISABLED)
        self.qty_entry4.configure(state=DISABLED)
        self.qty_entry5.configure(state=DISABLED)
        self.gen_receipt_btn.configure(state=DISABLED)

        self.business_logic = BusinessLogic()


def main():

    root = Tk()
    root.resizable(0, 0)
    Page1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
