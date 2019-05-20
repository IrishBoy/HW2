import os
import sys
from pyparsing import *
import re
# from personal_manager import PersonalManager
# from banks import Bank


# banks = PersonalManager.banks
# print(banks)
# bks = self.banks
# for name in bks:
#     print(banks.name)

dict1 = {
    'name': 'SuperBank',
    'phone': 480,
    'card_start': 'card *',
    'cards_num': [6678, 6623],
    'sum_start': ': ',
    'sum_end': ' EUR, ',
    'minus': 'Withdrawal:',
    'plus': 'Transfer:',
    'balance': 'balance: ',
    'b_end': ' EUR '
}

dict2 = {
    'name': 'GorgeousBank',
    'phone': 720,
    'card_start': '*',
    'cards_num': [1238, 1253],
    'sum_start': '',
    'sum_end': ' EUR, ',
    'minus': ': -',
    'plus': ': +',
    'balance': 'left: ',
    'b_end': ' EUR '
}

table_name = 'table.xlsx'

message_file = 'mess.txt'
banks = [dict1, dict2]
folder_path = sys.path[0]
mess_path = os.path.join(folder_path, message_file)
mess_text = open(mess_path, 'r')

for line in mess_text:
    row = []
    for bank in banks:
        if line.startswith(str(bank['phone'])):
            row.append(bank['name'])
            line = line.replace(str(bank['phone']), '', 1)
            for card in bank['cards_num']:
                cur_card = bank['card_start'] + str(card)
                if cur_card in line:
                    row.append(card)
                    line = line.replace(str(bank['card_start']) + str(card), '', 1)
            if bank['minus'] in line:
                row.append('minus')
                line = line.replace(bank['minus'], '', 1)
            elif bank['plus'] in line:
                row.append('plus')
                line = line.replace(bank['plus'], '', 1)
            line = line.lstrip()
            cur_sum_end = bank['sum_end']
            cur_sum_start = bank['sum_start']
            s_start = bank['sum_start']
            s_end = bank['sum_end']
            b_start = bank['balance']
            b_end = bank['b_end']
            searchObj = re.search( r'{}(.*){}{}(.*?){}(.*).*'.format(s_start, s_end, b_start, b_end), line, re.M|re.I)
                row.append(searchObj.group(1))
                row.append(searchObj.group(2))
                row.append(searchObj.group(3))
            else:
                print("Nothing found!!")

            print(row)
# line = ": 10 EUR, balance: 578 EUR 2018-12-2 14:56:44";
# s_start = ': '
# s_end = ' EUR,'
# b_start = ' balance: '
# b_end = ' EUR'
# searchObj = re.search( r'{}(.*){}{}(.*?){}(.*).*'.format(s_start, s_end, b_start, b_end), line, re.M|re.I)

# if searchObj:
#    print "searchObj.group() :", searchObj.group()
#    print "searchObj.group(1) :", searchObj.group(1)
#    print "searchObj.group(2) :", searchObj.group(2)
#    print "searchObj.group(2) :", searchObj.group(3)