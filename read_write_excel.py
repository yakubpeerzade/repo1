import xlrd
import xlwt
from xlwt import Workbook
file="D:/hexl/tp.xlsx"
workbook=xlrd.open_workbook(file)
sheet=workbook.sheet_by_index(0)

#Below code is to iterate loop from row by column row 1 to all column data
for col in range (sheet.ncols):
    print(sheet.cell_value(1,col))

#Below code is to read code from row and column and store it in list

data=[[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
print(data)

sheet1=workbook.add_sheet('sheet3')

sheet1.write(0,0,'Column1')


