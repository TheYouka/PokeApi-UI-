#CREADO POR DANIEL CÁRDENAS ADAME
#Con ayuda de Alberto
#Este programa se corre únicamente importándolo desde main.py

import requests as req
import os
import re
import json



#Carga la lista con los nombres de los pokemones y su respectivo color a la vez de inicializar el registro de colores
def saveThisTo(saving,file):
	with open(file,'w') as guardando:
		json.dump(saving,guardando)

def ACTUALIZAR():
    
    path=os.getcwd()
    registroPath=os.path.join(path,"registros")
    Pokemones = {}
    
    from Modulos import pokeOffline
    
    
    #sección de cargar la info de colores
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

            #para el futuro cuando haya un nuevo juego de Pokémon
                                            

        colorDiccionario[color_name] = pokeList	

        saveThisTo(colorDiccionario,os.path.join(registroPath,'Color.txt'))

	

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

    saveThisTo(tipoDiccionario,os.path.join(registroPath,'Tipos.txt'))


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

    saveThisTo(habitatDiccionario,os.path.join(registroPath,'Habitat.txt'))


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

    saveThisTo(huevoDiccionario,os.path.join(registroPath,'GrupoDeHuevo.txt'))

    #para los pokemon que fallan
    for pokemon in list(Pokemones.keys()):
        try:
            if Pokemones[pokemon]['id']==0:
                print(0)
        except:
            
            num=1
            for color in list(colorDiccionario.keys()):
                
                if pokemon in colorDiccionario[color]:
                    
                    colorInfo=req.get('https://pokeapi.co/api/v2/pokemon-color/'+str(num)+'/').json()
                    for j in range(len(colorInfo['pokemon_species'])):
                        
                        if colorInfo['pokemon_species'][j]['name']==pokemon:
                            pokeSpeciesInfo=req.get(colorInfo['pokemon_species'][j]['url']).json()
                            Pokemones[pokemon]['id']=str(pokeSpeciesInfo['id'])
                            
                            pokeInfo=req.get('https://pokeapi.co/api/v2/pokemon/'+Pokemones[pokemon]['id']+'/').json()
                            Pokemones[pokemon]['tipo']=[]
                            
                            for i in range(len(pokeInfo['types'])):
                                tipoInfo=req.get(pokeInfo['types'][i]['type']['url']).json()
                                Pokemones[pokemon]['tipo'].append(tipoInfo['names'][5]['name'].lower())
                    
                else:
                    num+=1
                    
        try:
            a=Pokemones[pokemon]['habitat']
        except:
            Pokemones[pokemon]['habitat']='ninguno'
            continue

    saveThisTo(Pokemones, os.path.join(registroPath,'GlobalData.txt'))


    print("Cargando información de generaciones...")

    def genNum(gen):
        if gen==1:
            pokeID=range(1,152)
        elif gen==2:
            pokeID=range(152,252)
        elif gen==3:
            pokeID=range(252,387)
        elif gen==4:
            pokeID=range(387,494)
        elif gen==5:
            pokeID=range(494,650)
        elif gen==6:
            pokeID=range(650,722)
        elif gen==7:
            pokeID=range(722,810)
        elif gen==8:
            pokeID=range(810,906)
        elif gen==9:
            pokeID=range(906,1026)
        else:
            pokeID=range(1026,9999)
        return pokeID



    for i in range(1,11):
        genList=[]

        #Pokemones
        for j in genNum(i):
            nombre=pokeOffline.numToName(j,Pokemones)
            
            if str(nombre)=='0':
                break
            genList.append(nombre)
        saveThisTo(genList, os.path.join(registroPath,'Gen'+str(i)+'.txt'))


    print("Se tiene lista la información en base únicamente a la API.")




