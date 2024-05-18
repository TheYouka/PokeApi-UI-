from Modulos import pokeOffline
from Modulos import globalMod
from registros import actualizarDatosPokeAPI as datosMod
import json
import requests
import openpyxl
import os
import random
from pathlib import Path

def saveThisTo(jsonDic,archivo):
        with open(archivo, 'w') as file:
                json.dump(jsonDic,file)
        a=0
        #se cierra función

def isOnline():
        test=requests.get('https://pokeapi.co/api/v2/pokemon-color/1/').status_code
        if test==200:
                return True
        else:
                return False
        
        

from Modulos.Graficas import Gr_Dic_colores
from Modulos.Graficas import Gr_Dic_colores_Gen as colorGrafGen
from Modulos.Graficas import Gr_Dic_tipos
from Modulos.Graficas import Gr_Dic_tipos_Gen as tiposGrafGen
from Modulos.Graficas import Gr_Dic_gen_tip_Gen as grafCompararGen
from Modulos.Graficas import habilidadesPokemon
from Modulos.Graficas import Estadisticas
from Modulos.Graficas import tablaPokeProp




path=os.getcwd()
pathRegistro=os.path.join(path,'registros')

def checkCrear(filename, jsonDic):
    # Verificar si el archivo existe
    if not os.path.exists(filename):
        # Si el archivo no existe, crearlo y asignarle el contenido
        with open(filename, 'w') as file:
            json.dump(jsonDic,file)
    else:
            a=0
            #no hacer nada


print("################# ¡Bienvenido a la PokéAPI! #################",end="\n\n")
print("¡Una app para conocer todo sobre los Pokémon!")
print('')


#-------------------------------------------------------------------------------------------
#Menu de edición
def edite_menu():
        print("¡Bienvenido al menú de edición, aqui puede agregar datos al registro")

        pokemon = {}

        name = input("¿Cúal es el nombre de su pokemon?")

        print("""Ingresa el color de tu pokemon, las opciones validas son:
- Negro
- Azul
- Marrón
- Gris
- Verde
- Rosa
- Morado
- Rojo
- Blanco
- Amarillo""")

        color = input(">> ").lower()
        
        while color not in ["negro","azul","marrón","gris","verde","rosa","morado","rojo","blanco","amarillo"]:
                print("Ingresa una opcion valida")
                color = input(">> ").lower()


        print("""Ingresa el tipo de tu pokemon, las opciones validas son:
- normal
- fighting
- flying
- poison
- ground
- rock
- bug
- ghost
- steel
- fire
- water
- grass
- electric
- psychic
- ice
- dragon
- dark
- fairy
- stellar
- unknown
""")

        tipo = input(">> ").lower()
        while tipo not in ["normal", "fighting", "flying", "poison", "ground", "rock", "bug", "ghost", "steel", "fire", "water", "grass", "electric", "psychic", "ice", "dragon", "dark", "fairy", "stellar", "unknown"]:
                print("Ingresa una opcion valida")
                tipo = input(">> ").lower()


        print("""Ingresa el grupo al que pertenece tu pokemon, las opciones validas son:
- monster
- water1
- bug
- flying
- ground
- fairy
- plant
- humanshape
- water3
- mineral
- indeterminate
- water2
- ditto
- dragon
- no-eggs
""")
        
        grupo = input(">> ").lower()
        while grupo not in ["monster", "water1", "bug", "flying", "ground", "fairy", "plant", "humanshape", "water3", "mineral", "indeterminate", "water2", "ditto", "dragon", "no-eggs"]:
                print("Ingresa una opcion valida")
                grupo = input(">> ").lower()

        print("""Ingresa el grupo al que pertenece tu pokemon, las opciones validas son:
- Caverna               
- bosque
- pradera
- montaña
- raro
- campo 
- mar
- ciudad
- agua salada

""")

        habitat = input(">> ").lower()
        while habitat not in ["caverna", "bosque", "pradera", "montaña", "raro", "campo", "mar", "ciudad", "agua salada"]:
                print("Ingresa una opcion valida")
                habitat = input(">> ").lower()


        #Generar id random
        id_ = random.randint(1000, 9999)

        #Añadir info de pokemon
        pokemon["name"] = name
        pokemon["tipo"] = tipo
        pokemon["color"] = color
        pokemon["habitat"] = habitat
        pokemon["grupo"] = grupo
        pokemon["id"] = id_

        Pokemones[name] = pokemon

        registroPath=os.path.join(path,"registros")
        datosMod.saveThisTo(Pokemones, os.path.join(registroPath,'GlobalData.txt'))
        
        print(Pokemones["goku"])
        

