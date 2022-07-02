
def cargar_diccionario_ingredientes(ruta_in):
     """
     Lee el archivo ingredientes.txt y con esa información
     carga el diccionario de ingredientes a ser usado mas adelante
     """
     text_file = open(ruta_in, 'r')
     diccionario_ingredientes = {}
     for row in text_file.readlines():
          new_row = [element.rstrip('\n').strip() for element in row.split(" ")]
          diccionario_ingredientes[new_row[0].title()] = int(new_row[1])
     return diccionario_ingredientes

def cargar_diccionario_recetas(ruta_re):
     """
     lee el archivo recetas.csv y con esa información carga el
     diccionario de recetas a ser usado mas adelante
     """
     csv_file = open(ruta_re, 'r')
     diccionario_recetas = {}
     for row in csv_file.readlines():
          new_row = [element.rstrip('\n').strip() for element in row.split(",")]
          first,  *others = new_row
          diccionario_recetas[first] = others
     return diccionario_recetas
    
def printStocks(dic_ingredientes):
     """
     A partir del diccionario de ingredientes genera el listado que debe imprimirse después de cada operación de preparación o reposición
     """
     print('Stock actual de ingredientes disponibles')
     for k,v in dic_ingredientes.items():
             print  (k, v)
    

def reponerIngredientes(lista_ingredientes, dic_ingredientes):
     for ingrediente in lista_ingredientes:
          if ingrediente in dic_ingredientes.keys():
               dic_ingredientes[ingrediente] += 1

     return  printStocks(dic_ingredientes)

def prepararReceta(receta,dic_recetas, dic_ingredientes):
     if receta in dic_recetas.keys():
          sin_stock = {}
          for ingrediente in dic_recetas[receta]:
               if dic_ingredientes[ingrediente] == 0:
                    sin_stock[ingrediente] = 0

          if len(sin_stock) > 0:
               ingredientes_faltantes = ''
               for k,v in sin_stock.items():
                    ingredientes_faltantes = ingredientes_faltantes + k + ', '
               
               print(f'*** No se puede hacer {receta} porque falta {ingredientes_faltantes[0:len(ingredientes_faltantes)-2]} ***')
               return printStocks(dic_ingredientes)
          else:
               for ingrediente in dic_recetas[receta]:
                    dic_ingredientes[ingrediente] -= 1
               return printStocks(dic_ingredientes)

     else:
          print (f'*** Lo sentimos pero no preparamos {receta} ***')
          return printStocks(dic_ingredientes)


ruta_in = '/Users/dvilches/Desktop/Diplomado/Parte A/Mod 6/miniproyecto3/ingredientes.txt'
ruta_re = '/Users/dvilches/Desktop/Diplomado/Parte A/Mod 6/miniproyecto3/recetas.csv'

recetas =  cargar_diccionario_recetas(ruta_re)
ingredientes = cargar_diccionario_ingredientes(ruta_in)


Seguir = True

while Seguir:
     #Ingreso de respuesta del usuario. Esta respuesta se convierte en lista y cada elemento queda en mayúscula.
     respuesta = input('Ingresa la receta que quieres o REPONER: ').split(' ')

     #Comprobamos si la palabra STOP en mayúscula se encuentra ubicado en la primera posición de la lista, si es así el programa termina.
     if 'STOP' in respuesta[0].upper():
          Seguir =  False

     elif 'REPONER' in respuesta[0].upper():
          x, *y = respuesta
          reponerIngredientes((element.title() for element in y), ingredientes)

     elif 'PREPARAR' in respuesta[0].upper():
          prepararReceta(respuesta[1],recetas, ingredientes)
     

     







