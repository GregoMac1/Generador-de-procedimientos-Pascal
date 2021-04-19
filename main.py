import PySimpleGUI as sg
from modulos import *
from listas_de_datos import *

sg.theme('DefaultNoMoreNagging')

layout = [[sg.Text(texto_bienvenida,size=(60,3),justification='center',font=('Arial',18))],        
        [sg.Listbox(lista_de_opciones, size=(20,10), key='opciones', enable_events=True, select_mode='LISTBOX_SELECT_MODE_SINGLE',font=('Arial',11)), 
        sg.Text(size=(25,5),key='descripciones', background_color='#FFFFFF',font=('Arial',11)), 
        sg.Text(size=(60,5),key='encabezados', background_color='#FFFFFF',font=('Monaco',11))],        
        [sg.Text('Campos requeridos: ',size=(15,1)), sg.Text(size=(50,3),key='campos_requeridos', background_color='#FFFFFF',font=('Arial',11))],        
        [sg.Text('Ingrese los campos en el mismo orden en que se muestran arriba. Si es necesario ingresar los campos del registro, no lo haga en este cuadro, sino en el de abajo (Valores separados por coma. Por ejemplo, "empleado,regEmpleado,Archivo Maestro,..."):',size=(70,3),justification='center'), sg.Input(size=(50,3),key='campos_ingresados')],
        [sg.Text('Campos del registro (Sólo llenar si el procedimiento lo solicita. Valores separados por coma. Por ejemplo, "apellido,nombre,pais de origen,..."): ',font=('Arial',11),size=(70,2),justification='center'), sg.Input(key='campos_registro',font=('Arial',11))],
        [sg.Button('Generar',font=('Arial',11)), sg.Exit('Salir',font=('Arial',11))]]

window = sg.Window('Generador de procedimientos de Pascal',layout,resizable=True,grab_anywhere=True,element_justification='center',font=('Arial',11))

while True:
    event, values = window.read()
    window['descripciones'].update(descripciones[window['opciones'].get_indexes()[0]])
    window['encabezados'].update(encabezados[window['opciones'].get_indexes()[0]])
    window['campos_requeridos'].update(campos_requeridos[window['opciones'].get_indexes()[0]])
    if event == 'Generar':        
        campos_ingresados = values['campos_ingresados'].split(',')
        for i in range(len(campos_ingresados)):
            campos_ingresados[i] = campos_ingresados[i].strip(' ')
        campos_registro = values['campos_registro'].split(',')
        for i in range(len(campos_registro)):
            campos_registro[i] = campos_registro[i].strip(' ')
        if window['opciones'].get_indexes()[0] == 0:
            sg.popup_scrolled(leer_datos_de_registro(campos_ingresados[0],campos_ingresados[1],campos_registro),title='Resultado',font=('Monaco',12))
        elif window['opciones'].get_indexes()[0] == 1:
            sg.popup_scrolled(registro_a_texto_multiline(campos_ingresados[0],campos_ingresados[1],campos_ingresados[2],campos_registro),title='Resultado',font=('Monaco',12))
        elif window['opciones'].get_indexes()[0] == 2:
            sg.popup_scrolled(leer_fin_de_archivo(campos_ingresados[0],campos_ingresados[1],campos_ingresados[2],campos_ingresados[3]),title='Resultado',font=('Monaco',12))
    if event == sg.WIN_CLOSED or event == 'Salir':
        break

window.close()
