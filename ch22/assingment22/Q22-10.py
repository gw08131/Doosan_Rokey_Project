# Q22-10.py

from openpyxl import Workbook, load_workbook


path = "C:/rokey/python/ch22/assingment22/data.xlsx"

wb = load_workbook(path)
sheet = wb.active
sheet['A1'] = 'Hello'
sheet['B1'] = 'My'
sheet['C1'] = 'name'
sheet['D1'] = 'is'
sheet['E1'] = 'Jiyun'
wb.save(path)