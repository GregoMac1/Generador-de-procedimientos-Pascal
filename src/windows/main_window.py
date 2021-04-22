import PySimpleGUI as sg
from src.data.lista_de_datos import lista_de_procedimientos

sg.theme('DarkBlue13')

version = 2.0

texto_bienvenida = '''Este programa genera los procedimientos más usuales de la materia FOD, permitiendo al usuario obtener un resultado personalizado según los nombres de variables y tipos que use.

Al seleccionar una opción de la lista de opciones, verá los campos que necesita ingresar para obtener el módulo seleccionado.'''

lista_de_opciones = []
for i in range(len(lista_de_procedimientos)):
    lista_de_opciones.append(lista_de_procedimientos[i]['nombre'])

def build():
    col_layout = [
        [sg.Text('Descripción:')],
        [sg.Text(size=(40,3),key='-DESCRIPCIONES-', background_color='#324F7B')],
        [sg.Text('Encabezado:')],
        [sg.Text(size=(40,3),key='-ENCABEZADOS-', background_color='#324F7B',font=('Monaco',14))],
        [sg.Text('Campos requeridos:')], 
        [sg.Text(size=(40,3),key='-CAMPOS_REQUERIDOS-', background_color='#324F7B')]
    ]

    layout = [
        [sg.Text('Generador de procedimientos de Pascal',size=(33,1),justification='center',font=('GeoSlab703 Md BT',40))],
        [sg.Text(texto_bienvenida,size=(76,5),justification='center')],        
        [sg.Listbox(lista_de_opciones, size=(30,14), key='-OPCIONES-', enable_events=True, select_mode='LISTBOX_SELECT_MODE_SINGLE'), sg.Column(col_layout)],
        [sg.Button('Seleccionar',key='-SELECT-'), sg.Exit('Salir',key='-EXIT-')]
    ]

    window = sg.Window(f'Generador de procedimientos de Pascal v{version}',layout,resizable=True,element_justification='center',font=('Bahnschrift SemiLight',15))

    return window
