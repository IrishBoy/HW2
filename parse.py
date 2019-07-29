import os
import sys
import re
import datetime
from filling import work


class Table:

    table_name = 'table.xlsx'

    message_file = 'mess.txt'

    folder_path = sys.path[0]

    def __init__(self):
        self.banks = []
        self.rows = []

    def addbank(self, bank):
        self.banks.append(bank)

    def work(self):
        cur_rows = self.parse()
        if cur_rows is not None:
            self.rows = cur_rows
            work(cur_rows)

    def parse(self):
        mess_path = os.path.join(self.folder_path, self.message_file)
        mess_text = open(mess_path, 'r')
        result = []
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
                            line = line.replace(str(bank.card_start) +
                                                str(card), '', 1)
                    if bank.minus in line:
                        cur_op = '-'
                        line = line.replace(bank.minus, '', 1)
                    elif bank.plus in line:
                        cur_op = '+'
                        line = line.replace(bank.plus, '', 1)
                    line = line.lstrip()
                    s_start = bank.sum_start
                    s_end = bank.sum_end
                    b_start = bank.balance
                    b_end = bank.b_end
                    searchObj = re.search( r'{}(.*){}{}(.*?){}(.*).*'.format(s_start, s_end, b_start, b_end), line, re.M|re.I)
                    if searchObj:
                        row.append(int(cur_op + searchObj.group(1)))
                        row.append(int(searchObj.group(2)))
                        date_obj = datetime.datetime.strptime(searchObj.group(3), '%Y-%m-%d %H:%M:%S')
                        row.append(date_obj)
                        row.append(bank.currency)
                    else:
                        print("Nothing found!!")
                    result.append(row)
        mess_text.close()
        if result != [] and result is not None:
            return result
