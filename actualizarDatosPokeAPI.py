#DANIEL CÁRDENAS ADAME
#obtener la info más reciente de la api y ponerlo en los datos que queremos
import requests as req
import json
import os
path=os.getcwd()
registroPath=path+str('\\registros\\')

def saveThisTo(saving,file):
    with open(file,'w') as guardando:
        json.dump(saving,guardando)


#sección de colores
print("Cargando información de colores...")
colorDiccionario={}
for i in range(1,20):
    try:
        colorDex=req.get('https://pokeapi.co/api/v2/pokemon-color/'+str(i)+'/').json()
        
    except:
        break

    name=colorDex['names'][5]['name'].lower()
    pokeList=list()
    for i in range(len(colorDex['pokemon_species'])):
        pokeList.append(colorDex['pokemon_species'][i]['name'])
    
    colorDiccionario[name]=pokeList
saveThisTo(colorDiccionario,registroPath+'Color.txt')

#sección de tipos
print("Cargando información de tipos...")
tipoDiccionario={}
for i in range(1,30):
    try:
        tipoDex=req.get('https://pokeapi.co/api/v2/type/'+str(i)+'/').json()
        
    except:
        break

    name=tipoDex['names'][5]['name'].lower()
    pokeList=list()
    for i in range(len(tipoDex['pokemon'])):
        pokeList.append(tipoDex['pokemon'][i]['pokemon']['name'])
    
    tipoDiccionario[name]=pokeList
saveThisTo(tipoDiccionario,registroPath+'Tipos.txt')


#sección de habitats
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
        pokeList.append(habitatDex['pokemon_species'][i]['name'])
    
    habitatDiccionario[name]=pokeList
saveThisTo(habitatDiccionario,registroPath+'Habitat.txt')


#sección de huevos
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
        pokeList.append(huevoDex['pokemon_species'][i]['name'])
    
    huevoDiccionario[name]=pokeList
saveThisTo(huevoDiccionario,registroPath+'GrupoDeHuevo.txt')







#basicamente toda la info
print("Compilando la información de cada Pokémon...")
pokemonList=[]
for i in range(1,9999):
    #Imprimiendo información para que quien lo use se sienta cómode.
    if i==152:
        print("Ha terminado la generación 1.")
    elif i==252:
        print("Ha terminado la generación 2.")
    elif i==387:
        print("Ha terminado la generación 3.")
    elif i==494:
        print("Ha terminado la generación 4.")
    elif i==650:
        print("Ha terminado la generación 5.")
    elif i==722:
        print("Ha terminado la generación 6.")
    elif i==810:
        print("Ha terminado la generación 7.")
    elif i==906:
        print("Ha terminado la generación 8.")
    elif i==1025:
        print("Ha terminado la generación 9.")
    #listo
        
    url = f"https://pokeapi.co/api/v2/pokemon/"+str(i)+"/"
    respuesta = req.get(url)
    if respuesta.status_code == 200:
        pokemon = respuesta.json()
        name=pokemon['name']
        globalid=pokemon['id']
        
        tipo1=req.get(pokemon['types'][0]['type']['url']).json()['names'][5]['name'].lower()
        tipos=[]
        tipos.append(tipo1)
        if len(pokemon['types'])==2:
            tipo2=req.get(pokemon['types'][1]['type']['url']).json()['names'][5]['name'].lower()
            tipos.append(tipo2)

        stats=[pokemon['stats'][0]['base_stat']]
        for j in range(1,6):
            stats.append(pokemon['stats'][j]['base_stat'])

        
        #datos guardados en otros archivos
        gruposdehuevo=[]
        with open(registroPath+'GrupoDeHuevo.txt','r') as huevos:
            huevoInfo=json.load(huevos)
            for huevo in list(huevoInfo.keys()):
                if name in huevoInfo[huevo]:
                    gruposdehuevo.append(huevo.lower())

        habitats=0
        with open(registroPath+'Habitat.txt','r') as huevos:
            #aqui estoy reutilizando la misma estructura que antes
            huevoInfo=json.load(huevos)
            for habitat in list(huevoInfo.keys()):
                if name in huevoInfo[habitat]:
                    habitats=habitat.lower()

        colors=0
        with open(registroPath+'Color.txt','r') as huevos:
            huevoInfo=json.load(huevos)
            for color in list(huevoInfo.keys()):
                if name in huevoInfo[color]:
                    colors=color.lower()
        

        pokeInfo={}
        pokeInfo['nombre']=name
        pokeInfo['id']=globalid
        pokeInfo['color']=colors
        pokeInfo['habitat']=habitats
        pokeInfo['tipos']=tipos
        pokeInfo['stats']=stats
        pokeInfo['grupo']=gruposdehuevo
        pokemonList.append(pokeInfo)

    else:
        print("Se ha recopilado toda la información de la API.")
        break
    
saveThisTo(pokemonList, registroPath+'GlobalData.txt')
print("Se ha compilado la información.")



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


print("Registrando listas de Pokémon por generación.")
for i in range(1,11):
    genList=[]
    with open(registroPath+'GlobalData.txt','r') as datos:
        pokeInfo=json.load(datos)
        for j in genNum(i):
            try:
                print(j)
                genList.append(pokeInfo[j]['nombre'])
            except IndexError:
                print("Se ha terminado de registrar las listas por generación.")
                break

    saveThisTo(genList, registroPath+'Gen'+str(i)+'.txt')
    

print('Listo. Se han actualizado los registros por consulta web.')
