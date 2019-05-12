import sys
import time


class PersonalManager:
    possible_operations = [
        '1. Show current funds',
        '2. Expences per month',
        '3. Exit from the program'
    ]

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
            ans = input('\nYour choice: ')
            choice = pos.get(int(ans))
            choice()

    def exit(self):
        sys.exit()

    def total(self):
        pass
