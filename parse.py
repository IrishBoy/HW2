import os
import sys
from pyparsing import *
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
    'carddet': 'card *',
    'cards_num': [6678, 6623],
    'minus': 'Withdrawal:',
    'plus': 'Transfer:',
    'balance': 'balance: '
}

dict2 = {
    'name': 'GorgeousBank',
    'phone': 720,
    'carddet': '*',
    'cards_num': [1238, 1253],
    'minus': ': -',
    'plus': ': +',
    'balance': 'left: '
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
                cur_card = bank['carddet'] + str(card)
                if cur_card in line:
                    row.append(card)
                    line = line.replace(str(bank['carddet']) + str(card), '', 1)
            if bank['minus'] in line:
                row.append('minus')
                line = line.replace(bank['minus'], '', 1)
            elif bank['plus'] in line:
                row.append('plus')
                line = line.replace(bank['plus'], '', 1)

            print(row)
            print(line)
