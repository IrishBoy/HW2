from openpyxl import load_workbook
import os
import sys


file_path = os.path.join(sys.path[0], 'table.xlsx')
wb = load_workbook(file_path)
sheet = wb.active


captions = [
    {
        1: 'Bank Name',
        2: 'Card Number',
        3: 'Operation',
        4: 'Summ',
        5: 'Balance'
    }
]


for name in captions:
    row = []
    for capt in name:
        row.append(name[capt])
    sheet.append(row)


wb.save(file_path)
