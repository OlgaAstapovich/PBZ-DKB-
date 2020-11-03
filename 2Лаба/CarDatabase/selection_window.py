from tkinter import *
from tkinter import ttk
from base_controller import *


class Count:
    def __init__(self, parent, width=500, height=250, x=250, y=130, title="Select", resizable=(False, False)):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.root.resizable(resizable[0], resizable[1])

        self.start_date_entry = Entry(self.root)
        self.end_date_entry = Entry(self.root)


    def draw_widgets(self):
        Label(self.root, text="Дата начала периода").grid(row=0, column=0)
        self.start_date_entry.grid(row=1, column=0)
        Label(self.root, text="Дата окончания периода").grid(row=0, column=1)
        self.end_date_entry.grid(row=1, column=1)

        Button(self.root, text="Ok", command=lambda: count_number_of_cars_during_a_period(self.start_date_entry.get(),
                                                                                          self.end_date_entry.get())).grid(
            row=2, columnspan=2)

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

class Table:
    def __init__(self, parent, width=500, height=250, x=250, y=130, title="Select", resizable=(False, False)):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.root.resizable(resizable[0], resizable[1])

        self.input = Entry(self.root)
        self.table_list_of_officers = ttk.Treeview(self.root, columns=1, show="headings")
        self.history_of_car = ttk.Treeview(self.root, columns=(1, 2, 3), show="headings")

    def draw_officers_widgets(self):
        Label(self.root, text="Дата").pack()
        self.input.pack()
        Button(self.root, text="Ok", command=lambda: list_of_officers(self.input.get(), self.table_list_of_officers)).pack()
        self.table_list_of_officers.pack()

    def draw_car_widgets(self):
        Label(self.root, text="Госномер авто").pack()
        self.input.pack()
        Button(self.root, text="Ok", command=lambda: history_of_car(self.input.get(), self.history_of_car)).pack()
        self.history_of_car.pack()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
