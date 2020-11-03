import mysql.connector
from tkinter import messagebox


def connect():
    database = mysql.connector.connect(
        user='root',
        password='paswrd',
        host='localhost',
        database='technical_inspection')
    return database


def add_officer_info(officer_name, officer_position, officer_rank):
    try:
        database = connect()
        my_cursor = database.cursor()
        my_cursor.execute("INSERT INTO officer_info(officer_name, officer_position, officer_rank) VALUES (%s,%s, %s)",
                          (officer_name, officer_position, officer_rank))
        database.commit()

        database.close()
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")


def add_car_info(car_number, engine_number, car_color, car_brand, technical_passport_number, driver_license_number,
                 owner_name, address, year_of_birth):
    try:
        database = connect()
        my_cursor = database.cursor()

        my_cursor.execute(
            "INSERT INTO car_info(car_number, engine_number, car_color, car_brand, technical_passport_number, driver_license_number,"
            "owner_name, address, year_of_birth) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (car_number, engine_number, car_color, car_brand, technical_passport_number,
             driver_license_number, owner_name, address, year_of_birth))
        database.commit()

        database.close()
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")


def add_inspection_info(officer_name, car_number, date_of_inspection, result_of_inspection):
    try:
        database = connect()
        my_cursor = database.cursor()
        my_cursor.execute(
            "INSERT INTO inspection_info(officer_name, car_number, date_of_inspection, result_of_inspection) VALUES (%s,%s, %s, %s)",
            (officer_name, car_number, date_of_inspection, result_of_inspection))
        database.commit()

        database.close()
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")


def edit_car_info(edit_id, car_number, engine_number, car_color, car_brand, technical_passport_number,
                  driver_license_number,
                  owner_name, address, year_of_birth):
    try:
        database = connect()
        my_cursor = database.cursor()
        my_cursor.execute(
            "UPDATE car_info "
            f"SET car_number='{car_number}', engine_number='{engine_number}', car_color='{car_color}', "
            f"car_brand='{car_brand}', technical_passport_number='{technical_passport_number}', "
            f"driver_license_number='{driver_license_number}', owner_name='{owner_name}', address='{address}',"
            f"year_of_birth='{year_of_birth}' "
            f"WHERE id = {int(edit_id)}"
        )
        database.commit()
        database.close()
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")


def edit_officer_info(edit_id, officer_name, officer_position, officer_rank):
    try:
        database = connect()
        my_cursor = database.cursor()
        my_cursor.execute(
            "UPDATE officer_info "
            f"SET officer_name='{officer_name}', officer_position='{officer_position}', officer_rank='{officer_rank}' "
            f"WHERE id={int(edit_id)}"
        )
        database.commit()
        database.close()
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")


def edit_inspection_info(edit_id, officer_name, car_number, date_of_inspection, result_of_inspection):
    try:
        database = connect()
        my_cursor = database.cursor()
        my_cursor.execute(
            "UPDATE inspection_info "
            f"SET officer_name='{officer_name}', car_number='{car_number}', "
            f"date_of_inspection='{date_of_inspection}', result_of_inspection='{result_of_inspection}' "
            f"WHERE id={int(edit_id)}"
        )
        database.commit()
        database.close()
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")


def delete_info(table, deleted_id):
    try:
        database = connect()
        my_cursor = database.cursor()
        my_cursor.execute(f"DELETE FROM {table} WHERE id={deleted_id}")
        database.commit()
        my_cursor.execute(f"UPDATE {table} SET id =id-1 WHERE id>={deleted_id}")
        database.commit()
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")


def count_number_of_cars_during_a_period(start_date, end_date):
    try:
        database = connect()
        my_cursor = database.cursor()
        my_cursor.execute(
            f"SELECT COUNT(DISTINCT car_number) FROM inspection_info "
            f"WHERE date_of_inspection >='{start_date}' and date_of_inspection<='{end_date}'")
        for x in my_cursor:
            message = x[0]
        messagebox.showinfo(title="Count", message=f"Количество авто прошедших техосмотр за данный период {message}")
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")


def list_of_officers(date, table):
    try:
        for i in table.get_children():
            table.delete(i)
        database = connect()
        my_cursor = database.cursor()
        my_cursor.execute(
            f"SELECT officer_name FROM inspection_info WHERE date_of_inspection ='{date}'")
        rows = my_cursor.fetchall()
        for row in rows:
            table.insert("", "end", values=row)
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")


def history_of_car(car_number, table):
    try:
        for i in table.get_children():
            table.delete(i)
        database = connect()
        my_cursor = database.cursor()
        my_cursor.execute(
            f"SELECT officer_name, date_of_inspection, result_of_inspection FROM inspection_info WHERE car_number ='{car_number}' ")
        rows = my_cursor.fetchall()
        for row in rows:
            table.insert("", "end", values=row)
    except:
        messagebox.showinfo(title="Error", message="Sorry!\n Something wrong!")

