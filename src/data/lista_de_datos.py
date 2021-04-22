from src.data.funciones_de_procedimientos import *

lista_de_procedimientos = [
    {
        'nombre':'LeerRegistro', 
        'funcion':leer_datos_de_registro, 
        'descripcion':'Solicita el ingreso por teclado de los campos del registro.',
        'encabezado':'procedure leerRegistro (var nombreRegistro:tipoRegistro);',
        'campos_requeridos':'Nombre del registro, Tipo del registro, Campos del registro'
    },

    {
        'nombre':'LeerFinDeArchivo', 
        'funcion':leer_fin_de_archivo, 
        'descripcion':'Verifica si es el final del archivo.',
        'encabezado':'procedure leer (var archivo:tipoArchivo; var nombreRegistro:tipoRegistro);',
        'campos_requeridos':'Nombre del registro, Tipo del registro, Tipo del archivo'
    },

    {
        'nombre':'Minimo', 
        'funcion':minimo, 
        'descripcion':'Calcula el registro minimo entre los registros de un vector de archivos detalle.',
        'encabezado':'procedure minimo (var V:vectorDeDetalles; var min:tipoRegistro);',
        'campos_requeridos':'Cantidad de archivos detalle, Tipo del registro, Tipo del vector de archivos detalle, Tipo del vector de registros'
    },

    {
        'nombre':'EliminarConListaInvertida', 
        'funcion':baja_logica_lista_invertida, 
        'descripcion':'Elimina un registro solicitando el codigo del registro a eliminar, y reasigna el espacio mediante una lista invertida.',
        'encabezado':'procedure eliminar (var archivo:bin);',
        'campos_requeridos':'Nombre del registro, Tipo del registro, Tipo del archivo'
    },

    {
        'nombre':'AgregarConListaInvertida', 
        'funcion':agregar_en_archivo_lista_invertida, 
        'descripcion':'Agrega un registro en un archivo que trabaja con una lista invertida para controlar las bajas.',
        'encabezado':'procedure agregar (var archivo:bin);',
        'campos_requeridos':'Nombre del registro, Tipo del registro, Tipo del archivo'
    },

    {
        'nombre':'CompactarArchivoDesordenado', 
        'funcion':compactar_archivo_desordenado, 
        'descripcion':'Ocupa las posiciones previamente eliminadas con los registros del final del archivo, y lo trunca.',
        'encabezado':'procedure compactar (var archivo:bin);',
        'campos_requeridos':'Nombre del registro, Tipo del registro, Tipo del archivo'
    },

    {
        'nombre':'DesplegarMenu', 
        'funcion':desplegar_menu, 
        'descripcion':'Muestra en pantalla un menu con opciones. Las opciones en este caso son ejemplos.',
        'encabezado':'procedure desplegarMenu (var archivo:bin; var txt:text);',
        'campos_requeridos':'Tipo del archivo'
    },
    
    {
        'nombre':'RegATexto', 
        'funcion':registro_a_texto_multilinea, 
        'descripcion':'Escribe todos los campos de un registro en un archivo de texto, cada campo en una nueva linea.',
        'encabezado':'procedure regATexto (var nombreRegistro:tipoRegistro; var nombreArchivoTexto:text);',
        'campos_requeridos':'Nombre del registro, Tipo del registro, Nombre del archivo de texto, Campos del registro'
    },
    
    {
        'nombre':'ValorEntero', 
        'funcion':valor_entero, 
        'descripcion':'Función que recibe un string y, en caso de ser un número, retorna su valor en integer. De no ser un número entero, retorna -1.',
        'encabezado':'function valorEntero (texto:string):integer;',
        'campos_requeridos':'Ninguno'
    }
]
