from tkinter import (Tk, Radiobutton, Toplevel, IntVar, Listbox, ACTIVE,
                     messagebox, DISABLED)
from tkinter.ttk import Frame, Button, Label

from logic import MLLogic


class Page2(Frame):

    def __init__(self, parent, main_page):
        super().__init__(parent)
        self.top = Toplevel(parent, relief='flat', borderwidth=20)
        self.main_page = main_page
        self.pack(fill=None, expand=False)
        self.set_header()
        self.set_body()

    def set_header(self):
        header = f'Recommendations ({self.main_page.business_logic.selected_choice} appliances)'
        Label(self.top, text=header,
              font='Helvetica 12 bold').grid(row=0, columnspan=3, sticky='NW')

    def create_widgets(self, frame, recommendation):
        Label(frame, text='Item', font='Helvetica 8 bold').grid(row=1, column=0, sticky='NW')
        Label(frame, text='Unit Price', font='Helvetica 8 bold').grid(row=1, column=1, sticky='NW')
        Label(frame, text='Quanity', font='Helvetica 8 bold').grid(row=1, column=2, sticky='NW')
        Label(frame, text='Price', font='Helvetica 8 bold').grid(row=1, column=3, sticky='NW')
        row_number = 2
        sum = 0
        for item in recommendation:
            Label(frame, text=item).grid(row=row_number, column=0, sticky='NW')
            qty, up = recommendation[item]
            Label(frame, text=up).grid(row=row_number, column=1, sticky='NW')
            Label(frame, text=qty).grid(row=row_number, column=2, sticky='NW')
            price = int(qty) * int(up)
            sum += price
            Label(frame, text=str(price)).grid(row=row_number, column=3, sticky='NW')
            row_number += 1
        Label(frame, text='Cost').grid(row=row_number, column=2, sticky='NW')
        Label(frame, text=str(sum)).grid(row=row_number, column=3, sticky='NW')
        row_number += 1
        Label(frame, text='Tax(10%)').grid(row=row_number, column=2, sticky='NW')
        tax = (sum * 10) / 100.0
        Label(frame, text=str(tax)).grid(row=row_number, column=3, sticky='NW')
        row_number += 1
        Label(frame, text='TOTAL').grid(row=row_number, column=2, sticky='NW')
        total = sum + tax
        Label(frame, text=str(total)).grid(row=row_number, column=3, sticky='NW')
        row_number += 1
        Button(frame, text='Select', command=self.on_pay_now_btn_click).grid(
            row=row_number, column=3, sticky='NW')

    def on_pay_now_btn_click(self):
        print('Clicked')
        self.top.destroy()
        self.destroy()
        self.main_page.radio_btn_var.set(3)
        self.main_page.item_lst_box.delete(0, 'end')

    def set_body(self):
        column = 1
        row = 2
        for recommendation in self.main_page.business_logic.get_recommendations():
            frame = Frame(self.top, relief='groove', borderwidth=10)
            frame.grid(row=row, column=column, padx=30, pady=4)
            self.create_widgets(frame, recommendation)
            column += 1
            if column > 3:
                row += 1
                column = 1

    def show(self):
        self.top.resizable(0, 0)
        self.top.grab_set()
        self.top.wait_window()


class Page1(Frame):

    def on_recommend_btn_click(self):
        selected_index = self.item_lst_box.curselection()
        user_preferences = [self.item_lst_box.get(indx) for indx in selected_index]
        print(f'User preferences are {user_preferences}')
        if len(user_preferences) > 3:
            messagebox.showwarning("Warning", "Currently doesnt support for than 3 preferences")
        else:
            self.business_logic.set_preferences(user_preferences)
            Page2(self.master, self).show()

    def get_appliances(self):
        selected = self.radio_btn_var.get()
        print(f'Selected option is {selected}')
        if selected in (0, 1):
            self.business_logic.set_choice(selected)
            for index, item in enumerate(
                    self.business_logic.items[
                        self.business_logic.selected_choice]):
                self.item_lst_box.insert(index, item)
            self.recommend_btn.configure(state=ACTIVE)
        else:
            self.recommend_btn.configure(state=DISABLED)
            self.item_lst_box.delete(0, 'end')

    def __init__(self, master):
        super().__init__(master, relief='flat', borderwidth=40)
        self.business_logic = MLLogic()
        self.radio_btn_var = IntVar()
        self.master.title(self.business_logic.title)
        self.pack(fill=None, expand=False)
        Label(self,
              text="Select the type of appliances you want to buy").grid(
            row=1, columnspan=2, sticky='NW')
        for index, appliance_type in enumerate(
                self.business_logic.appliance_choices):
            rdo_btn = Radiobutton(self, text=appliance_type, variable=self.radio_btn_var,
                                  value=index, command=self.get_appliances)
            rdo_btn.select()
            rdo_btn.grid(row=index+2, column=2)
        Label(self, text="Preferences").grid(row=7, columnspan=2, sticky='NW')
        self.item_lst_box = Listbox(self, selectmode='multiple')
        self.item_lst_box.delete(0,'end')
        self.item_lst_box.grid(row=7, column=2)
        self.recommend_btn = Button(self, text='Recommend',
                                    command=self.on_recommend_btn_click)
        self.recommend_btn.grid(row=9, column=2, sticky='NW')
        self.recommend_btn.configure(state=DISABLED)


def main():

    root = Tk()
    root.resizable(0, 0)
    Page1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
