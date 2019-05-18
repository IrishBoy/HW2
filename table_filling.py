# from openpyxl import load_workbook
import os
import sys
from pyparsing import *


class Table:

    table_name = 'table.xlsx'

    message_file = 'mess.txt'

    folder_path = sys.path[0]

    def __init__(self):
        self.banks = []

    def addbank(self, bank):
        self.banks.append(bank)

    def work(self):
        pass
        mess_path = os.path.join(self.folder_path, self.message_file)
        mess_text = open(mess_path, 'r')
        for line in mess_text:
            row = []
            for bank in self.banks:
                if line.startswith(str(bank.phone)):
                    row.append(bank.name)
                    line = line.replace(str(bank.phone), '', 1)
                    for card in bank.cards_num:
                        cur_card = bank.card_start + str(card)
                        if cur_card in line:
                            row.append(card)
                            line = line.replace(str(bank.card_start) + str(card), '', 1)
                    if bank.minus in line:
                        row.append('minus')
                        line = line.replace(bank.minus, '', 1)
                    elif bank.plus in line:
                        row.append('plus')
                        line = line.replace(bank.plus, '', 1)
                    line = line.lstrip()
                    cur_sum_end = bank.sum_end
                    cur_sum_start = bank.sum_start
                    s_start = bank.sum_start
                    s_end = bank.sum_end
                    b_start = bank.balance
                    b_end = bank.b_end
                    searchObj = re.search( r'{}(.*){}{}(.*?){}(.*).*'.format(s_start, s_end, b_start, b_end), line, re.M|re.I)
                        row.append(searchObj.group(1))
                        row.append(searchObj.group(2))
                        row.append(searchObj.group(3))
                    else:
                        print("Nothing found!!")

                    print(row)



# def caption():
#     table_path = os.path.join(folder_path, table_name)
#     wb = load_workbook(table_path)
#     sheet = wb.active
#     captions = [
#         {
#             1: 'Bank Name',
#             2: 'Card Number',
#             3: 'Operation',
#             4: 'Summ',
#             5: 'Balance'
#         }
#     ]

#     for name in captions:
#         row = []
#         for capt in name:
#             row.append(name[capt])
#         sheet.append(row)

#     wb.save(table_path)

#     def parse():
#         mess_path = os.path.join(folder_path, message_file)
#         mess_text = open(mess_path, 'r')
#         for line in mess_text:
#             row = []
#             for banks in Bank:
#                 if line.startswith(banks.phone):
#                     row.append(banks.name)
#     sheet.append(row)
