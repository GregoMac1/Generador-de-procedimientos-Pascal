def leer_datos_de_registro(nombre_registro,tipo_registro,campos):
    modulo = f'''procedure leer{nombre_registro.capitalize()} (var {nombre_registro}:{tipo_registro});
  begin
    with {nombre_registro} do begin
      writeln('Ingrese:');
      write('{campos[0].capitalize()}: ');readln();
      if ({campos[0]}<>0) then begin'''
    for i in range(1,len(campos)):
        modulo += f'\n        write(\'{campos[i].capitalize()}: \');readln();'
    modulo += '''
      end;
    end;writeln();
  end;
'''
    return modulo

def registro_a_texto_multiline(nombre_registro,tipo_registro,nombre_archivo_texto,campos):
    modulo = f'''procedure regATexto (var {nombre_registro}:{tipo_registro}; var {nombre_archivo_texto}:text);
  begin'''
    for i in range(len(campos)):
        modulo += f"\n    write({nombre_archivo_texto},\'{campos[i].capitalize()}: \');write({nombre_archivo_texto},{nombre_registro}.{campos[i]});write({nombre_archivo_texto},'\\n');"
    modulo += f'''
    write({nombre_archivo_texto},'\\n');   
  end;'''
    return modulo

def leer_fin_de_archivo(nombre_registro,tipo_registro,nombre_archivo,tipo_archivo):
    modulo = f'''procedure leer (var {nombre_archivo}:{tipo_archivo}; var {nombre_registro}:{tipo_registro});
  begin
    if (not eof({nombre_archivo})) then
      read({nombre_archivo},{nombre_registro})
    else
      {nombre_registro}.codigo:=valoralto; //'codigo' por defecto.
  end;'''
    return modulo