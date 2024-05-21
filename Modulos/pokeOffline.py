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
  #agarra un id y te va a regresar el nombre del pokemon
  #sirve para organizar en base a generación con la función genPrevTot()
  for name in list(pokemones.keys()):
    if pokemones[name]['id']==str(pokemonID):
      return name
      break
    else:
      name=0
  return name

def nameToNum(name,pokemones=abrirJson(os.path.join(pathRegistro,'GlobalData.txt'))):
  #DANIEL CÁRDENAS ADAME
  #Función inversa de numToName
  num=pokemones[name]['id']
  try:
    return num
  except:
    return 0

def printInfo(nombrePoke,pokeInfo):
  nombreMayus=nombrePoke.capitalize()
  nombre=nombrePoke
  print('-----'+nombreMayus+'-----')
  print('Color: '+pokeInfo[nombre]['color'].capitalize())
  if len(pokeInfo[nombre]['tipo'])==1:
    print('Tipo: '+pokeInfo[nombre]['tipo'][0].capitalize())
  elif len(pokeInfo[nombre]['tipo'])==2:
    print('Tipos: '+pokeInfo[nombre]['tipo'][0].capitalize()+'-'+pokeInfo[nombre]['tipo'][1].capitalize())
  if len(pokeInfo[nombre]['grupo'])==1:
    print('Grupo de huevo: '+pokeInfo[nombre]['grupo'][0].capitalize())
  elif len(pokeInfo[nombre]['grupo'])==2:
    print('Grupos de huevo: '+pokeInfo[nombre]['grupo'][0].capitalize()+'-'+pokeInfo[nombre]['grupo'][1].capitalize())
  print('Número Nacional: '+ str(pokeInfo[nombre]['id']))
  print('Hábitat: '+pokeInfo[nombre]['habitat'].capitalize())
  print('-------------------------------')

#Te dice el total de Pokémon antes de cierta generación.
def genPrevTot(genNum):
  if genNum==1:
    prevTot=0
  elif genNum==2:
    prevTot=151
  elif genNum==3:
    prevTot=251
  elif genNum==4:
    prevTot=386
  elif genNum==5:
    prevTot=493
  elif genNum==6:
    prevTot=649
  elif genNum==7:
    prevTot=721
  elif genNum==8:
    prevTot=809
  elif genNum==9:
    prevTot=905
  else:
    prevTot=1025
  return prevTot

#Te dice la ID mínima de una generación
def genMin(genNum):
  if genNum==1:
    prevTot=1
  elif genNum==2:
    prevTot=152
  elif genNum==3:
    prevTot=252
  elif genNum==4:
    prevTot=387
  elif genNum==5:
    prevTot=494
  elif genNum==6:
    prevTot=650
  elif genNum==7:
    prevTot=722
  elif genNum==8:
    prevTot=810
  elif genNum==9:
    prevTot=906
  else:
    prevTot=1026
  return prevTot

#Te dice la ID máxima de una generación
def genMax(genNum):
  if genNum==1:
    prevTot=151
  elif genNum==2:
    prevTot=251
  elif genNum==3:
    prevTot=386
  elif genNum==4:
    prevTot=493
  elif genNum==5:
    prevTot=649
  elif genNum==6:
    prevTot=721
  elif genNum==7:
    prevTot=810
  elif genNum==8:
    prevTot=905
  elif genNum==9:
    prevTot=1025
  else:
    prevTot=9999
  return prevTot

def isInGen(idNum,gen):
  if idNum<=genMax(gen) and idNum>=genMin(gen):
    return True
  else:
    return False
    #fin



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




