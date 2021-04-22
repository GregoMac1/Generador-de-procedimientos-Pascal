import PySimpleGUI as sg
from src.windows import main_window
from src.data.lista_de_datos import lista_de_procedimientos
from src.components import fields_input

def start():
    window = main_window.build()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED,'Exit','-EXIT-'):
            break

        try:
            seleccionado = window['-OPCIONES-'].get_indexes()[0]        
            actualizar_elementos(window,seleccionado)
        except IndexError:
            pass

        if event in ('Seleccionar','-SELECT-'):
            try:
                if lista_de_procedimientos[seleccionado]['campos_requeridos'] == 'Ninguno':
                    sg.popup_scrolled(lista_de_procedimientos[seleccionado]['funcion'](),title='Resultado',font=('Monaco',16))
                else:
                    window.hide()
                    fields_input.start(lista_de_procedimientos[seleccionado]['campos_requeridos'],seleccionado)
                    window.un_hide()
            except (IndexError,UnboundLocalError):
                sg.popup('Error. No hay ningún procedimiento seleccionado.',title='Error',font=('Bahnschrift SemiLight',15))

    window.close()

def actualizar_elementos(window,seleccionado):
    try:
        window['-DESCRIPCIONES-'].update(lista_de_procedimientos[seleccionado].get('descripcion'))        
    except IndexError:
        pass
    try:
        window['-ENCABEZADOS-'].update(lista_de_procedimientos[seleccionado].get('encabezado'))
    except IndexError:
        pass
    try:
        window['-CAMPOS_REQUERIDOS-'].update(lista_de_procedimientos[seleccionado].get('campos_requeridos'))
    except IndexError:
        pass
