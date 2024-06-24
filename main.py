from os import system
system("cls")
import flet as ft
import MySQLdb as mysql
from datetime import datetime


try:
    db= mysql.connect(host="localhost",user="root",
                    database="ingreso")
except:
    print("Error en la conexion de la base de datos")



cursor = db.cursor()


def main(page: ft.Page):

    border = 23
    nombre_txt = ft.TextField(value="",hint_text="Nombre", text_align=ft.TextAlign.CENTER, width=300, border_radius=border, text_style=ft.TextStyle(weight=ft.FontWeight.W_700))
    apellido_txt = ft.TextField(value="", hint_text="Apellido", text_align=ft.TextAlign.CENTER, width=300, border_radius=border, text_style=ft.TextStyle(weight=ft.FontWeight.W_700))
    dni_txt = ft.TextField(value="", hint_text="DNI", text_align=ft.TextAlign.CENTER, width=300, border_radius=border, text_style=ft.TextStyle(weight=ft.FontWeight.W_700))
    patente_txt = ft.TextField(value="", hint_text="Patente", text_align=ft.TextAlign.CENTER, width=300,height=100 , border_radius=border, text_style=ft.TextStyle(weight=ft.FontWeight.W_700))
    dd = ft.Dropdown(
        label="Area",
        hint_text="¿A que area se dirige?",
        width=200,
        options=[
            ft.dropdown.Option("Compras"),
            ft.dropdown.Option("Ventas"),
            ft.dropdown.Option("Atencion al cliente"),
            ft.dropdown.Option("Tengo una reunion"),
        ],
    )
    def click_ingreso(e):
        ingreso = True
        nombre_txt.disabled = False
        apellido_txt.disabled = False
        dni_txt.disabled = False
        patente_txt.disabled = False
        dd.disabled = False
        page.update()


    def click_egreso(e):
        ingreso = False
        nombre_txt.disabled = True
        apellido_txt.disabled = True
        patente_txt.disabled = True
        dd.disabled = True
        page.update()

    ingreso_boton = ft.TextButton(text="Ingreso",on_click=click_ingreso,width=160)
    egreso_boton = ft.TextButton("Egreso",on_click=click_egreso)

    def submit(e):
        if nombre_txt.disabled == True:
            now = datetime.now()
            db_query2 = "UPDATE ingresos SET hora_salida=%s WHERE dni=%s"
            cursor.execute(db_query2,(now,dni_txt.value))
            db.commit()
            dni_txt.value = ""
            print('ASdAF')
            page.update()
        else:
            db_query = "INSERT INTO ingresos(nombre,apellido,dni,patente,area) VALUES(%s,%s,%s,%s,%s)"
            cursor.execute(db_query,(nombre_txt.value,apellido_txt.value,dni_txt.value,patente_txt.value,dd.value))
            db.commit()
            nombre_txt.value = ""
            apellido_txt.value = ""
            dni_txt.value = ""
            patente_txt.value = ""
            dd.value=""
            page.update()

    container = ft.Container(
        ft.Row([
            ft.Column([
                ft.Row([
                    ingreso_boton,
                    egreso_boton,
                ]),
                nombre_txt,
                apellido_txt, 
                dni_txt, 
                patente_txt,
                dd,
                ft.FilledButton(text="Enviar", width=200,height=70,on_click=submit)
                ], alignment = "center"
            )
        ], alignment = ft.MainAxisAlignment.CENTER),
        border_radius=10,
        width=350,
        height=720,
        bgcolor=ft.colors.WHITE,    
)


    page.title = "Ingreso"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(
        container
    )
    

ft.app(main)