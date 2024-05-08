import json
import os
from Modulos import Utils

def abrirJson(fileName):
  #DANIEL CÁRDENAS ADAME
  #Esta función te guarda un archivo a formato diccionario en una variable
  #Lo retorna a una variable
  with open(fileName,'r') as datos:
    datoInfo=json.load(datos)
  return datoInfo

def abrirRegistro(fileName):
  #DANIEL CÁRDENAS ADAME
  #Esta función te guarda un archivo a formato diccionario en una variable
  #Te deja saltar el paso de incluir el directorio hacia el registro
  #Lo retorna a una variable
  path=os.getcwd()
  try:
    with open(path+'\\registros\\'+str(fileName),'r') as datos:
      datoInfo=json.load(datos)
    return datoInfo
  except:
    #no se encontró el archivo
    return False


def findNum(pokemon,lista):
  #DANIEL CÁRDENAS ADAME
  #Esta función te regresa el ÍNDICE en el que se tiene el Pokémon.
  #No te regresa su ID, solo índice. Va a depender de la lista que uses.
  for i in range(len(lista)):
    if lista[i]['nombre']==pokemon:
      return i
      break



def rewrite_data():

  print("¡Bienvenido al modificador de información\n")

  print("¿Qué sección desea modificar?\n")

  print("1- Pokemones por Color\n\n2-Pokemones por Generación\n\n3-Habitat\n\n4-Grupos de huevos\n\n5-Tipos de pokemones\n")

  opcion = input(">>")



def By_color():
  #Convertir Archivo a Diccionario
  color_path = os.path.join(os.getcwd(),"registros","Color.txt")
  archivo = json.loads(Utils.load_json(color_path))

  #Secciones posibles a modificar
  opciones = ['negro', 'azul', 'marrón', 'gris', 'verde', 'rosa', 'morado', 'rojo', 'blanco', 'amarillo']

  print( """
Seleccione el color que desea modificar:
1. negro
2. azul
3. marrón
4. gris
5. verde
6. rosa
7. morado
8. rojo
9. blanco
10. amarillo

Ingrese el número correspondiente al color que desea modificar: 
"""
)

  opcion = input(">> ")

  #Validad datos 
  pass





