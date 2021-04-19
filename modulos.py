def leer_datos_de_registro(nombre_registro,tipo_registro,campo_de_corte,valor_de_corte,campos):
    modulo = f'''procedure leer{nombre_registro.capitalize()} (var {nombre_registro}:{tipo_registro});
  begin
    with {nombre_registro} do begin
      writeln('Ingrese:');
      write('{campo_de_corte.capitalize()}: ');readln();
      if ({campo_de_corte}<>{valor_de_corte}) then begin'''
    for i in range(len(campos)):
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
