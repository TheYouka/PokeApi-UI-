#CREADO POR DANIEL CÁRDENAS ADAME
#Con ayuda de Alberto
#Este programa se corre únicamente importándolo desde main.py

import requests as req
import os
import re
import json

def ACTUALIZAR():
    
    path=os.getcwd()
    registroPath=os.path.join(path,"registros")
    Pokemones = {}
    
    from Modulos import pokeOffline
    
    #Carga la lista con los nombres de los pokemones y su respectivo color a la vez de inicializar el registro de colores
    def saveThisTo(saving,file):
        with open(file,'w') as guardando:
            json.dump(saving,guardando)




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



    saveThisTo(Pokemones, os.path.join(registroPath,'GlobalData.txt'))


    print("Cargando información de generaciones...")

    def genNum(gen):
        if gen==1:
            pokeID=range(0,151)
        elif gen==2:
            pokeID=range(151,251)
        elif gen==3:
            pokeID=range(251,386)
        elif gen==4:
            pokeID=range(386,493)
        elif gen==5:
            pokeID=range(493,649)
        elif gen==6:
            pokeID=range(649,721)
        elif gen==7:
            pokeID=range(721,809)
        elif gen==8:
            pokeID=range(809,905)
        elif gen==9:
            pokeID=range(905,1025)
        else:
            pokeID=range(1025,9999)
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





