from openpyxl import load_workbook
from openpyxl import Workbook
import matplotlib.pyplot as plt
#Grafica de pastel de colores
wb =load_workbook("GrColor.xlsx")
ws = wb.active
#1r for para manipular las columnas y filas, cree el dic de listas para almacenar listas con nombres de variables
#2do for para manipular el excel y no contar 0s
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
#Sacar la long de c/u
dic=[]
for i in range (0,10):
    d=len(listas['L'+str(i+1)])
    dic.append(d)
#sacar total y porcentajes de c/u
total=sum(dic)
porcentajes=[]
for i in range (10):
    a=dic[i]
    p=(a*100)/1025
    porcentajes.append(p) 
#Para asignar los titulos en una lista
T=[]
for i in range (1,11):
    t=ws.cell(row=1, column=i)
    T.append(t.value)
#Crear gráfica
colores=['beige','blue','brown','grey','green','pink','purple','red','white', 'yellow']
plt.pie(porcentajes, labels=T, autopct="%1.1f%%", startangle=90, colors=colores)
plt.axis("equal")
plt.title("Cantidad de Pokemones de cada color")
wb.save("Grcolor.xlsx")
plt.show()
return
