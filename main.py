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

window = sg.Window('Generador de procedimientos de Pascal',layout,resizable=True,element_justification='center',font=('Arial',11),return_keyboard_events=True)

while True:
    event, values = window.read()
    try:
        window['descripciones'].update(descripciones[window['opciones'].get_indexes()[0]])        
    except IndexError:
        pass
    try:
        window['encabezados'].update(encabezados[window['opciones'].get_indexes()[0]])
    except IndexError:
        pass
    try:
        window['campos_requeridos'].update(campos_requeridos[window['opciones'].get_indexes()[0]])
    except IndexError:
        pass
    if event == 'Generar' or event == 'Enter':        
        campos_ingresados = values['campos_ingresados'].split(',')
        for i in range(len(campos_ingresados)):
            campos_ingresados[i] = campos_ingresados[i].strip(' ')
        campos_registro = values['campos_registro'].split(',')
        for i in range(len(campos_registro)):
            campos_registro[i] = campos_registro[i].strip(' ')
        try:                 
            if window['opciones'].get_indexes()[0] == 0:
                try:
                    sg.popup_scrolled(leer_datos_de_registro(campos_ingresados[0],campos_ingresados[1],campos_registro),title='Resultado',font=('Monaco',12))
                except IndexError:
                    sg.popup('Error en el ingreso de los campos.',title='Error')
            elif window['opciones'].get_indexes()[0] == 1:
                try:
                    sg.popup_scrolled(registro_a_texto_multiline(campos_ingresados[0],campos_ingresados[1],campos_ingresados[2],campos_registro),title='Resultado',font=('Monaco',12))
                except IndexError:
                    sg.popup('Error en el ingreso de los campos.',title='Error')
            elif window['opciones'].get_indexes()[0] == 2:
                try:
                    sg.popup_scrolled(leer_fin_de_archivo(campos_ingresados[0],campos_ingresados[1],campos_ingresados[2],campos_ingresados[3]),title='Resultado',font=('Monaco',12))
                except IndexError:
                    sg.popup('Error en el ingreso de los campos.',title='Error')
            elif window['opciones'].get_indexes()[0] == 3:
                try:
                    sg.popup_scrolled(minimo(campos_ingresados[0],campos_ingresados[1],campos_ingresados[2],campos_ingresados[3]),title='Resultado',font=('Monaco',12))
                except IndexError:
                    sg.popup('Error en el ingreso de los campos.',title='Error')
            elif window['opciones'].get_indexes()[0] == 4:
                try:
                    sg.popup_scrolled(desplegar_menu(campos_ingresados[0]),title='Resultado',font=('Monaco',12))
                except IndexError:
                    sg.popup('Error en el ingreso de los campos.',title='Error')
            elif window['opciones'].get_indexes()[0] == 5:
                try:
                    sg.popup_scrolled(agregar_en_archivo_lista_invertida(campos_ingresados[0],campos_ingresados[1],campos_ingresados[2]),title='Resultado',font=('Monaco',12))
                except IndexError:
                    sg.popup('Error en el ingreso de los campos.',title='Error')
            elif window['opciones'].get_indexes()[0] == 6:
                try:
                    sg.popup_scrolled(baja_fisica_lista_invertida(campos_ingresados[0],campos_ingresados[1],campos_ingresados[2]),title='Resultado',font=('Monaco',12))
                except IndexError:
                    sg.popup('Error en el ingreso de los campos.',title='Error')
            elif window['opciones'].get_indexes()[0] == 7:
                try:
                    sg.popup_scrolled(valor_entero(),title='Resultado',font=('Monaco',12))
                except IndexError:
                    sg.popup('Error en el ingreso de los campos.',title='Error')
        except IndexError:
            sg.popup('Error. No hay ningún procedimiento seleccionado.',title='Error')
    if event == sg.WIN_CLOSED or event == 'Salir':
        break

window.close()
