from tkinter import *
import mysql.connector
from input_window import InputWindow
from delete_window import DeleteWindow
from edit_window import EditWindow
from tkinter import ttk
from base_controller import *
from selection_window import Count
from selection_window import Table


def show_table(sql_table, window_table):
    database = connect()
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM {sql_table}")
    rows = cursor.fetchall()
    for row in rows:
        window_table.insert("", "end", values=row)


def update_table(sql_table, window_table):
    for i in window_table.get_children():
        window_table.delete(i)
    database = connect()
    cursor = database.cursor()
    cursor.execute(f"SELECT * FROM {sql_table}")
    rows = cursor.fetchall()
    for row in rows:
        window_table.insert("", "end", values=row)


class Window:
    def __init__(self, width=900, height=600, x=200, y=50, title="MyWindow", resizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("{}x{}+{}+{}".format(width, height, x, y))
        self.root.resizable(resizable[0], resizable[1])

        self.car_buttons_frame = Frame(self.root)
        self.officer_buttons_frame = Frame(self.root)
        self.inspection_buttons_frame = Frame(self.root)
        self.selection_buttons_frame = Frame(self.root)

        self.add_car_button = Button(self.car_buttons_frame, width=40, wraplength=300,
                                     text="Дабавить информацию о транспортных средствах и их владельцах",
                                     relief=RAISED, bd=5, bg="#ccffff",
                                     command=lambda: self.create_input_window(title="Input Car"))
        self.edit_car_button = Button(self.car_buttons_frame, width=40, wraplength=300,
                                      text="Редактировать информацию о транспортных средствах и их владельцах",
                                      relief=RAISED, bd=6, bg="#ccffff",
                                      command=lambda: self.create_edit_window(title="Edit car"))
        self.delete_car_info_button = Button(self.car_buttons_frame, width=40, wraplength=300,
                                             text="Удалить информацию о транспортных средствах и их владельцах",
                                             relief=RAISED, bd=6, bg="#ccffff",
                                             command=lambda: self.create_delete_window(title="Delete car"))
        self.add_officer_info_button = Button(self.officer_buttons_frame, width=40, wraplength=300,
                                              text="Добавить информацию о сотрудниках ГАИ",
                                              relief=RAISED, bd=6, bg="#ccffff",
                                              command=lambda: self.create_input_window(title="Input Officer"))
        self.edit_officer_info_button = Button(self.officer_buttons_frame, width=40, wraplength=300,
                                               text="Редактировать информацию о сотрудниках ГАИ",
                                               relief=RAISED, bd=6, bg="#ccffff",
                                               command=lambda: self.create_edit_window(title="Edit officer"))
        self.delete_officer_info_button = Button(self.officer_buttons_frame, width=40, wraplength=300,
                                                 text="Удалить информацию о сотрудниках ГАИ",
                                                 relief=RAISED, bd=6, bg="#ccffff",
                                                 command=lambda: self.create_delete_window(title="Delete officer"))
        self.add_inspection_info_button = Button(self.inspection_buttons_frame, width=40, wraplength=300,
                                                 text="Добавить информацию о проведенном техосмотре",
                                                 relief=RAISED, bd=6, bg="#ccffff",
                                                 command=lambda: self.create_input_window(
                                                     title="Input technical inspection"))
        self.edit_inspection_info_button = Button(self.inspection_buttons_frame, width=40, wraplength=300,
                                                  text="Редатировать информацию о проведенном техосмотре",
                                                  relief=RAISED, bd=6, bg="#ccffff",
                                                  command=lambda: self.create_edit_window(
                                                      title="Edit technical inspection"))
        self.delete_inspection_info_button = Button(self.inspection_buttons_frame, width=40, wraplength=300,
                                                    text="Удалить информацию о проведенном техосмотре",
                                                    relief=RAISED, bd=6, bg="#ccffff",
                                                    command=lambda: self.create_delete_window(
                                                        title="Delete technical inspection"))

        self.count_number_of_cars_during_a_period_button = Button(self.selection_buttons_frame, width=40,
                                                                  wraplength=300,
                                                                  text="Расчет количества автомобилей, прошедших техосмотр за заданный промежуток времени",
                                                                  relief=RAISED, bd=6, bg="#ccffff",
                                                                  command=lambda: self.create_select_window(
                                                                      title="Count")
                                                                  )
        self.list_of_officers_button = Button(self.selection_buttons_frame, width=40, wraplength=300,
                                              text="Просмотр списка сотрудников ГАИ, проводивших осмотр на заданную дату",
                                              relief=RAISED, bd=6, bg="#ccffff",
                                              command=lambda: self.create_select_window(title="List of officers"))
        self.inspection_history_of_the_car_button = Button(self.selection_buttons_frame, width=40, wraplength=300,
                                                           text="Просмотр истории прохождения осмотров заданным автомобилем",
                                                           relief=RAISED, bd=6, bg="#ccffff",
                                                           command=lambda: self.create_select_window(
                                                               title="History of the car"))

        self.cars_frame = LabelFrame(self.root, text="Cars")
        self.officers_frame = LabelFrame(self.root, text="Officers")
        self.inspection_frame = LabelFrame(self.root, text="Inspection")

        self.table_cars = ttk.Treeview(self.cars_frame, height=3, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
                                       show="headings")
        self.table_officers = ttk.Treeview(self.officers_frame, height=3, columns=(1, 2, 3, 4), show="headings")
        self.table_inspection = ttk.Treeview(self.inspection_frame, height=3, columns=(1, 2, 3, 4, 5), show="headings")

        self.table_cars.heading(1, text="id", anchor=W)
        self.table_cars.heading(2, text="Госномер авто", anchor=W)
        self.table_cars.heading(3, text="Номер двигателя", anchor=W)
        self.table_cars.heading(4, text="Цвет", anchor=W)
        self.table_cars.heading(5, text="Марка", anchor=W)
        self.table_cars.heading(6, text="Номер технического пасспорта", anchor=W)
        self.table_cars.heading(7, text="Номер водительского удостоверения", anchor=W)
        self.table_cars.heading(8, text="ФИО владельца", anchor=W)
        self.table_cars.heading(9, text="Адрес прописки", anchor=W)
        self.table_cars.heading(10, text="Год рождения", anchor=W)

        self.table_officers.heading(1, text="id", anchor=W)
        self.table_officers.heading(2, text="ФИО сотрудника ГАИ", anchor=W)
        self.table_officers.heading(3, text="Должность сотрудника ГАИ", anchor=W)
        self.table_officers.heading(4, text="Звание сотрудника ГАИ", anchor=W)

        self.table_inspection.heading(1, text="id", anchor=W)
        self.table_inspection.heading(2, text="ФИО сотрудника ГАИ", anchor=W)
        self.table_inspection.heading(3, text="Госномер авто", anchor=W)
        self.table_inspection.heading(4, text="Дата прохождения осмотра", anchor=W)
        self.table_inspection.heading(5, text="Результат осмотра", anchor=W)

        self.horizontal_car_scroll = ttk.Scrollbar(self.cars_frame, orient="horizontal", command=self.table_cars.xview)
        self.vertical_car_scroll = ttk.Scrollbar(self.cars_frame, orient="vertical", command=self.table_cars.yview)
        self.table_cars.configure(xscrollcommand=self.horizontal_car_scroll.set)
        self.table_cars.configure(yscrollcommand=self.vertical_car_scroll.set)

        self.horizontal_officer_scroll = ttk.Scrollbar(self.officers_frame, orient="horizontal",
                                                       command=self.table_officers.xview)
        self.vertical_officer_scroll = ttk.Scrollbar(self.officers_frame, orient="vertical",
                                                     command=self.table_officers.yview)
        self.table_officers.configure(xscrollcommand=self.horizontal_officer_scroll.set)
        self.table_officers.configure(yscrollcommand=self.vertical_officer_scroll.set)

        self.horizontal_inspection_scroll = ttk.Scrollbar(self.inspection_frame, orient="horizontal",
                                                          command=self.table_inspection.xview)
        self.vertical_inspection_scroll = ttk.Scrollbar(self.inspection_frame, orient="vertical",
                                                        command=self.table_inspection.yview)
        self.table_inspection.configure(xscrollcommand=self.horizontal_inspection_scroll.set)
        self.table_inspection.configure(yscrollcommand=self.vertical_inspection_scroll.set)

    def run(self):
        show_table("car_info", self.table_cars)
        show_table("officer_info", self.table_officers)
        show_table("inspection_info", self.table_inspection)
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.cars_frame.pack(anchor=N)
        self.car_buttons_frame.pack(pady=7)

        self.horizontal_car_scroll.pack(fill=BOTH)
        self.vertical_car_scroll.pack(side=RIGHT, fill=BOTH, expand=False)

        self.add_car_button.grid(row=0, column=0, padx=5)
        self.edit_car_button.grid(row=0, column=1)
        self.delete_car_info_button.grid(row=0, column=2)

        self.officers_frame.pack(anchor=W, fill=X)
        self.officer_buttons_frame.pack(anchor=W, pady=10)

        self.horizontal_officer_scroll.pack(fill=BOTH)
        self.vertical_officer_scroll.pack(side=RIGHT, fill=BOTH, expand=False)

        self.add_officer_info_button.grid(row=0, column=0)
        self.edit_officer_info_button.grid(row=0, column=1)
        self.delete_officer_info_button.grid(row=0, column=2)

        self.inspection_frame.pack(anchor=W)
        self.inspection_buttons_frame.pack(anchor=W, pady=7)

        self.horizontal_inspection_scroll.pack(fill=BOTH)
        self.vertical_inspection_scroll.pack(side=RIGHT, fill=BOTH, expand=False)

        self.add_inspection_info_button.grid(row=0, column=0)
        self.edit_inspection_info_button.grid(row=0, column=1)
        self.delete_inspection_info_button.grid(row=0, column=2)

        self.table_cars.pack()
        self.table_officers.pack()
        self.table_inspection.pack()

        self.selection_buttons_frame.pack()

        self.count_number_of_cars_during_a_period_button.grid(row=0, column=0)
        self.list_of_officers_button.grid(row=0, column=1)
        self.inspection_history_of_the_car_button.grid(row=0, column=2)

    def create_input_window(self, width=500, height=250, x=400, y=190, title="Input", resizable=(False, False)):
        input_window = InputWindow(self.root, width, height, x, y, title, resizable)
        if title == "Input Car":
            input_window.draw_car_widgets()
        elif title == "Input Officer":
            input_window.draw_officer_widgets()
        elif title == "Input technical inspection":
            input_window.draw_inspection_widgets()

        input_window.grab_focus()
        if title == "Input Car":
            update_table("car_info", self.table_cars)
        elif title == "Input Officer":
            update_table("officer_info", self.table_officers)
        elif title == "Input technical inspection":
            update_table("inspection_info", self.table_inspection)

    def create_delete_window(self, width=500, height=250, x=400, y=190, title="Delete", resizable=(False, False)):
        delete_window = DeleteWindow(self.root, width, height, x, y, title, resizable)
        if title == "Delete car":
            delete_window.draw_car_widgets()
        elif title == "Delete officer":
            delete_window.draw_officer_widgets()
        elif title == "Delete technical inspection":
            delete_window.draw_inspection_widgets()
        delete_window.grab_focus()

        if title == "Delete car":
            update_table("car_info", self.table_cars)
        elif title == "Delete officer":
            update_table("officer_info", self.table_officers)
        elif title == "Delete technical inspection":
            update_table("inspection_info", self.table_inspection)

    def create_edit_window(self, width=600, height=250, x=400, y=190, title="Edit", resizable=(False, False)):
        edit_window = EditWindow(self.root, width, height, x, y, title, resizable)
        if title == "Edit car":
            edit_window.draw_car_widgets()
        elif title == "Edit officer":
            edit_window.draw_officer_widgets()
        elif title == "Edit technical inspection":
            edit_window.draw_inspection_widgets()
        edit_window.grab_focus()

        if title == "Edit car":
            update_table("car_info", self.table_cars)
        elif title == "Edit officer":
            update_table("officer_info", self.table_officers)
        elif title == "Edit technical inspection":
            update_table("inspection_info", self.table_inspection)

    def create_select_window(self, width=500, height=250, x=250, y=130, title="Count", resizable=(False, False)):
        if title == "Count":
            count_window = Count(self.root, width, height, x, y, title, resizable)
            count_window.draw_widgets()
            count_window.grab_focus()
        elif title == "List of officers":
            list_of_officers = Table(self.root, width, height, x, y, title, resizable)
            list_of_officers.draw_officers_widgets()
            list_of_officers.grab_focus()
        elif title == "History of the car":
            history_of_car = Table(self.root, width, height, x, y, title, resizable)
            history_of_car.draw_car_widgets()
            history_of_car.grab_focus()

#
# if __name__ == "__main__":
#     window = Window(title="CarDatabase")
#     window.run()