#-------------------------------------------------------------------------------------------


def update():
        if isOnline():
                print('---------- Actualizando ----------')
                print('')
                Pokemones = datosMod.ACTUALIZAR()
                print('')
                print('---------- Se ha actualizado ----------')
                print('')
                print('')

        else:
                print('[WARNING] Los registros no están actualizados, proceda con precaución')

        return Pokemones

def show_menu():

        #Imprimir Opciones
        print("""Seleccione una de las siguientes opciones:

1- Consultar información sobre los Pokémon

2- Acceder a las estadisticas 

3- Ver gráficas

4- Actualizar registros

5- Borrar datos creados por el programa

6- Salir del programa
""")

        while True:
                        
                seleccion=str(input('>> '))

                if seleccion=='1':
                        return 1
                elif seleccion=='2':
                        return 2
                elif seleccion =='3':
                        return 3
                elif seleccion=='4':
                        return 4
                elif seleccion=='5':
                        return 5
                elif seleccion=='6':
                        return 6
                else:
                        print('Vuelva a intentar. Intente escribir el número.')


#fin de función showmenu()


def menuConsultar():

        #Imprimir Opciones
        print("""Seleccione una de las siguientes opciones:

1- Consultar información de cualquier Pokémon

2- Consultar información de Pokémon por generación

3- Agregar información de un Pokémon nuevo
""")


        while True: 
                opcion = str(input(">> "))
                if opcion == "1":
                        return 1
                        break

                elif opcion == "2":
                        return 2
                        break

                elif opcion == "3":
                        return 3
                        break
                
                else:
                        print("Ingrese una opción valida. Intente escribir el número.")

#fin de función menuConsultar()

def menuIndivOrTodos():
        #Imprimir Opciones
        print("""Seleccione lo que quiere hacer:

1- Imprimir la información de todos los Pokémon.

2- Imprimir la información de un Pokémon específico.
""")


        while True: 
                opcion = str(input(">> "))
                if opcion == "1":
                        return 1
                        break

                elif opcion == "2":
                        return 2
                        break
                
                else:
                        print("Ingrese una opción valida. Intente escribir el número.")

#fin de función menuIndivOrTodos()


def siono():
        print("""1. Sí
2. No
""")
        while True:
                
                opcion=str(input('>> '))

                if opcion.strip()=='1' or opcion.lower().strip()=='si' or opcion.lower().strip()=='sí':
                        return 1
                elif opcion.strip()=='2' or opcion.lower().strip()=='no':
                        return 2
                else:
                        print("Ingrese una opción valida. Revise su ortografía.")


Pokemones=pokeOffline.abrirRegistro('GlobalData.txt')

opcion=0

while opcion!=6:

        checkCrear(os.path.join(pathRegistro,'GrFila.txt'),{'color':1,'tipo':1,'tipoGen':1,'habilidad':1})
        GrFila=pokeOffline.abrirRegistro('GrFila.txt')
        
        opcion=show_menu()
        
        #de aquí vamos a hacer los procesos que apliquen para cada sección



