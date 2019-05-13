import sys
import time
from openpyxl import load_workbook
import os
import sys


class PersonalManager:
    possible_operations = [
        '1. Show current funds',
        '2. Expences per month',
        '3. Exit from the program'
    ]

    table_name = 'table.xlsx'

    message_file = 'mess.txt'

    folder_path = sys.path[0]

    def __init__(self):
        self.banks = []

    def add_bank(self, bank):
        self.banks.append(bank)

    def work(self):
        while True:
            print('\nPossible operations:')
            for operation in self.possible_operations:
                print(operation)
            self.execute(input('\nYour choice: '))

    def execute(self, number):
        operations = {
            1: self.current_funds,
            2: self.monthly,
            3: self.exit
        }
        choice = operations.get(int(number))
        choice()

    def current_funds(self):
        pass

    def monthly(self):
        while True:

            print('\nEnter month and year in the following format MM-YYYY:')
            us_date = input('\nYour choice: ')

            try:
                valid_date = time.strptime(us_date, '%m-%Y')
            except ValueError:
                print('Invalid date!')

            print('\nSelect a credit card: ')
            pos, date = self.card_monthly(valid_date)
            ans = input('\nYour choice: ')
            choice = pos.get(int(ans))
            choice()

    def card_monthly(self, date):
        pos = {}
        position = 1
        for bank in self.banks:
            for card in bank.cards_num:
                pos[position] = pos.get(position, [bank.name, card])
                print(f'{position}. {card}, {bank.name}')
                position += 1
        print(f'\n{position + 1}. Total')
        print(f'\n{position + 2}. Exit to main menu')
        pos[position + 1] = pos.get(position + 1, self.total)
        pos[position + 2] = pos.get(position + 2, self.work)
        return (pos, date)

    def exit(self):
        sys.exit()

    def total(self):
        pass

    def caption(self):
        table_path = os.path.join(self.folder_path, self.table_name)
        wb = load_workbook(table_path)
        sheet = wb.active
        captions = [
            {
                1: 'Bank Name',
                2: 'Card Number',
                3: 'Operation',
                4: 'Summ',
                5: 'Balance'
            }
        ]

        for name in captions:
            row = []
            for capt in name:
                row.append(name[capt])
            sheet.append(row)

        wb.save(table_path)

    # def parse(self):
    #     mess_path = os.path.join(self.folder_path, self.message_file)
    #     mess_text = open(mess_path, 'r')
    #     for line in mess_text:
    #         row = []
    #         for bank in self.bank:
    #             if line.startswith(bank.phone):
    #                 row.append(bank.name)


# class Table:

#     table_name = 'table.xlsx'

#     message_file = 'mess.txt'

#     folder_path = sys.path[0]

#     def __init__(self):
#         self.banks = []

#     def add_bank(self, bank):
#         self.banks.append(bank)

#     def fill(self):
#         while True:
#             for bank in self.banks:
#                 print(bank.phone)
