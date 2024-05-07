#Graficas
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.chart import Barchart, Reference, Series
wb=Workbook()
wb.save('grtip.xlsx')
wb=load_workbook ('grtip.xslx')
p1=wb.create_sheet('Pagina 1')
wb.save('grtip.xslx')
