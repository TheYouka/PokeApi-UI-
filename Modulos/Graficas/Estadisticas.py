def ejecutarmenu(): 
    while True:
        print("\nSeleccione una opción:\n1.Cantidad de pokemones por color\n2.El color que tiene más pokemones\n3.Cantidad de pokemones por su grupo de huevo\n4.El grupo de huevo con más pokemones\n5.La cantidad de cada hábitat\n6.Exit")
        r1=int(input("Opción: "))
        if r1==1:
            cua_cada(wb,ws,dic)
        elif r1==2:
            printmodaco(ws,ind,ma)
        elif r1==3:
            cgp(pagina3,nongh)
        elif r1==4:
            printgpp(nongh,ma,ngh,pagina3)
        elif r1==5:
            path=os.path.join(os.path.dirname(__file__), 'Habitats.xlsx')
            wb2=load_workbook(filename=path)
            ws2=wb2.active
            porch(ws2)
        elif r1==6:
            return
        else:
            pass
            print("Ingrese una de las opciones brindadas")
def modaco(wb,ws):
    s=-1
    listas={}
    for i in range(0,10):
        c=i+1
        s=s+1
        nam=f"L{c}"
        listas[nam]=[]
        for row in ws.iter_rows(min_row=2, max_col=c, values_only=True):
            valor = row[s]
            if valor is None:
                continue
                
            if valor != 0:
                listas[nam].append(valor)
                continue
    dic=[]
    for i in range (0,10):
        d=len(listas['L'+str(i+1)])
        dic.append(d)
    ma=0
    for i in range (0,len(dic)):
        if dic[i]>ma:
            ma=dic[i]  
        else:
            pass
    ind=dic.index(ma)
    key=list(listas.keys())
    key[ind]
    wb.save("GrColor.xlsx")
    return ind, ma, dic

def printmodaco(ws,ind,ma):
    m=ws.cell(row=1, column=(ind+1))
    print("El color que más se repite es " +str(m.value)+ " con " + str(ma) +" pokemones")
    exit
    
def cua_cada(wb,ws,dic):
    while True:
            k=int(input("Selecciona una opción \n1.Todos los pokemones\n2.Uno en específico\n3.Volver al menú  "))
            if k==1:
                for i in range (1,11):
                    cv=ws.cell(row=1,column=i)
                    va=dic[i-1]
                    print("El color "+ str(cv.value) +" tiene " + str(va)+" pokemones")
            elif k==2:
                cuacaop2(wb,ws,dic)

            elif k==3:
                print("Volviendo al menú....")
                break
            else:
                print("Ingrese nuevamente\n")
def cuacaop2(wb,ws,dic):
    ola=[]
    diccolores={}
    for j in range (1,11):
        m=ws.cell(row=1, column=(j))
        m=m.value
        ola.append(m)
        diccolores[j]=ola[j-1]
    while True:
            print("Ingrese un opción de acuerdo al índice que corresponda\n"+str(diccolores)+"\n11.Exit")
            n=(int(input("  :   ")))
            if n==11:
                return
            elif n<11 and n>0:
                va=dic[n-1]
                print("El color "+str(diccolores[n])+" contiene "+str(va)+" pokemones")
            else:
                print("Ingrese de nuevo")

def porch(ws2):
    #Porcentaje de cada habitat
    s=-1
    hab={}
    for i in range(0,9):
        c=i+1
        s=s+1
        nam=f"L{c}"
        hab[nam]=[]
        for row in ws2.iter_rows(min_row=2, max_col=c, values_only=True):
            valor = row[s]
            if valor is None:
                continue
                
            if valor != 0:
                hab[nam].append(valor)
                continue
    ongdh=[]
    for i in range (0,9):
        d=len(hab['L'+str(i+1)])
        ongdh.append(d)
    s=sum(ongdh)
    por=[]
    for i in range (0,9):
        a=ongdh[i]
        c=a*(100/s)
        por.append(a)
    sn=1
    while True:
        print("Ingrese el número del hábitat del que desea conocer su porcentaje:\n1.Cueva\n2.Bosque\n3.Campo\n4.Montaña\n5.Raro\n6.Terreno rocoso\n7.Oceano\n8.Urbano\n9.Costas\n10.Volver al menú principal ")
        r=int(input("\n Opción: "))
        if 1<=r<=9:
            for i in range (1,10):
                if r==i:
                    t=ws2.cell(row=1, column=i)
                    x=t.value
                    y=x.capitalize()
                    print('Hay '+str(por[i-1])+'% del hábitat '+y)
        elif r==10:
            break

        else:
            print("Ingrese de nuevo")
def cgp(ws3,nongh):
    while True:
        r=int(input("Seleccione una opción:\n1.Vizualizar la cantidad de todos los grupos de huevos\n2.Visualizar un cierto tipo\n3.Volver al menú\nOpción: "))
        if r==1:
            for i in range (1,15):
                cv=ws3.cell(row=1,column=i)
                cv=cv.value
                cv=cv.capitalize()
                va=nongh[i-1]
                print("El grupo de huevo "+ str(cv) +" tiene " + str(va)+" pokemones\n")
        elif r==2:
            pricgp(pagina3,nongh)
        elif r==3:
            return
        else:
            print("Ingrese nuevamente")
def pricgp(ws3,nongh):
    titulos=[]
    opc={}
    for i in range (1,15):
        m=ws3.cell(row=1, column=(i))
        m=m.value
        titulos.append(m)
        opc[i]=titulos[i-1]
    while True:
        u=int(input("Ingrese una opción\n"+str(opc)+"\n15.Volver atrás\nOpción: "))
        if u==15:
            return
        elif u<15 and u>0:
            va=nongh[u-1]
            print("El grupo de huevo "+str(opc[u])+" contiene "+str(va)+" pokemones")
        else:
            print("Intente de nuevo\n")
def gpp(pagina3):
    s=-1
    ngh={}
    for i in range(0,16):
        c=i+1
        s=s+1
        nam=f"L{c}"
        ngh[nam]=[]
        for row in pagina3.iter_rows(min_row=2, max_col=c, values_only=True):
            valor = row[s]
            if valor is None:
                continue
                
            if valor != 0:
                ngh[nam].append(valor)
                continue
    nongh=[]
    for i in range (0,16):
        d=len(ngh['L'+str(i+1)])
        nongh.append(d)
    ma=0
    for i in range (0,len(nongh)):
        if nongh[i]>ma:
            ma=nongh[i]  
        else:
            pass
    worbe.save("Gpohvs.xlsx")
    return nongh,ma,ngh,pagina3
def printgpp(nongh,ma,ngh,pagina3):
    ind=nongh.index(ma)
    key=list(ngh.keys())
    key[ind]
    m=pagina3.cell(row=1, column=(ind+1))
    m=m.value
    m=m.capitalize()
    print("El grupo de huevo que más se repite es " +str(m)+ " con " + str(ma) +" pokemones")
from openpyxl import load_workbook
from openpyxl import Workbook
import difflib
path=os.path.join(os.path.dirname(__file__), 'GrColor.xlsx')
wb =load_workbook(filename=path)
ws = wb.active
ind, ma,dic=modaco(wb,ws)
path=os.path.join(os.path.dirname(__file__), 'Gpohvs.xlsx')
worbe=load_workbook(filename=path)
pagina3=worbe.active
nongh,ma,ngh,pagina3=gpp(pagina3)
ejecutarmenu()
