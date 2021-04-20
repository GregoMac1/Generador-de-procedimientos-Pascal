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

def minimo(tipo_vector_detalles,tipo_vector_registros,tipo_registro,cant_detalles):
    modulo = f'''procedure minimo (var V:{tipo_vector_detalles}; var min:{tipo_registro});
  var
    i,iMin,valorMin:integer; Vreg:{tipo_vector_registros};
  begin
    valorMin:=9999;
    for i:= 1 to {cant_detalles} do begin
      leer(V[i],Vreg[i]);
      if (Vreg[i].codigo <> valoralto) & (Vreg[i].codigo < valorMin) then begin
        valorMin:=Vreg[i].codigo;
        iMin:=i;
      end;
    end;
    min:=V[iMin];
    leer(V[iMin],Vreg[iMin]);
  end;'''
    return modulo

def desplegar_menu(tipo_archivo):
    modulo = f'''procedure desplegarMenu (var archivo:{tipo_archivo}; var txt:text);
  var
    opcion:integer;
  begin
    writeln('1. Crear un archivo de registros.');
    writeln('2. Listar los celulares con stock menor al minimo.');
    writeln('3. Listar los celulares que tengan descripcion.');
    writeln('4. Exportar el archivo de registros a un txt.');
    writeln('5. Anadir uno o mas celulares.');
    writeln('6. Modificar el stock disponible de un celular.');
    writeln('7. Exportar los celulares sin stock a txt.');
    writeln('0. Salir.');writeln();
    write('Opcion: ');readln(opcion);writeln();
    if (opcion<>0) then begin
      case opcion of
        1: crearBinario(archivo,txt);
        2: listarCelularesStock(archivo);
        3: listarCelularesDescrip(archivo);
        4: exportarTodos(archivo);
        5: anadirCelulares(archivo);
        6: modificarStock(archivo);
        7: exportarSinStock(archivo);
        else
          writeln('Opcion incorrecta.');writeln();
      end;
      desplegarMenu(archivo,txt);
    end;  
  end;'''
    return modulo

def agregar_en_archivo_lista_invertida(nombre_registro,tipo_registro,tipo_archivo):
    modulo = f'''procedure agregar{nombre_registro.capitalize()} (var archivo:{tipo_archivo});
  var
    {nombre_registro}:{tipo_registro}; pos,posInicio:integer;
  begin    
    reset(archivo);
    read(archivo,{nombre_registro});
    if ({nombre_registro}.codigo<=0) then begin
      pos:={nombre_registro}.codigo*(-1);
      seek(archivo,pos);
      read(archivo,{nombre_registro});
      posInicio:={nombre_registro}.codigo;
      leer{nombre_registro}({nombre_registro});
      seek(archivo,filepos(archivo)-1);
      write(archivo,{nombre_registro});
      seek(archivo,0);
      {nombre_registro}.codigo:=posInicio;
      write(archivo,{nombre_registro});
    end
    else begin
      seek(archivo,filesize(archivo));
      leer{nombre_registro.capitalize()}({nombre_registro});
      write(archivo,{nombre_registro});
    end;    
    close(archivo);
  end;'''
    return modulo

def baja_fisica_lista_invertida(nombre_registro,tipo_registro,tipo_archivo):
    modulo = f'''procedure eliminar{nombre_registro.capitalize()} (var archivo:{tipo_archivo});
  var
    {nombre_registro}:{tipo_registro}; codigo,pos,posInicio:integer;
  begin
    reset(archivo);
    write('Ingrese el codigo de la novela a eliminar: ');readln(codigo);
    read(archivo,{nombre_registro});
    posInicio:={nombre_registro}.codigo;
    while ({nombre_registro}.codigo<>codigo) do
      read(archivo,{nombre_registro});
    pos:=(filepos(archivo)-1)*(-1);
    {nombre_registro}.codigo:=posInicio;
    seek(archivo,filepos(archivo)-1);
    write(archivo,{nombre_registro});
    seek(archivo,0);
    {nombre_registro}.codigo:=pos;
    write(archivo,{nombre_registro});
    close(archivo);
  end;'''
    return modulo

def valor_entero():
    modulo = '''function valorEntero (texto:string):integer;
  var
    valor,codigoError:integer;
  begin
    valor:=-1;
    val(texto,valor,codigoError);
    valorEntero:=valor;
  end;'''
    return modulo