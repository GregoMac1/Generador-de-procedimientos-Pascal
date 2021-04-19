texto_bienvenida = '''Generador de procedimientos de Pascal (por ahora sólo para la materia FOD).
Al seleccionar una opción de la lista de procedimientos, verá una lista de los campos que necesita llenar para obtener el procedimiento seleccionado.'''

lista_de_opciones = ['LeerRegistro',
            'RegATexto',
            'LeerFinDeArchivo',
            'Minimo',
            'AgregarListaAlFinal',
            'AgregarListaAdelante',
            'InsertarOrdenadoLista',
            'MergeAcumulador']

descripciones = [
'Solicita el ingreso por teclado de los campos del registro.',
'Escribe todos los campos de un registro en un archivo de texto, cada campo en una nueva linea.',
'Verifica si es el final del archivo.',
'Calcula el minimo.',
'h','o','l','a'
]

encabezados = [
'procedure leerRegistro (var nombreRegistro:tipoRegistro);',
'procedure regATexto (var nombreRegistro:tipoRegistro; var nombreArchivoTexto:text);',
'procedure leer (var nombreArchivo:tipoArchivo; var nombreRegistro:tipoRegistro);',
'h','o','l','a','!'
]

campos_requeridos = [
'Nombre del registro, Tipo del registro, Campos del registro',
'Nombre del registro, Tipo del registro, Nombre del archivo de texto, Campos del registro',
'Nombre del registro, Tipo del registro, Nombre del archivo, Tipo del archivo',
'h','o','l','a','!'
]
