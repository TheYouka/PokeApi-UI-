import json
import os
from Modulos import Utils


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





