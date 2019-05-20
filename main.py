from banks import Bank
from personal_manager import PersonalManager
from parse import Table


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
                       ' EUR ',
                       'EUR'))

    table.addbank(Bank('GorgeousBank',
                       720,
                       '*',
                       [1238, 1253],
                       '',
                       ' EUR, ',
                       ': -',
                       ': +',
                       'left: ',
                       ' EUR ',
                       'EUR'))

    assistant.add_bank(Bank('SuperBank',
                            480,
                            'card *',
                            [6678, 6623],
                            ': ',
                            ' EUR, ',
                            'Withdrawal:',
                            'Transfer:',
                            'balance: ',
                            ' EUR ',
                            'EUR'))

    assistant.add_bank(Bank('GorgeousBank',
                            720,
                            '*',
                            [1238, 1253],
                            '',
                            ' EUR, ',
                            ': -',
                            ': +',
                            'left: ',
                            ' EUR ',
                            'EUR'))
    table.work()
    assistant.work()


if __name__ == '__main__':
    main()
