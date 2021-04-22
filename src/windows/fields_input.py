import PySimpleGUI as sg

def build(campos_requeridos):
    layout = [
            [sg.Text('Campos requeridos:')], 
            [sg.Text(campos_requeridos,size=(60,2),key='-CAMPOS_REQUERIDOS-', background_color='#324F7B',justification='center')],
            [sg.Text('\nIngrese los campos en el mismo orden en que se muestran arriba\n(Valores separados por coma. Por ejemplo, "empleado,regEmpleado,Archivo Maestro,..."):',size=(70,4),justification='center')], 
            [sg.Input(size=(60,3),key='-CAMPOS_INGRESADOS-',justification='center')],            
        ]
    
    if 'Campos del registro' in campos_requeridos:
        layout.insert(2, [sg.Text('Los campos del registro deben ingresarse por separado, en el cuadro de más abajo.',size=(60,2),text_color='yellow',justification='center')])
        layout.append([sg.Text('\nCampos del registro (Valores separados por coma. Por ejemplo, "apellido,nombre,pais de origen,..."): ',size=(70,3),justification='center')])
        layout.append([sg.Input(size=(60,3),key='-CAMPOS_REGISTRO-',justification='center')])
    
    layout.append([sg.Button('Generar',key='-CREATE-'), sg.Exit('Salir',key='-EXIT-')])

    window = sg.Window('Ingreso de datos',layout,resizable=True,element_justification='center',font=('Bahnschrift SemiLight',15))

    return window