#-----------------------------------------------------------------

        
        if opcion==1:
                #consultar info de pokemones
                print('')
                pokeInfo=pokeOffline.abrirRegistro('GlobalData.txt')
                opcionPoke=menuConsultar()
                
                if opcionPoke==1:
                        print('')
                        genList=[]
                        for i in range(1,11):
                                genList+=abrirRegistro('Gen'+str(i)+'.txt')
                        totPoke=len(genList)
                        decIndiv=menuIndivOrTodos()

                        if decIndiv==1:
                                #imprimir la info de todos los pokemones
                                for i in range(1,totPoke+1):
                                        try:
                                                nombre=pokeOffline.numToName(i)
                                                print('')
                                                pokeOffline.printInfo(nombre)
                                                print('')
                                        except:
                                                print('Error.')
                                                pass
                                                #error
                                print('¿Desea guardar esta información en las consultas?')
                                verif=siono()
                                if verif==1:
                                        ##guardar en excel
                                        print('\nEspere un momento')
                                        for i in range(1,totPoke+1):
                                                name=pokeOffline.numToName(i)
                                                if tablaPokeProp.guardarPoke(name,pokeInfo[name],hoja='Nacional'):
                                                        verifPoke=1
                                                else:
                                                        print('Error. Intente cerrar el archivo de Excel.')
                                        if verifPoke==1:
                                                print('Listo, se ha guardado en el Excel de "Información" en la carpeta de Consultas. La hoja es "Nacional"\n')
                        
                        elif decIndiv==2:
                                #imprimir la info de un solo pokemon
                                verif=0
                                checkPoke=[]
                                while verif==0:

                                        pokemon=str(input('\nIngrese el nombre o el número de un Pokémon.\n>> ')).lower()
                                        
                                        if str(pokemon).isdigit():
                                                #ingresó un número
                                                pokemon=int(pokemon)
                                                try:
                                                        #sí está en la generación
                                                        nombre=pokeOffline.numToName(pokemon)
                                                        verif=1
                                                except:
                                                        print('Error. Vuelva a intentar. Puede que ese Pokémon no sea válido.')
                                                        verif=0

                                        else:
                                                try:
                                                        numero=int(pokeInfo[pokemon]['id'])
                                                        nombre=pokemon
                                                        
                                                except:
                                                        print('Error. Vuelva a intentar. Puede que ese Pokémon no sea válido.')
                                                        verif=0
                                        
                                        if verif!=0:
                                                checkPoke.append(nombre)
                                                nombreMayus=nombre.capitalize()
                                                print('')
                                                pokeOffline.printInfo(nombre)
                                                print('')
                                                print('¿Desea ingresar otro Pokémon?')
                                                verif=siono()-1
                                                print('')

                                                if verif==1:
                                                        print('¿Desea guardar esta información en las consultas?')
                                                        verif=siono()
                                                        if verif==1:
                                                                ##guardar en excel
                                                                for pokemonName in checkPoke:
                                                                        if tablaPokeProp.guardarPoke(pokemonName,pokeInfo[pokemonName],hoja='Individuales'):
                                                                                verifPoke=1
                                                                        else:
                                                                                print('Error. Intente cerrar el archivo de Excel.')
                                                                if verifPoke==1:
                                                                        print('Listo, se ha guardado en el Excel de "Información" en la carpeta de Consultas. La hoja es "Individuales"\n')

                                                checkPoke=[]

                                        
                                        else:
                                                continue
        
                                        
                        else:
                                print('Error')
                
                elif opcionPoke==2:
                        gen=globalMod.minmaxInt('\nIngrese la generación que desea analizar.\n>> ',minVal=1,maxVal=9)
                        genList=pokeOffline.abrirRegistro('Gen'+str(gen)+'.txt')
                        #se carga la lista de los pokemon de la generación
                        genSet=set(genList) #esto hace un conjunto y sirve para intersecciones
                        genMin=pokeOffline.genMin(gen)
                        genMax=pokeOffline.genMax(gen)
                        genPrevTot=pokeOffline.genPrevTot(gen)
                        print('')

                        decIndiv=menuIndivOrTodos()

                        if decIndiv==1:
                                #imprimir la info de todos los pokemones
                                for i in range(genMin,genMax+1):
                                        try:
                                                nombre=pokeOffline.numToName(i)
                                                print('')
                                                pokeOffline.printInfo(nombre)
                                                print('')
                                        except:
                                                print('')
                                                pass
                                                #error
                                print('¿Desea guardar esta información en las consultas?')
                                verif=siono()
                                if verif==1:
                                        ##guardar en excel
                                        print('Espere un momento.')
                                        for i in range(genMin,genMax+1):
                                                name=pokeOffline.numToName(i)
                                                if tablaPokeProp.guardarPoke(name,pokeInfo[name],hoja='Generación '+str(gen)):
                                                        verifPoke=1
                                                else:
                                                        print('Error. Intente cerrar el archivo de Excel.')
                                        if verifPoke==1:
                                                print('Listo, su información se encuentra en la hoja de "Generación '+str(gen)+'" dentro del Excel de "Información" en la carpeta de Consultas\n')
                        
                        elif decIndiv==2:
                                #imprimir la info de un solo pokemon
                                verif=0
                                checkPoke=[]
                                while verif==0:

                                        pokemon=str(input('\nIngrese el nombre o el número de un Pokémon de la generación '+str(gen)+'.\n>> ')).lower()
                                        
                                        if str(pokemon).isdigit():
                                                #ingresó un número
                                                pokemon=int(pokemon)
                                                if pokeOffline.isInGen(pokemon+genPrevTot,gen):
                                                        #sí está en la generación
                                                        nombre=pokeOffline.numToName(pokemon+genPrevTot)
                                                        verif=1
                                                else:
                                                        print('Error. Vuelva a intentar. Puede que ese Pokémon no sea válido en esta generación.')
                                                        verif=0

                                        else:
                                                try:
                                                        numero=int(pokeInfo[pokemon]['id'])
                                                        if pokeOffline.isInGen(numero,gen):
                                                                #sí está en la generación
                                                                nombre=pokeOffline.numToName(numero)
                                                                verif=1
                                                        else:
                                                                print('Error. Vuelva a intentar. Puede que ese Pokémon no sea válido en esta generación.')
                                                                verif=0
                                                        
                                                except:
                                                        print('Error. Vuelva a intentar. Puede que ese Pokémon no sea válido en esta generación.')
                                                        verif=0

                                        if verif!=0:
                                                checkPoke.append(nombre)
                                                nombreMayus=nombre.capitalize()
                                                print('')
                                                pokeOffline.printInfo(nombre)
                                                print('')
                                                print('¿Desea ingresar otro Pokémon?')
                                                verif=siono()-1
                                                print('')
                                        else:
                                                continue
                                print('¿Desea guardar esta información en las consultas?')
                                verif=siono()
                                if verif==1:
                                        ##guardar en excel
                                        for pokemonName in checkPoke:
                                                if tablaPokeProp.guardarPoke(pokemonName,pokeInfo[pokemonName],hoja='Individuales'):
                                                        verifPoke=1
                                                else:
                                                        print('Error. Intente cerrar el archivo de Excel.')
                                        if verifPoke==1:
                                                print('Listo, se ha guardado en el Excel de "Información" en la carpeta de Consultas. La hoja es "Individuales"')
                                checkPoke=[]
                                        
                                        
                                        
                                        


                        else:
                                print('Error')
                                
                        
                
                elif opcionPoke==3:
                        pass

                else:
                        print('Error.')
                
