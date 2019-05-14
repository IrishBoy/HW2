import os
import sys
from pyparsing import *
from personal_manager import PersonalManager
from banks import Bank


banks = PersonalManager.banks
print(banks)
# bks = self.banks
# for name in bks:
#     print(banks.name)
table_name = 'table.xlsx'

message_file = 'mess.txt'

folder_path = sys.path[0]
mess_path = os.path.join(folder_path, message_file)
mess_text = open(mess_path, 'r')
# for line in mess_text:
#         row = []
#         for banks in banks:
#             if line.startswith(str(banks.phone)):
#                 row.append(banks.name)
#                 print(row)
#                 for card in banks.cards_num:
#                     card_parse = Word(nums, exact=len(str(card)))
#                     grammar = Literal(banks.carddet).suppress() + card_parse
#                     cur_card = grammar.parseString(line)
#                     print(cur_card)
#                     if cur_card == card:
#                         row.append(cur_card)
# print(row)
