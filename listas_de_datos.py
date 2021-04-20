texto_bienvenida = '''Generador de procedimientos de Pascal (por ahora sólo para la materia FOD).
Al seleccionar una opción de la lista de procedimientos, verá una lista de los campos que necesita ingresar para obtener el procedimiento seleccionado.'''

lista_de_opciones = [
'LeerRegistro',
'RegATexto',
'LeerFinDeArchivo',
'Minimo',
'DesplegarMenu',
'AgregarRegistroBajas',
'BajaLogicaListaInvertida',
'ValorEntero',
]

descripciones = [
'Solicita el ingreso por teclado de los campos del registro.',
'Escribe todos los campos de un registro en un archivo de texto, cada campo en una nueva linea.',
'Verifica si es el final del archivo.',
'Calcula el registro minimo entre los registros de un vector de archivos detalle.',
'Muestra en pantalla un menu con opciones. Las opciones en este caso son ejemplos.',
'Agrega un registro en un archivo que trabaja con una lista invertida para controlar las bajas.',
'Elimina un registro solicitando el codigo del registro a eliminar, y reasigna el espacio mediante una lista invertida.',
'Función que recibe un string y, en caso de ser un número, retorna su valor en integer. De no ser un número entero, retorna -1',
]

encabezados = [
'procedure leerRegistro (var nombreRegistro:tipoRegistro);',
'procedure regATexto (var nombreRegistro:tipoRegistro; var nombreArchivoTexto:text);',
'procedure leer (var nombreArchivo:tipoArchivo; var nombreRegistro:tipoRegistro);',
'procedure minimo (var V:vectorDeDetalles; var min:tipoRegistro);',
'procedure desplegarMenu (var archivo:bin; var txt:text);',
'procedure agregar (var archivo:bin);',
'procedure eliminar (var archivo:bin);',
'function valorEntero (texto:string):integer;',
]

campos_requeridos = [
'Nombre del registro, Tipo del registro, Campos del registro',
'Nombre del registro, Tipo del registro, Nombre del archivo de texto, Campos del registro',
'Nombre del registro, Tipo del registro, Nombre del archivo, Tipo del archivo',
'Tipo del vector de archivos detalle, Tipo del vector de registros, Tipo del registro, Cantidad de archivos detalle',
'Tipo del archivo',
'Nombre del registro, Tipo del registro, Tipo del archivo',
'Nombre del registro, Tipo del registro, Tipo del archivo',
'',
]
