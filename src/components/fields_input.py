import PySimpleGUI as sg
from src.windows import fields_input
from src.data.lista_de_datos import lista_de_procedimientos

def start(campos_requeridos,seleccionado):
    window = fields_input.build(campos_requeridos)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED,'Exit','-EXIT-'):
            break

        if event in ('Generar','-CREATE-'):
            campos_ingresados = values['-CAMPOS_INGRESADOS-'].split(',')
            campos_ingresados = [campo.strip(' ') for campo in campos_ingresados]
            if 'Campos del registro' in campos_requeridos:
                campos_registro = values['-CAMPOS_REGISTRO-'].split(',')
                campos_registro = [campo.strip(' ') for campo in campos_registro]

            try:                    
                if 'Campos del registro' in campos_requeridos:
                    procedimiento_resultado = lista_de_procedimientos[seleccionado]['funcion'](campos_ingresados,campos_registro)
                    sg.popup_scrolled(procedimiento_resultado,title='Resultado',font=('Monaco',16))
                else:
                    procedimiento_resultado = lista_de_procedimientos[seleccionado]['funcion'](campos_ingresados)
                    sg.popup_scrolled(procedimiento_resultado,title='Resultado',font=('Monaco',16))
            except IndexError:
                    sg.popup('Error en el ingreso de los campos.',title='Error')

    window.close()
