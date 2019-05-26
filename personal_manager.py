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
            operations = {
                1: self.current_funds,
                2: self.monthly,
                3: self.exit
            }
            print('\nPossible operations:')
            for operation in self.possible_operations:
                print(operation)
            print('''\nIf u want program to work properly,
                     to begin with choose 1st op. ''')
            ans = input('\nYour choice: ')
            if ans.isdigit() and int(ans) in operations:
                operations[int(ans)]()
            else:
                print('Invalid choice')

    def current_funds(self):
        infos = {}
        for bank in self.banks:
            infos[bank.name] = infos.get(bank.name, bank.cards_num)
        total(infos)

    def monthly(self):
        while True:
            print("\nEnter month and year in the following format MM-YYYY or '0' to exit:")
            us_date = input('\nYour choice: ')
            if us_date == '0':
                self.work()
            else:
                try:
                    valid_date = time.strptime(us_date, '%m-%Y')
                    while True:
                        print('\nSelect a credit card: ')
                        pos, ch_date, info = self.card_monthly(valid_date)
                        ans = input('\nYour choice: ')
                        if ans.isdigit() and int(ans) == len(pos):
                            pos[int(ans)]()
                        elif ans.isdigit() and int(ans) in pos:
                            pos[int(ans)](info[int(ans)])
                        else:
                            print('Invalid choice')
                except ValueError:
                    print('Invalid date!')

    def card_monthly(self, date):
        pos = {}
        que = {}
        position = 1
        for bank in self.banks:
            for card in bank.cards_num:
                info = {}
                pos[position] = pos.get(position, card_monthly)
                info['Bank'] = info.get('Bank', bank.name)
                info['Card'] = info.get('Card', card)
                info['Date'] = info.get('Date', date)
                que[position] = que.get(position, info)
                print(f'{position}. {card}, {bank.name}')
                position += 1
        print(f'\n{position}. Total')
        que[position] = que.get(position, {'Date':date})
        # pos[position + 1] = pos.get(position, 'Total')
        print(f'\n{position + 1}. Exit to main menu')
        pos[position] = pos.get(position, monthly_total)
        pos[position + 1] = pos.get(position + 1, self.work)
        return (pos, date, que)

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