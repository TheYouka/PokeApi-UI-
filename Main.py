from Modulos import pokeOffline
import json
import requests
import openpyxl
import os


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



opcion=0
while opcion!=6:
        opcion=show_menu()
        #de aquí vamos a hacer los procesos que apliquen para cada sección

        if opcion==1:
                pass

        if opcion==2:
                pass

        if opcion==3:
                pass

        if opcion==4:
                #Daniel Cárdenas Adame
                test=requests.get('https://pokeapi.co/api/v2/pokemon-color/1/').status_code
                if test==200:
                        
                
                        from registros import actualizarDatosPokeAPI as datosMod
                        print('---------- Actualizando ----------')
                        print('')
                        datosMod.ACTUALIZAR()
                        print('')
                        print('---------- Se ha actualizado ----------')
                        print('')
                        print('')

                else:
                        print('Lo sentimos. Esta sección requiere una conexión a internet. Vuelva a intentar después.')

        if opcion==5:
                pass

        if opcion==6:
                #Daniel Cárdenas Adame
                print('')
                print("Muchas gracias por usar este programa.")
        

