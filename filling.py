import sys
import os
import pandas as pd
import numpy as np 


class Table_fill:
    table_name = 'table.xlsx'
    folder_path = sys.path[0]

    def work(self, table):
        self.ops_table = self.fill(table)
        print(self.ops_table)

    def fill(self, rows):
        table_path = os.path.join(self.folder_path, self.table_name)
        captions = ('Bank Name', 'Card', 'Operation', 'Balance', 'Date', 'Сurrency')
        table = pd.DataFrame(rows, columns=captions)
        table['Date'] = pd.to_datetime(table.Date)
        table = table.sort_values(by='Date')
        table = table.reset_index(drop=True)
        return table

    def total(self, info):
        frames = []
        for i in info:
            for j in info[i]:
                cur_total = self.ops_table.loc[(self.ops_table['Card'] == info[i][j]) & (self.ops_table['Bank Name'] == i)]
                cur_total.tail(1)
                cur_total.loc[:, ['Bank Name', 'Card', 'Balance', 'Сurrency']]
                frames.append(cur_total)
        total = pd.contact(frames)
        print(total.to_string(index=False))

        # def card_month(self, card, date):
