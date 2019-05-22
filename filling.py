import sys
import os
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from xlsxwriter import *


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
    writer = pd.ExcelWriter(table_path, engine='xlsxwriter')
    frames = []
    global full_table
    cur_full = full_table
    fram = [cur_full]
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
    total.loc['Total'] = pd.Series(total['Balance'].sum(), index=['Balance'])
    # print(total)
    total.at['Total', 'Сurrency'] = currency
    total.fillna('', inplace=True)
    fram.append(total)
    # global full_table
    full_table = pd.concat(fram, sort=False)
    full_table = full_table.reset_index(drop=True)
    full_table.index = np.arange(1, len(full_table) + 1)
    last_row = full_table.shape[0]
    full_table.fillna('', inplace=True)
    full_table = full_table.rename({last_row: 'Total'})
    full_table.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    print(total.to_string())


def monthly_total(info):
    writer = pd.ExcelWriter(table_path, engine='xlsxwriter')
    frames = []
    global full_table
    cur_table = full_table
    print(cur_table)
    frames.append(cur_table)
    cur_table['Date'] = pd.to_datetime(cur_table['Date'])
    cur_table['Year'], cur_table['Month'] = cur_table['Date'].dt.year,cur_table['Date'].dt.month
    cur_date = info['Date']
    cur_total = cur_table.loc[(cur_table['Year'] == cur_date.tm_year) & (cur_table['Month'] == cur_date.tm_mon)]
    cur_total = cur_total.loc[:, total_captions]
    cur_total = cur_total.groupby(['Bank Name',
                                   'Card'])['Operation'].agg('sum')
    # cur_total.loc['Total'] = pd.Series(cur_total['Operation'].sum(), index = ['Operation'])
    # if cur_total != [] and cur_total is not None:
    # print(type(cur_total))
    # cur_total = cur_total.reset_index(drop=True)
    if cur_total.shape[0] != 0:
        print(cur_total.to_string())
        while True:
            ans = input('Do u want to write it to xlsx file?(y/n)')
            if ans == 'y':
                # cur_total['Year'] = cur_date.tm_year
                # cur_total['Month'] = cur_date.tm_mon
                # cur_total['Currency'] = 'EUR'
                # full_table['Currency'] = 'EUR'
                frames.append(cur_total)
                full_table['Card'] = full_table.Card.astype(str)
                print(full_table)
                full_table = pd.concat(frames, sort=False, ignore_index=False)
                full_table['Card'] = full_table.Card.astype(str)
                print(full_table)
                full_table.fillna('', inplace=True)
                # full_table['Date'] = full_table['Date'].astype('datetime64[ns]')
                full_table = full_table.loc[:, ['Bank Name', 'Card', 'Operation', 'Month', 'Year', 'Balance', 'Operation']]
                # full_table['Date'] = [''].astype('datetime64[ns]')
                print(full_table.to_string())
                full_table.to_excel(writer, sheet_name='Sheet1')
                writer.save()
                break
            elif ans == 'n':
                break
            else:
                print('Invalid choice')
    else:
        print('U spent nothin in that month')
    #     while True:
    #         ans = input('Do u want to write it to xlsx file?(y/n)\n')
    #         if ans == 'y':
    #             cur_total['Year'] = cur_date.tm_year
    #             cur_total['Month'] = cur_date.tm_mon
    #             # cur_total['Currency'] = 'EUR'
    #             frames.append(cur_total)
    #             # full_table['Card'] = full_table.Card.astype(str)
    #             print(cur_table)
    #             full_table = pd.concat(frames, sort=False, ignore_index=False)
    #             full_table['Card'] = full_table.Card.astype(str)
    #             print(full_table)
    #             # full_table.fillna('', inplace=True)
    #             # full_table['Card'] = full_table.Card.astype(str)
    #             full_table.fillna('', inplace=True)
    #             full_table['Date'] = full_table['Date'].astype('datetime64[ns]')
    #             full_table = full_table.loc[:, ['Bank Name', 'Card', 'Operation', 'Month', 'Year', 'Balance']]
    #             # full_table['Date'] = [''].astype('datetime64[ns]')
    #             # full_table['Currency'] = 'EUR'
    #             full_table.fillna('', inplace=True)
    #             # full_table.insert(full_table.shape[1], 'Currency', 'EUR')
    #             print(full_table)
    #             full_table.to_excel(writer, sheet_name='Sheet1')
    #             writer.save()
    #             break
    #         elif ans == 'n':
    #             break
    #         else:
    #             print('Invalid choice')
    # else:
    #     print('U spent nothin in that month')
    # else:
    #     print("U spent nothing in this month")


def card_monthly(info):
    global full_table
    frames = []
    cur_table = full_table
    cur_table['Date'] = pd.to_datetime(cur_table['Date'])
    cur_table['Year'], cur_table['Month'] = cur_table['Date'].dt.year, cur_table['Date'].dt.month
    cur_date = info['Date']
    cur_card = info['Card']
    cur_bank = info['Bank']
    cur_total = cur_table.loc[(cur_table['Year'] == cur_date.tm_year) &
                              (cur_table['Month'] == cur_date.tm_mon) &
                              (cur_table['Card'] == cur_card) &
                              (cur_table['Bank Name'] == cur_bank)]
    cur_total = cur_total.loc[:, total_captions]
    cur_total = cur_total.groupby(['Bank Name',
                                   'Card'])['Operation'].agg('sum')
    # if cur_total != [] and cur_total is not None:
    if cur_total.shape[0] != 0:
        print(cur_total.to_string())
        while True:
            ans = input('Do u want to write it down to xlsx report?(y/n)\n')
            if ans == 'y':
                print(1)
                break
            elif ans =='n':
                break
            else:
                print('Invalid choice')
    else:
        print("U spent nothing in that month from this card")


table_name = 'table.xlsx'
folder_path = sys.path[0]
currency = 'EUR'
captions = ('Bank Name', 'Card', 'Operation',
            'Balance', 'Date', 'Сurrency')
use_captions = ['Bank Name', 'Card', 'Balance', 'Сurrency']
total_captions = ['Bank Name', 'Card', 'Operation', 'Сurrency']
table_path = os.path.join(folder_path, table_name)
full_table = pd.DataFrame()
