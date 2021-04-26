def leer_datos_de_registro(campos,campos_registro):
    modulo = f'''procedure leer{campos[0].capitalize()} (var {campos[0]}:{campos[1]});
  begin
    with {campos[0]} do begin
      writeln('Ingrese:');
      write('{campos[0].capitalize()}: ');readln();
      if ({campos[0]}<>0) then begin'''
    for i in range(1,len(campos_registro)):
        modulo += f'\n        write(\'{campos_registro[i].capitalize()}: \');readln();'
    modulo += '''
      end;
    end;writeln();
  end;
'''
    return modulo

def registro_a_texto_multilinea(campos,campos_registro):
    modulo = f'''procedure regATexto (var {campos[0]}:{campos[1]}; var {campos[2]}:text);
  begin'''
    for i in range(len(campos_registro)):
        modulo += f"\n    write({campos[2]},\'{campos_registro[i].capitalize()}: \');write({campos[2]},{campos[0]}.{campos_registro[i]});write({campos[2]},'\\n');"
    modulo += f'''
    write({campos[2]},'\\n');   
  end;'''
    return modulo

def leer_fin_de_archivo(campos):
    modulo = f'''procedure leer (var archivo:{campos[2]}; var {campos[0]}:{campos[1]});
  begin
    if (not eof(archivo)) then
      read(archivo,{campos[0]})
    else
      {campos[0]}.codigo:=valoralto; //'codigo' por defecto.
  end;'''
    return modulo

def minimo(campos):
    modulo = f'''procedure minimo (var V:{campos[2]}; var min:{campos[1]});
  var
    i,iMin,valorMin:integer; Vreg:{campos[3]};
  begin
    valorMin:=9999;
    for i:= 1 to {campos[0]} do begin
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

def desplegar_menu(campos):
    modulo = f'''procedure desplegarMenu (var archivo:{campos[0]}; var txt:text);
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

def agregar_en_archivo_lista_invertida(campos):
    modulo = f'''procedure agregar{campos[0].capitalize()} (var archivo:{campos[2]});
  var
    {campos[0]}:{campos[1]}; pos,posInicio:integer;
  begin    
    reset(archivo);
    read(archivo,{campos[0]});
    if ({campos[0]}.codigo<0) then begin
      pos:={campos[0]}.codigo*(-1);
      seek(archivo,pos);
      read(archivo,{campos[0]});
      posInicio:={campos[0]}.codigo;
      leer{campos[0].capitalize()}({campos[0]});
      seek(archivo,filepos(archivo)-1);
      write(archivo,{campos[0]});
      seek(archivo,0);
      {campos[0]}.codigo:=posInicio;
      write(archivo,{campos[0]});
    end
    else begin
      seek(archivo,filesize(archivo));
      leer{campos[0].capitalize()}({campos[0]});
      write(archivo,{campos[0]});
    end;    
    close(archivo);
  end;'''
    return modulo

def baja_logica_lista_invertida(campos):
    modulo = f'''procedure eliminar{campos[0].capitalize()} (var archivo:{campos[2]});
  var
    {campos[0]}:{campos[1]}; codigo,pos,posInicio:integer;
  begin
    reset(archivo);
    write('Ingrese el codigo del {campos[0]} a eliminar: ');readln(codigo);
    read(archivo,{campos[0]});
    posInicio:={campos[0]}.codigo;
    while ({campos[0]}.codigo<>codigo) do
      read(archivo,{campos[0]});
    pos:=(filepos(archivo)-1)*(-1);
    {campos[0]}.codigo:=posInicio;
    seek(archivo,filepos(archivo)-1);
    write(archivo,{campos[0]});
    seek(archivo,0);
    {campos[0]}.codigo:=pos;
    write(archivo,{campos[0]});
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
  
def compactar_archivo_desordenado(campos):
    modulo = f'''procedure compactar (var archivo:{campos[2]});
  var
    {campos[0]}:{campos[1]}; cantPosiciones:integer;
  begin
    reset(archivo);
    cantPosiciones:=1;
    leer(archivo,{campos[0]});
    while ({campos[0]}.codigo<>valoralto) do begin
      if ({campos[0]}.codigo<0) then begin
        posActual:=filepos(archivo)-1;
        seek(archivo,filesize(archivo)-cantPosiciones);
        read(archivo,{campos[0]});
        while ({campos[0]}.codigo < 0) do begin
          seek(archivo,filepos(archivo)-2);
          read(archivo,{campos[0]});
        end;
        seek(archivo,posActual);
        write(archivo,{campos[0]});
        cantPosiciones:=cantPosiciones+1;
      end;
      leer(archivo,{campos[0]});
    end;
    seek(archivo,filepos(archivo)-cantPosiciones);
    truncate(archivo);
    close(archivo);
  end;'''
    return modulo
procedure compactar (var archivo:bin);
  var
    especie:reg; cantPosiciones:integer;
  begin
    reset(archivo);
    cantPosiciones:=1;
    leer(archivo,especie);
    while (especie.codigo<>valoralto) do begin
      if (especie.codigo<0) then begin
        posActual:=filepos(archivo)-1;
        seek(archivo,filesize(archivo)-cantPosiciones);
        read(archivo,especie);
        while (especie.codigo < 0) do begin
          seek(archivo,filepos(archivo)-2);
          read(archivo,especie);
        end;
        seek(archivo,posActual);
        write(archivo,especie);
        cantPosiciones:=cantPosiciones+1;
      end;
      leer(archivo,especie);
    end;
    seek(archivo,filepos(archivo)-cantPosiciones);
    truncate(archivo);
    close(archivo);
  end;