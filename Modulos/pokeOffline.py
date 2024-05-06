import json

#esta función carga un archivo tipo json o txt a una variable
#lo convierte a una lista, diccionario, etc. que se puede manipular por Python
def loadFile(fileName):
  with open(fileName,'r') as file:
    info=json.load(file)
  #se cierra el archivo
  return info
