#DANIEL CÁRDENAS ADAME
#obtener la info más reciente de la api y ponerlo en los datos que queremos
import requests as req
import json

def saveThisTo(saving,file):
    with open(file,'w') as guardando:
        json.dump(saving,guardando)


#sección de colores
colorDiccionario={}
for i in range(1,11):
    try:
        colorDex=req.get('https://pokeapi.co/api/v2/pokemon-color/'+str(i)+'/').json()
        
    except:
        break

    name=colorDex['names'][5]['name'].lower()
    pokeList=list()
    for i in range(len(colorDex['pokemon_species'])):
        pokeList.append(colorDex['pokemon_species'][i]['name'])
    
    colorDiccionario[name]=pokeList
saveThisTo(colorDiccionario,'Color.txt')

#sección de tipos

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
saveThisTo(tipoDiccionario,'Tipos.txt')


#sección de habitats

habitatDiccionario={}
for i in range(1,70):
    try:
               
        habitatDex=req.get('https://pokeapi.co/api/v2/pokemon-habitat/'+str(i)+'/').json()
        print(i)
    except:
        break
    
    name=habitatDex['names'][1]['name'].lower()
    pokeList=list()
    for i in range(len(habitatDex['pokemon_species'])):
        pokeList.append(habitatDex['pokemon_species'][i]['name'])
    
    habitatDiccionario[name]=pokeList
saveThisTo(habitatDiccionario,'Habitat.txt')
print('Done')


#sección de huevos

huevoDiccionario={}
for i in range(1,70):
    try:      
        huevoDex=req.get('https://pokeapi.co/api/v2/egg-group/'+str(i)+'/').json()
        print(i)
    except:
        break
    
    name=huevoDex['names'][5]['name'].lower()
    pokeList=list()
    for i in range(len(huevoDex['pokemon_species'])):
        pokeList.append(huevoDex['pokemon_species'][i]['name'])
    
    huevoDiccionario[name]=pokeList
saveThisTo(huevoDiccionario,'GrupoDeHuevo.txt')
print('Done')






#basicamente toda la info

pokemonList=[]
for i in range(1,9999):
    url = f"https://pokeapi.co/api/v2/pokemon/"+str(i)+"/"
    respuesta = req.get(url)
    if respuesta.status_code == 200:
        print(i)
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
        with open('GrupoDeHuevo.txt','r') as huevos:
            huevoInfo=json.load(huevos)
            for huevo in list(huevoInfo.keys()):
                if name in huevoInfo[huevo]:
                    gruposdehuevo.append(huevo.lower())

        habitats=0
        with open('Habitat.txt','r') as huevos:
            #aqui estoy reutilizando la misma estructura que antes
            huevoInfo=json.load(huevos)
            for habitat in list(huevoInfo.keys()):
                if name in huevoInfo[habitat]:
                    habitats=habitat.lower()

        colors=0
        with open('Color.txt','r') as huevos:
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
        break
    
saveThisTo(pokemonList, 'GlobalData.txt')
print('Done')


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



for i in range(1,10):
    genList=[]
    print("")
    print(' -------------- ')
    print(' GENERACION   ')
    print(i)
    print('')

    with open('GlobalData.txt','r') as datos:
        pokeInfo=json.load(datos)
        for j in genNum(i):
            print(j)
            genList.append(pokeInfo[j]['nombre'])


    saveThisTo(genList, 'Gen'+str(i)+'.txt')
    print('Done')

print('Done')


