#import subprocess
import pyfiglet
from Modulos import pokeOffline


def show_menu():

	print(pyfiglet.figlet_format("Poké App"))

	print("################# ¡Bienvenido a la PokéAPI! #################",end="\n\n")
	print("¡Una app para conocer todo sobre los Pokémon!")

	#Imprimir Opciones
	print("""
1- Consultar información sobre los Pokémon

2- Acceder a las estadisticas 

3- Ver gráficas

4- Actualizar registros

5- Borrar datos creados por el programa.
""")


	while True: 
		opcion = str(input(">> "))
		if opcion == "1":
			pass
			break

		elif opcion == "2":
			pass
			break

		elif opcion == "3":
			pass
			break

		elif opcion =="4":
			pass
			break

		elif opcion=="5"
			pass
			break
		
		else:
			print("Ingrese una opción valida. Intente escribir el número.")




show_menu()
#menu_offline.rewrite_data()
