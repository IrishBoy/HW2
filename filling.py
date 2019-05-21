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
    full_table = pd.concat(fram, sort=False)
    full_table = full_table.reset_index(drop=True)
    full_table.index = np.arange(1, len(full_table) + 1)
    full_table.fillna('', inplace=True)
    # print(full_table.to_string())
    print(total.to_string())


def monthly_total(info):
    cur_table = full_table
    cur_table['Date'] = pd.to_datetime(cur_table['Date'])
    cur_table['Year'], cur_table['Month'] = cur_table['Date'].dt.year,cur_table['Date'].dt.month
    cur_date = info['Date']
    print(cur_date.tm_year, cur_date.tm_mon)
    cur_total = cur_table.loc[(cur_table['Year'] == cur_date.tm_year) & (cur_table['Month'] == cur_date.tm_mon)]
    print(cur_total)
    cur_total = cur_total.loc[:, total_captions]
    print(cur_total)
    cur_total = cur_total.groupby(['Bank Name',
                                   'Card'])['Operation'].agg('sum')
    print(cur_total.to_string())


def card_monthly(info):
    cur_table = full_table
    pd.to_datetime(cur_table['Date'])
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
    print(cur_total.to_string())


table_name = 'table.xlsx'
folder_path = sys.path[0]
currency = 'EUR'
captions = ('Bank Name', 'Card', 'Operation',
            'Balance', 'Date', 'Сurrency')
use_captions = ['Bank Name', 'Card', 'Balance', 'Сurrency']
total_captions = ['Bank Name', 'Card', 'Operation', 'Сurrency']
table_path = os.path.join(folder_path, table_name)
