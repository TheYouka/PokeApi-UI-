import subprocess

#Función que muestra el menú principal
def show_menu():

	subprocess.run(["banner","Poke App"])

	print("################# ¡Bienvenido a la PokeAPI! #################",end="\n\n")
	print("Una app para conocer todo sobre los pokemones")

	#Imprimir Opciones
	print("""
1- Consultar información sobre los Pokemones

2- Acceder a los registros

3- Acceder a las estadisticas 

4 - Ver gráficas
""")

  #En base a la opción mostrar submenu correspondiente
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




show_menu()

