from tkinter import *
from tkinter import messagebox
from base_controller import *


class EditWindow:
    def __init__(self, parent, width=500, height=250, x=250, y=130, title="Delete", resizable=(False, False)):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.root.resizable(resizable[0], resizable[1])

        self.car_number_entry = Entry(self.root)
        self.engine_number_entry = Entry(self.root)
        self.car_color_entry = Entry(self.root)
        self.car_brand_entry = Entry(self.root)
        self.technical_passport_number_entry = Entry(self.root)
        self.driver_license_number_entry = Entry(self.root)
        self.owner_name_entry = Entry(self.root)
        self.address_entry = Entry(self.root)
        self.year_of_birth_entry = Entry(self.root)

        self.officer_name_entry = Entry(self.root)
        self.officer_position_entry = Entry(self.root)
        self.officer_rank_entry = Entry(self.root)

        self.date_of_inspection_entry = Entry(self.root)
        self.result_of_inspection_entry = Entry(self.root)

        self.id_entry = Entry(self.root)

    def draw_car_widgets(self):
        Label(self.root, text="id записи которую хотите изменить").grid(row=0, column=0)
        self.id_entry.grid(row=1, column=0)
        Label(self.root, text="Введите новые данные").grid(row=0, column=1)
        Label(self.root, text="Госномер авто").grid(row=1, column=1)
        self.car_number_entry.grid(row=2, column=1)
        Label(self.root, text="Номер двигателя").grid(row=3, column=1)
        self.engine_number_entry.grid(row=4, column=1)
        Label(self.root, text="Цвет").grid(row=5, column=1)
        self.car_color_entry.grid(row=6, column=1)
        Label(self.root, text="Марка").grid(row=7, column=1)
        self.car_brand_entry.grid(row=8, column=1)
        Label(self.root, text="Номер технического пасспорта").grid(row=1, column=2)
        self.technical_passport_number_entry.grid(row=2, column=2)
        Label(self.root, text="Номер водительского удостоверения").grid(row=3, column=2)
        self.driver_license_number_entry.grid(row=4, column=2)
        Label(self.root, text="ФИО владельца").grid(row=5, column=2)
        self.owner_name_entry.grid(row=6, column=2)
        Label(self.root, text="Адрес").grid(row=7, column=2)
        self.address_entry.grid(row=8, column=2)
        Label(self.root, text="Год рождения").grid(row=9, column=2)
        self.year_of_birth_entry.grid(row=10, column=2)

        Button(self.root, width=10, text="OK",
               command=lambda: (
                   edit_car_info(self.id_entry.get(), self.car_number_entry.get(), self.engine_number_entry.get(),
                                 self.car_color_entry.get(),
                                 self.car_brand_entry.get(), self.technical_passport_number_entry.get(),
                                 self.driver_license_number_entry.get(), self.owner_name_entry.get(),
                                 self.address_entry.get(), self.year_of_birth_entry.get()),
                   self.root.destroy())).grid(row=10,
                                              column=0)

    def draw_officer_widgets(self):
        Label(self.root, text="id записи которую хотите изменить").grid(row=0, column=0)
        self.id_entry.grid(row=1, column=0)
        Label(self.root, text="Введите новые данные").grid(row=0, column=1)
        Label(self.root, text="ФИО сотрудника ГАИ").grid(row=1, column=1)
        self.officer_name_entry.grid(row=2, column=1)
        Label(self.root, text="Должность сотрудника ГАИ").grid(row=3, column=1)
        self.officer_position_entry.grid(row=4, column=1)
        Label(self.root, text="Звание сотрудника ГАИ").grid(row=5, column=1)
        self.officer_rank_entry.grid(row=6, column=1)

        Button(self.root, width=10, text="Ok",
               command=lambda: (edit_officer_info(self.id_entry.get(), self.officer_name_entry.get(),
                                                  self.officer_position_entry.get(),
                                                  self.officer_rank_entry.get()), self.root.destroy())).grid(row=7,
                                                                                                             column=0)

    def draw_inspection_widgets(self):
        Label(self.root, text="id записи которую хотите изменить").grid(row=0, column=0)
        self.id_entry.grid(row=1, column=0)
        Label(self.root, text="Введите новые данные").grid(row=0, column=1)
        Label(self.root, text="ФИО сотрудника ГАИ").grid(row=1, column=1)
        self.officer_name_entry.grid(row=2, column=1)
        Label(self.root, text="Госномер авто").grid(row=3, column=1)
        self.car_number_entry.grid(row=4, column=1)
        Label(self.root, text="Дата осмотра").grid(row=5, column=1)
        self.date_of_inspection_entry.grid(row=6, column=1)
        Label(self.root, text="Результат осмотра").grid(row=7, column=1)
        self.result_of_inspection_entry.grid(row=8, column=1)

        Button(self.root, text="Ok",
               command=lambda: (edit_inspection_info(self.id_entry.get(), self.officer_name_entry.get(),
                                                     self.car_number_entry.get(), self.date_of_inspection_entry.get(),
                                                     self.result_of_inspection_entry.get()), self.root.destroy())).grid(
            row=8, column=0)

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
