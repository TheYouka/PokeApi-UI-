import json
import os
from Modulos import Utils
path=os.getcwd()
pathRegistro=os.path.join(path,'registros')

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
  pathRegistro=os.path.join(path,'registros')
  try:
    with open(os.path.join(pathRegistro,fileName),'r') as datos:
      datoInfo=json.load(datos)
    return datoInfo
  except:
    #no se encontró el archivo
    return False


def numToName(pokemonID,pokemones=abrirJson(os.path.join(pathRegistro,'GlobalData.txt'))):
  #DANIEL CÁRDENAS ADAME
  #Esta función te regresa el NOMBRE del pokemon con dado numero de pokedex
  for name in list(pokemones.keys()):
    if pokemones[name]['id']==pokemonID:
      return name
      break
    else:
      return 0
      break

def nameToNum(name,pokemones=abrirJson(os.path.join(pathRegistro,'GlobalData.txt'))):
  #DANIEL CÁRDENAS ADAME
  #Función inversa de numToName
  try:
    num=pokemones['name']['id']
    return num
  except:
    return 0


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





