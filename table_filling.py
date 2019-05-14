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
    #     mess_path = os.path.join(self.folder_path, self.message_file)
    #     mess_text = open(mess_path, 'r')
    #     for line in mess_text:
    #         row = []
    #         for banks in self.banks:
    #             if line.startswith(str(banks.phone)):
    #                 row.append(banks.name)
    #                 print(row)
    #                 for card in banks.cards_num:
    #                     card_parse = Word(nums, exact=len(str(card)))
    #                     grammar = Literal(banks.carddet).suppress() + card_parse
    #                     cur_card = grammar.parseString(line)
    #                     if cur_card == card:
    #                         row.append(cur_card)
    #     print(row)


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
