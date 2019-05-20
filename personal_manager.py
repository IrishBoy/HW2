import sys
import time
import os
import sys
from parse import Table
from filling import total, monthly_total, card_monthly


class PersonalManager:
    possible_operations = [
        '1. Show current funds',
        '2. Expences per month',
        '3. Exit from the program'
    ]
    table = Table()
    table.work()

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
        infos = {}
        for bank in self.banks:
            infos[bank.name] = infos.get(bank.name, bank.cards_num)
        total(infos)

    def monthly(self):
        while True:

            print('\nEnter month and year in the following format MM-YYYY:')
            us_date = input('\nYour choice: ')

            try:
                valid_date = time.strptime(us_date, '%m-%Y')
                print('\nSelect a credit card: ')
                pos, date = self.card_monthly(valid_date)
                ans = input('\nYour choice: ')
                while True:
                    try:
                        ans = int(ans)
                        if int(ans) == len(pos):
                            pos[int(ans)]()
                        elif int(ans) in pos:
                            pos[int(ans)]([pos[int(ans)], date])
                    except ValueError:
                        print('Invalid choice')
            except ValueError:
                print('Invalid date!')

    def card_monthly(self, date):
        pos = {}
        position = 1
        for bank in self.banks:
            for card in bank.cards_num:
                pos[position] = pos.get(position, card_monthly)
                print(f'{position}. {card}, {bank.name}')
                position += 1
        print(f'\n{position}. Total')
        # pos[position + 1] = pos.get(position, 'Total')
        print(f'\n{position + 1}. Exit to main menu')
        pos[position] = pos.get(position, monthly_total)
        pos[position + 1] = pos.get(position + 1, self.work)
        return (pos, date)

    def exit(self):
        sys.exit()

    def total(self):
        pass


    # def parse(self):
    #     mess_path = os.path.join(self.folder_path, self.message_file)
    #     mess_text = open(mess_path, 'r')
    #     for line in mess_text:
    #         row = []
    #         for bank in self.bank:
    #             if line.startswith(bank.phone):
    #                 row.append(bank.name)
