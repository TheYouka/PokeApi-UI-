#esta función te deja validar datos enteros con mínimo y máximo
#tiene el formato de entrada=string
#entrada es lo que le va a aparecer al usuario al ingresar el valor
#se puede usar maxVal=50 por ejemplo, y se irá directo al valor que se pide
def minmaxInt(entrada,minVal="null",maxVal="null"):
    #Daniel Cárdenas Adame
    while True:
        try:
            a=int(input(entrada))
        except ValueError:
            print("Error, no es una entrada válida.")
            continue
        if minVal!="null":
            if a<minVal:
                print("Error. El valor debe de ser mínimo "+str(minVal)+".")
                continue
        if maxVal!="null":
            if a>maxVal:
                print("Error. El valor debe de ser máximo "+str(maxVal)+".")
                continue
        break
    return a


#esta funcion hace lo mismo que minmaxInt, pero con flotantes en vez de enteros
def minmaxFloat(entrada,minVal="null",maxVal="null"):
    #Daniel Cárdenas Adame
    while True:
        try:
            a=float(input(entrada))
        except ValueError:
            print("Error, no es una entrada válida.")
            continue
        if minVal!="null":
            if a<minVal:
                print("Error. El valor debe de ser mínimo "+str(minVal)+".")
                continue
        if maxVal!="null":
            if a>maxVal:
                print("Error. El valor debe de ser máximo "+str(maxVal)+".")
                continue
        break
    return a


#esta función retorna el string pero con la primera letra en mayuscula
# lo retorna en una variable que se les dé
def mayusPrimer(string):
    #Daniel Cárdenas Adame
    a=string[0]
    b=string[1:len(string)]
    may=a.upper()
    mayusPrim=may+b
    return mayusPrim


#Esto imprime una lista de forma bonita, en el orden en que estén.
#Ejemplo: si se ingresa printList( [1,2,3,4,5,6] )
#Se va a imprimir:    1, 2, 3, 4, 5, 6
#Retorna Falso si no hay elementos, y retorna Verdadero si sí hay,
#Esta parte de retornar no la usé pero podría ayudar a validar.
def printList(lista,casoNulo="No hay elementos"):
    #Daniel Cárdenas Adame
    lista=list(lista)
    if len(lista)==0:
        print(casoNulo)
        return False
    if len(lista)==1:
        print(lista[0])
        return True
    if len(lista)>1:
        print(lista[0],end="")
        for i in range(1,len(lista)):
            print(", "+str(lista[i]),end="")
        print("")
        return True
