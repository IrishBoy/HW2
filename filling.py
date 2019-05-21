import sys
import os
import pandas as pd
import numpy as np


def work(rows):
    ops_table = fill(rows)


def fill(rows):
    table = pd.DataFrame(rows, columns=captions)
    table['Date'] = pd.to_datetime(table.Date)
    table = table.sort_values(by='Date')
    global full_table
    full_table = table.reset_index(drop=True)
    return full_table


def total(info):
    frames = []
    for i in info:
        for j in info[i]:
            cur_bank = i
            cur_card = j
            cur_total = full_table.loc[(full_table['Card'] == cur_card) &
                                       (full_table['Bank Name'] == cur_bank)]
            cur_total = cur_total.tail(1)
            cur_total = cur_total.loc[:, use_captions]
            frames.append(cur_total)
    total = pd.concat(frames)
    total = total.reset_index(drop=True)
    total.index = np.arange(1, len(total) + 1)
    total['Card'] = total['Card'].apply(str)
    # total = total['Card'].apply(str)
    total.loc['Total'] = pd.Series(total['Balance'].sum(), index=['Balance'])
    # print(total)
    total.at['Total', 'Сurrency'] = 'EUR'
    total.at['Total', 'Bank Name'] = ' '
    total.at['Total', 'Card'] = ' '
    print(total.to_string())


def monthly_total(info):
    print(1)
    sys.exit()


def card_monthly(info):
    print(2)
    sys.exit()


table_name = 'table.xlsx'
folder_path = sys.path[0]
captions = ('Bank Name', 'Card', 'Operation',
            'Balance', 'Date', 'Сurrency')
use_captions = ['Bank Name', 'Card', 'Balance', 'Сurrency']
table_path = os.path.join(folder_path, table_name)
        # def card_month(self, card, date):
# class Table_fill:
#     table_name = 'table.xlsx'
#     folder_path = sys.path[0]
#     captions = ('Bank Name', 'Card', 'Operation',
#                 'Balance', 'Date', 'Сurrency')

#     def __init__(self):
#         self.rows = []

#     def work(self, rows):
#         self.rows = rows
#         self.ops_table = self.fill(self.rows)
#         print(self.ops_table)

#     def fill(self, rows):
#         table_path = os.path.join(self.folder_path, self.table_name)
#         table = pd.DataFrame(rows, columns=self.captions)
#         table['Date'] = pd.to_datetime(table.Date)
#         table = table.sort_values(by='Date')
#         table = table.reset_index(drop=True)
#         return table

#     def total(self, info):
#         print(self.rows)
#         print(0)
#         print(self.ops_table)
#         frames = []
#         print(info)
#         for i in info:
#             for j in info[i]:
#                 print(1)
#                 print(i, j)
#                 print(self.ops_table)
#                 cur_bank = i
#                 cur_card = j
#                 cur_total = self.ops_table.loc[(self.ops_table['Card'] == cur_card) & (self.ops_table['Bank Name'] == cur_bank)]
#                 print(2)
#                 cur_total.tail(1)
#                 cur_total.loc[:, ['Bank Name', 'Card', 'Balance', 'Сurrency']]
#                 frames.append(cur_total)
#                 print(3)
#         total = pd.contact(frames)
#         print(4)
#         print(total.to_string(index=False))
#         print(5)
