from os import system
system("cls")
import flet as ft
import MySQLdb as mysql

db= mysql.connect(host="localhost",user="root",
                  database="ingreso")

cursor = db.cursor()

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nombre_txt = ft.TextField(value="",hint_text="Nombre", text_align=ft.TextAlign.CENTER, width=300)
    apellido_txt = ft.TextField(value="", hint_text="Apellido", text_align=ft.TextAlign.CENTER, width=300)
    dni_txt = ft.TextField(value="", hint_text="DNI", text_align=ft.TextAlign.CENTER, width=300)
    patente_txt = ft.TextField(value="", hint_text="Patente", text_align=ft.TextAlign.CENTER, width=300)

    def minus_click(e):
        print(type(nombre_txt.value))
        db_query = "INSERT INTO ingresos(nombre,apellido,dni,patente) VALUES(%s,%s,%s,%s)"
        cursor.execute(db_query,(nombre_txt.value,apellido_txt.value,dni_txt.value,patente_txt.value))
        db.commit()
    
        page.update()

    page.add(
        ft.Column(
            [
                nombre_txt,
                apellido_txt,
                dni_txt,
                patente_txt,
                ft.IconButton(ft.icons.SEND_ROUNDED, on_click=minus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)