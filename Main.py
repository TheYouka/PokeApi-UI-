from Modulos import pokeOffline
from Modulos import globalMod
import json
import requests
import openpyxl
import os
from Modulos.Graficas import Gr_Dic_tipos
from Modulos.Graficas import Gr_Dic_gen_tip
from Modulos.Graficas import Gr_Dic_colores
path=os.getcwd()

print("################# ¡Bienvenido a la PokéAPI! #################",end="\n\n")
print("¡Una app para conocer todo sobre los Pokémon!")
print('')

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

		elif opcion =="4":
			return 4
			break

		elif opcion=="5":
			return 5
		elif opcion=="6":
			return 6
		else:
			print("Ingrese una opción valida. Intente escribir el número.")

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


opcion=0

while opcion!=6:

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
                                                #error
                        
                        elif decIndiv==2:
                                #imprimir info de un solo pokemon
                                pass
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
                                #imprimir toda la info de la generación
                                pass
                        
                        elif decIndiv==2:
                                #imprimir la info de un solo pokemon
                                verif=0
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
                                                nombreMayus=nombre.capitalize()
                                                print('')
                                                pokeOffline.printInfo(nombre)
                                                print('')
                                                print('¿Desea ingresar otro Pokémon?')
                                                verif=siono()-1
                                                print('')
                                        else:
                                                continue
                                        


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
		while True:
	                r=int(input("¿Cuál de las siguientes gráficas deseas consultar?\n1.Gráfica de cantidad de pokemones por color\n2.Gráfica de cantidad de pokemones por tipo\n3.Gráfica de comparación sobre la generación 1 y generación 9 referente a cuantos tipos de pokemones hay\n Opción: "))
			if r==1:
				print(Gr_Dic_colores)
			elif r==2:
				print(Gr_Dic_tipos)
			elif r==3:
				print(Gr_Dic_gen_tip)
			else:
				print("Ingrese de nuevo")
                pass

#----------------------------------------------------------------------

        elif opcion==3:
                #consultar gráficas
                pass

#------------------------------------------------------------------------

        elif opcion==4:
                #actualizar registros
                #Daniel Cárdenas Adame
                test=requests.get('https://pokeapi.co/api/v2/pokemon-color/1/').status_code
                if test==200:
                        
                
                        from registros import actualizarDatosPokeAPI as datosMod
                        print('\n---------- Actualizando ----------')
                        print('')
                        datosMod.ACTUALIZAR()
                        print('')
                        print('---------- Se ha actualizado ----------')
                        print('')
                        print('')

                else:
                        print('Lo sentimos. Esta sección requiere una conexión a internet. Vuelva a intentar después.')

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
        

