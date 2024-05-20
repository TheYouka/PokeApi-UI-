
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
from Modulos import pokeOffline







path=os.getcwd()
pathRegistro=os.path.join(path,'registros')




pathGlobalData=os.path.join(pathRegistro,'GlobalData.txt')


        



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
        Pokemones=pokeOffline.abrirRegistro('GlobalData.txt')
        Colores=pokeOffline.abrirRegistro('Color.txt')
        Habitats=pokeOffline.abrirRegistro('Habitat.txt')
        Tipos=pokeOffline.abrirRegistro('Tipos.txt')
        Grupos=pokeOffline.abrirRegistro('GrupoDeHuevo.txt')
        Gen10=pokeOffline.abrirRegistro('Gen10.txt')

        name = input("¿Cúal es el nombre de su Pokémon?\n>> ")

        print("""\nIngrese el color de su Pokémon, las opciones válidas son:
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
                print("\nIngrese una opcion valida. Revise su ortografía.")
                color = input(">> ").lower()

        Colores[color].append(name)


        print("""\nIngrese el primer tipo de su Pokémon, las opciones válidas son:
- Normal
- Lucha
- Volador
- Veneno
- Tierra
- Roca
- Bicho
- Fantasma
- Acero
- Fuego
- Agua
- Planta
- Eléctrico
- Psíquico
- Hielo
- Dragón
- Siniestro
- Hada
- Stellar
""")
        tipos = []
        tipo1 = input(">> ").lower()
        while tipo1 not in ['normal', 'lucha', 'volador', 'veneno', 'tierra', 'roca', 'bicho', 'fantasma', 'acero', 'fuego', 'agua', 'planta', 'eléctrico', 'psíquico', 'hielo', 'dragón', 'siniestro', 'hada', 'stellar']:
                print("\nIngrese una opcion valida. Revise su ortografía.")
                tipo1 = input(">> ").lower()

        print("""\nIngrese el primer tipo de su Pokémon, las opciones válidas son:
- Normal
- Lucha
- Volador
- Veneno
- Tierra
- Roca
- Bicho
- Fantasma
- Acero
- Fuego
- Agua
- Planta
- Eléctrico
- Psíquico
- Hielo
- Dragón
- Siniestro
- Hada
- Stellar
- Ninguno
""")

        tipo2 = input(">> ").lower()
        while tipo2 not in ['normal', 'lucha', 'volador', 'veneno', 'tierra', 'roca', 'bicho', 'fantasma', 'acero', 'fuego', 'agua', 'planta', 'eléctrico', 'psíquico', 'hielo', 'dragón', 'siniestro', 'hada', 'stellar', 'ninguno']:
                print("\nIngrese una opcion valida. Revise su ortografía.")
                tipo2 = input(">> ").lower()


        if tipo2=='ninguno':
                #tipos=[tipo1,tipo2]
                tipos.append(tipo1)
                #Tipos[tipo2].append(name)
        else:
                tipos.append(tipo1)
                tipos.append(tipo2)

        #Tipos[tipo1].append(name)


        print("""\nIngrese el primer grupo de huevo al que pertenece su Pokémon, las opciones válidas son:
- Monstruo
- Agua 1
- Bicho
- Volador
- Campo
- Hada
- Planta
- Humanoide
- Agua 3
- Mineral
- Amorfo
- Agua 3
- Agua 2
- Ditto
- Dragón
- Desconocido
""")
        grupos = []
        grupo1 = input(">> ").lower()
        while grupo1 not in ['monstruo', 'agua 1', 'bicho', 'volador', 'campo', 'hada', 'planta', 'humanoide', 'agua 3', 'mineral', 'amorfo', 'agua 2', 'ditto', 'dragón', 'desconocido']:
                print("\nIngrese una opcion valida. Revise su ortografía.")
                grupo1 = input(">> ").lower()

        print("""\nIngrese el segundo grupo de huevo al que pertenece su Pokémon, las opciones válidas son:
- Monstruo
- Agua 1
- Bicho
- Volador
- Campo
- Hada
- Planta
- Humanoide
- Agua 3
- Mineral
- Amorfo
- Agua 3
- Agua 2
- Ditto
- Dragón
- Desconocido
- Ninguno
""")
        
        grupo2 = input(">> ").lower()
        while grupo2 not in ['monstruo', 'agua 1', 'bicho', 'volador', 'campo', 'hada', 'planta', 'humanoide', 'agua 3', 'mineral', 'amorfo', 'agua 2', 'ditto', 'dragón', 'desconocido','ninguno']:
                print("\nIngrese una opcion valida. Revise su ortografía.")
                grupo2 = input(">> ").lower()

        if grupo2=='ninguno':
                grupos.append(grupo1)
        else:
                grupos.append(grupo1)
                grupos.append(grupo2)

        #Grupos[grupo1].append(name)
                

        print("""Ingrese el hábitat al que pertenece su Pokémon, las opciones válidas son:
- Caverna               
- Bosque
- Pradera
- Montaña
- Raro
- Campo
- Mar
- Ciudad
- Agua salada
- Ninguno
""")

        habitat = input(">> ").lower()
        while habitat not in ["caverna", "bosque", "pradera", "montaña", "raro", "campo", "mar", "ciudad", "agua salada", 'ninguno']:
                print("\nIngrese una opcion valida. Revise su ortografía.")
                habitat = input(">> ").lower()


        if habitat!='ninguno':
                Habitats[habitat].append(name)


        #Generar id random
        id_ = random.randint(1026, 9999)

        #Añadir info de pokemon
        pokemon["name"] = name
        pokemon["tipo"] = tipos
        pokemon["color"] = color
        pokemon["habitat"] = habitat
        pokemon["grupo"] = grupos
        pokemon["id"] = id_

        Pokemones[name] = pokemon

        print('\nListo, la información de su Pokémon se ha registrado.\n')
        
        registroPath=os.path.join(path,"registros")
        datosMod.saveThisTo(Pokemones, os.path.join(registroPath,'GlobalData.txt'))
        datosMod.saveThisTo(Habitats, os.path.join(registroPath,'Habitat.txt'))
        datosMod.saveThisTo(Grupos, os.path.join(registroPath,'GrupoDeHuevo.txt'))
        datosMod.saveThisTo(Colores, os.path.join(registroPath,'Color.txt'))
        datosMod.saveThisTo(Tipos, os.path.join(registroPath,'Tipos.txt'))
        
       
        

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

















opcion=0

while opcion!=6:

        checkCrear(os.path.join(pathRegistro,'GrFila.txt'),{'color':1,'tipo':1,'tipoGen':1,'habilidad':1})
        GrFila=pokeOffline.abrirRegistro('GrFila.txt')
        
        


        try:
                Pokemones=pokeOffline.abrirRegistro('GlobalData.txt')
                a=Pokemones['snorlax']
                opcion=show_menu()
        except:
                print('Antes de continuar, se deben de actualizar los datos.\n')
                print('')
                update()
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
                                genList+=pokeOffline.abrirRegistro('Gen'+str(i)+'.txt')
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
                                                        verif=1
                                                        
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
                while True:
                        dec4=str(input("""¿Qué desea hacer?
1- Actualizar los registros con los datos de la API
(Advertencia: Esto borrará los Pokémon que se hayan creado)
2- Crear un Pokémon nuevo.

>> """))
                        if dec4.isdigit():
                                if dec4=='1':
                                        dec4=1
                                        break
                                elif dec4=='2':
                                        dec4=2
                                        break
                                else:
                                        print('\nVuelva a intentar. Esa opción no es válida.\n')
                        else:
                                print('\nVuelva a intentar. Ingrese el número.\n')
                                
                if dec4==2:
                        edite_menu()

                elif dec4==1:
                        update()

                else:
                        print('Error')

#------------------------------------------------------------------------

        elif opcion==5:
                #borrar información de los registros guardados en txt
                while True:
                                
                        try:
                                
                                folder = Path(os.path.join(os.getcwd(),"registros"))

                                for file in folder.iterdir():
                                        if file.suffix == ".txt":

                                                #Vaciar archivos
                                                with open(str(file),"w") as f:
                                                        f.write("{}")

                                #aquí borrando en las consultas
                                folder = Path(os.path.join(os.getcwd(),"Consultas"))

                                for file in folder.iterdir():
                                        if file.suffix == ".xlsx":

                                                #Eliminar archivos.
                                                os.remove(file)

                                #diciéndole al usuario
                                print('\nListo. Los archivos se han borrado.\n')
                                break

                        except:
                                a=input('\nOcurrió un error. Revise que no estén abiertos los archivos.\nLo esperaremos.\n>> ')
                                continue
                                
                                

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
        

