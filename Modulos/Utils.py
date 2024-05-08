import subprocess


def check_connection_internet():
  process = subprocess.run(["ping","-w","1","pokeapi.co"],capture_output=True)
  if process.returncode == 0:
    #Tienes internet
    return True
  else:
    #No tienes internet
    return False


def load_json(file):
  contenido = ""

  with open(file,"r") as f:
    contenido = f.read()

  return contenido

