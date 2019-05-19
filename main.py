from banks import Bank
from personal_manager import PersonalManager
from table_filling import Table


def main():
    assistant = PersonalManager()
    table = Table()

    table.addbank(Bank('SuperBank',
                       480,
                       'card *',
                       [6678, 6623],
                       ': ',
                       ' EUR, ',
                       'Withdrawal:',
                       'Transfer:',
                       'balance: ',
                       ' EUR '))

    table.addbank(Bank('GorgeousBank',
                       720,
                       '*',
                       [1238, 1253],
                       '',
                       ' EUR, ',
                       ': -',
                       ': +',
                       'left: ',
                       ' EUR '))

    assistant.add_bank(Bank('SuperBank',
                            480,
                            'card *',
                            [6678, 6623],
                            ': ',
                            ' EUR, ',
                            'Withdrawal:',
                            'Transfer:',
                            'balance: ',
                            ' EUR '))

    assistant.add_bank(Bank('GorgeousBank',
                            720,
                            '*',
                            [1238, 1253],
                            '',
                            ' EUR, ',
                            ': -',
                            ': +',
                            'left: ',
                            ' EUR '))
    table.work()
    assistant.work()


if __name__ == '__main__':
    main()
