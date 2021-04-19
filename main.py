import PySimpleGUI as sg
from modulos import *

sg.theme('DefaultNoMoreNagging')

opciones = ['LeerRegistro',
            'RegATexto',
            'Minimo',
            'AgregarListaAlFinal',
            'AgregarListaAdelante',
            'InsertarOrdenadoLista',
            'MergeAcumulador']

descripciones = [
'''Solicita el ingreso por teclado de los campos del registro.
procedure leer (var nombreRegistro:tipoRegistro);''',
'''Escribe todos los campos de un registro en un archivo de texto, cada campo en una nueva linea.
procedure regATexto (var nombreRegistro:tipoRegistro; var nombreArchivoTexto:text);
''',
'Calcula el minimo.',
'h','o','l','a'
]

layout = [[sg.Text('Nombre del registro: ')],
        [sg.Input(key='nombre_registro')],
        [sg.Text('Tipo del registro: ')],
        [sg.Input(key='tipo_registro')],
        [sg.Button('Generar')],
        [sg.Listbox(opciones, size=(20,5), key='opciones', enable_events=True, select_mode='LISTBOX_SELECT_MODE_SINGLE')],
        [sg.Output(size=(100,3),key='descripciones')],
        [sg.Output(size=(100,20), key='output',font=('Monaco',16))],
        [sg.Exit('Salir')]]

window = sg.Window('Generador de módulos de Pascal',layout)

'''funciones = [leer_datos_de_registro(nombre_registro,tipo_registro,'codigo',0,['nombre','apellido']),
            registro_a_texto_multiline(nombre_registro,tipo_registro,'archivoTxt',['nombre','apellido','dni','edad'])]'''

while True:
    event, values = window.read()
    window['descripciones'].update(descripciones[window['opciones'].get_indexes()[0]])
    if event == 'Generar':
        nombre_registro = values['nombre_registro']
        tipo_registro = values['tipo_registro']
        if window['opciones'].get_indexes()[0] == 0:
            window['output'].update(leer_datos_de_registro(nombre_registro,tipo_registro,'codigo',0,['nombre','apellido']))
        elif window['opciones'].get_indexes()[0] == 1:
            window['output'].update(registro_a_texto_multiline(nombre_registro,tipo_registro,'archivoTxt',['nombre','apellido','dni','edad']))
        #window['output'].update(funciones[window['opciones'].get_indexes()[0]])    
    if event == sg.WIN_CLOSED or event == 'Salir':
        break

window.close()
