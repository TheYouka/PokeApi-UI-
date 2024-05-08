#import subprocess
import pyfiglet
from Modulos import pokeOffline


def show_menu():

	print(pyfiglet.figlet_format("Poke App"))

	print("################# ¡Bienvenido a la PokeAPI! #################",end="\n\n")
	print("Una app para conocer todo sobre los pokemones")

	#Imprimir Opciones
	print("""
1- Consultar información sobre los Pokemones

2- Acceder a los registros

3- Acceder a las estadisticas 

4 - Ver gráficas
""")


	while True: 
		opcion = input(">> ")
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

		else:
			print("Ingrese una opción valida")



pokeOffline.By_color()
#show_menu()
#menu_offline.rewrite_data()
