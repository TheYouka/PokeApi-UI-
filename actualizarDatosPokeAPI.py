import requests as req
import os
import re

#path=os.getcwd()
#registroPath=os.path.join(path,"registros")
Pokemones = {}

#Carga la lista con los nombres de los pokemones y su respectivo color a la vez de inicializar el registro de colores
def saveThisTo(saving,file):
    with open(file,'w') as guardando:
        json.dump(saving,guardando)


def init_poke_info():
	print("Cargando información de colores...")

	colorDiccionario={}
	

	for i in range(1,11):
		pokeList=list()

		colorDex=req.get('https://pokeapi.co/api/v2/pokemon-color/'+str(i)+'/').json()
		color_name = colorDex['names'][5]['name'].lower()
		
		for i in range(len(colorDex['pokemon_species'])):
			pokemon_name = colorDex['pokemon_species'][i]['name'] 

			pokemon = {"name":pokemon_name,"color":color_name,"tipo":[],"grupo":[]}
			
			Pokemones[pokemon_name] = pokemon

			pokeList.append(pokemon_name)

		else:
			colorDiccionario[color_name] = pokeList	

	#saveThisTo(colorDiccionario,os.path.join(registroPath,'Color.txt'))

	

def load_types():
	print("Cargando información de tipos...")
	tipoDiccionario={}
	for i in range(1,30):
	    try:
	        tipoDex=req.get('https://pokeapi.co/api/v2/type/'+str(i)+'/').json()
	        
	    except:
	        break

	    name=tipoDex['names'][5]['name'].lower()
	    pokeList=list()

	    #Cuidado con los elementos que no son pokemones como tal
	    for i in range(len(tipoDex['pokemon'])):
	    	pokemon_name = tipoDex['pokemon'][i]['pokemon']['name']



	    	pokeList.append(pokemon_name)
	    	
	    	#Comprobar que este en el diccionario
	    	if pokemon_name in Pokemones:
	    		Pokemones[pokemon_name]["tipo"].append(name) 
	    	
	    		#Extraer el id global del pokemon
	    		pokemon_id = re.search(r"pokemon\/(\d+)",tipoDex['pokemon'][i]['pokemon']['url']).group(1)
	    		Pokemones[pokemon_name]["id"] = pokemon_id 


	    tipoDiccionario[name]=pokeList

	#saveThisTo(tipoDiccionario,os.path.join(registroPath,'Tipos.txt'))


def load_habitats():
	print("Cargando información de hábitats...")
	habitatDiccionario={}
	for i in range(1,70):
	    try:
	        habitatDex=req.get('https://pokeapi.co/api/v2/pokemon-habitat/'+str(i)+'/').json()
	    except:
	        break
	    
	    name=habitatDex['names'][1]['name'].lower()
	    pokeList=list()
	    for i in range(len(habitatDex['pokemon_species'])):
	        pokemon_name = habitatDex["pokemon_species"][i]["name"]

	        pokeList.append(pokemon_name)

	        Pokemones[pokemon_name]["habitat"] = name
	        #print(Pokemones[pokemon_name])

	    habitatDiccionario[name]=pokeList
	#saveThisTo(habitatDiccionario,os.path.join(registroPath,'Habitat.txt'))


def load_eggs():
	print("Cargando información de grupos de huevo...")
	huevoDiccionario={}
	for i in range(1,70):
	    try:      
	        huevoDex=req.get('https://pokeapi.co/api/v2/egg-group/'+str(i)+'/').json()
	    except:
	        break
	    
	    name=huevoDex['names'][5]['name'].lower()
	    pokeList=list()
	    for i in range(len(huevoDex['pokemon_species'])):
	    	pokemon_name = huevoDex["pokemon_species"][i]["name"]
	    	
	    	pokeList.append(pokemon_name)
	    	
	    	Pokemones[pokemon_name]["grupo"].append(name)
	    
	    huevoDiccionario[name]=pokeList
	#saveThisTo(huevoDiccionario,os.path.join(registroPath+'GrupoDeHuevo.txt'))


init_poke_info()
load_types()
load_habitats()
load_eggs()
print(Pokemones["pikachu"])