#--------------------------------------------------------------------------------------

        elif opcion==2:
                #consultar estadísticas
                #Janis Aideé Reyna Garza
                Estadisticas.estadisticas()

#----------------------------------------------------------------------

        elif opcion==3:
               #consultar gráficas
                #Janis Aideé Reyna Garza
                while True:
                        try:
                                print("\n¿Cuál de las siguientes gráficas deseas consultar?\n1. Gráfica de cantidad de Pokémon por color\n2. Gráfica de cantidad de Pokémon por tipo\n3. Gráfica de comparación sobre la cantidad de tipos de dos generaciones")
                                if isOnline():
                                        print('4. Gráfica de habilidades de un Pokémon')
                                r=int(input(">> "))
                        except:
                                r=0
                        if r==4:
                                if isOnline():
                                        r=4
                                else:
                                        r=0
                        #listo, se validó las opciones
                        if r==1:
                                gen=str(input('\nIngrese la generación que quiera analizar. Si quiere analizar todas, ingrese 0.\n>> '))
                                if gen.isdigit():
                                        gen=int(gen)
                                        if gen>=1 and gen<=9:
                                                gen=gen
                                        else:
                                                gen=0
                                else:
                                        gen=0
                                if gen==0:

                                        if Gr_Dic_colores.grafColor(GrFila['color']):
                                                print('')
                                                print('Listo. Se guardó la gráfica en la hoja de "Color" en el Excel "Gráficas.xlsx" dentro de las Consultas')
                                                GrFila['color']+=30
                                                print('')
                                                saveThisTo(GrFila,os.path.join(pathRegistro,'GrFila.txt'))
                                                break
                                        else:
                                                print('Error. Intente cerrar el archivo de Excel para que se guarde.')
                                                
                                else:
                                        if colorGrafGen.grafColor(gen,GrFila['color']):
                                                #guardando las filas correspondientes
                                                print('')
                                                print('Listo. Se guardó la gráfica en la hoja de "Color" en el Excel "Gráficas.xlsx" dentro de las Consultas')
                                                GrFila['color']+=30
                                                print('')
                                                saveThisTo(GrFila,os.path.join(pathRegistro,'GrFila.txt'))
                                                break
                                        else:
                                                print('Error. Intente cerrar el archivo de Excel para que se guarde.')
                                
                                
                        elif r==2:

                                gen=str(input('\nIngrese la generación que quiera analizar. Si quiere analizar todas, ingrese 0.\n>> '))
                                if gen.isdigit():
                                        gen=int(gen)
                                        if gen>=1 and gen<=9:
                                                gen=gen
                                        else:
                                                gen=0
                                else:
                                        gen=0
                                if gen==0:

                                        if Gr_Dic_tipos.grafTipos(GrFila['tipo']):
                                                print('')
                                                print('Listo. Se guardó la gráfica en la hoja de "Tipos" en el Excel "Gráficas.xlsx" dentro de las Consultas')
                                                GrFila['tipo']+=30
                                                print('')
                                                saveThisTo(GrFila,os.path.join(pathRegistro,'GrFila.txt'))
                                                break
                                        else:
                                                print('Error. Intente cerrar el archivo de Excel para que se guarde.')
                                else:
                                        if tiposGrafGen.grafTipos(gen,GrFila['tipo']):
                                                #guardando las filas correspondientes
                                                print('')
                                                print('Listo. Se guardó la gráfica en la hoja de "Tipos" en el Excel "Gráficas.xlsx" dentro de las Consultas')
                                                GrFila['tipo']+=30
                                                print('')
                                                saveThisTo(GrFila,os.path.join(pathRegistro,'GrFila.txt'))
                                                break
                                        else:
                                                print('Error. Intente cerrar el archivo de Excel para que se guarde.')
                                
                        elif r==3:

                                gen1=globalMod.minmaxInt('\nIngrese la primera generación por analizar.\n>> ',minVal=1,maxVal=9)
                                while True:
                                        gen2=globalMod.minmaxInt('\nIngrese la segunda generación por analizar.\n>> ',minVal=1,maxVal=9)
                                        if gen2==gen1:
                                                print('\nLas generaciones que escogió son las mismas. Vuelva a intentar.\n>>')
                                                continue
                                        else:
                                                break

                                if grafCompararGen.compararTipos(gen1,gen2,GrFila['tipoGen']):
                                        #Esto va antes de un break
                                        GrFila['tipoGen']+=30
                                        print('')
                                        print('Listo. Se guardó la gráfica en la hoja de "Comparaciones de tipos" en el Excel "Gráficas.xlsx" dentro de las Consultas')
                                        print('')
                                        saveThisTo(GrFila,os.path.join(pathRegistro,'GrFila.txt'))
                                        break
                                else:
                                        print('Error.')

                        elif r==4 and isOnline():
                                print('\nIngrese el nombre o el número nacional de un Pokémon')
                                while True:
                                        poke=str(input('>> '))
                                        if poke.isdigit():
                                                try:
                                                        name=pokeOffline.numToName(poke).capitalize()
                                                except:
                                                        print('\nHubo un error. Puede que ese Pokémon no exista. Vuelva a intentar.\n')
                                                        continue
                                                else:
                                                        num=poke
                                                        break
                                        else:
                                                try:
                                                        num=pokeOffline.nameToNum(poke)
                                                except:
                                                        print('\nHubo un error. Puede que ese Pokémon no exista. Vuelva a intentar.\n')
                                                        continue
                                                else:
                                                        name=poke.capitalize()
                                                        break
                                #####imprimiendo la gráfica del pokemon
                                stats=habilidadesPokemon.getStats(num)
                                if habilidadesPokemon.graphStats(stats,name,fila=GrFila['habilidad']):
                                        #Esto va antes de un break
                                        GrFila['habilidad']+=30
                                        print('')
                                        print('Listo. Se guardó la gráfica en la hoja de "Habilidades" en el Excel "Gráficas.xlsx" dentro de las Consultas')
                                        print('')
                                        saveThisTo(GrFila,os.path.join(pathRegistro,'GrFila.txt'))
                                        break
                                else:
                                        print('Error.')
                                        
                                

                                        
                        else:
                                print("Ingrese de nuevo.")
                                continue

#------------------------------------------------------------------------
        
        ## Función Para actualizar los pokemnoes
        elif opcion==4:
                edite_menu()

#------------------------------------------------------------------------

        elif opcion==5:
                #borrar información
                pass

#-------------------------------------------------------------------------

        elif opcion==6:
                #Salir del programa
                #Daniel Cárdenas Adame
                print('')
                print("Muchas gracias por usar este programa.")

#--------------------------------------------------------------------------------

        else:
                print('Error')


# FIN DEL PROGRAMA
#  =D
        

