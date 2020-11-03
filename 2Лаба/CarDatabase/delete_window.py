from tkinter import *
from tkinter import messagebox
from base_controller import *
from tkinter import ttk


class DeleteWindow:
    def __init__(self, parent, width=500, height=250, x=250, y=130, title="Delete", resizable=(False, False)):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.root.resizable(resizable[0], resizable[1])

        self.delete_id_entry = Entry(self.root)

    def draw_car_widgets(self):
        Label(self.root, text="Id удаляемого элемента").pack()
        self.delete_id_entry.pack()

        Button(self.root, text="Ok",
               command=lambda: (delete_info("car_info", self.delete_id_entry.get()), self.root.destroy())).pack()

    def draw_officer_widgets(self):
        Label(self.root, text="Id удаляемого элемента").pack()
        self.delete_id_entry.pack()

        Button(self.root, text="Ok",
               command=lambda: (delete_info("officer_info", self.delete_id_entry.get()), self.root.destroy())).pack()

    def draw_inspection_widgets(self):
        Label(self.root, text="Id удаляемого элемента").pack()
        self.delete_id_entry.pack()

        Button(self.root, text="Ok",
               command=lambda: (delete_info("inspection_info", self.delete_id_entry.get()), self.root.destroy())).pack()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
