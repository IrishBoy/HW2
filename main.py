from banks import Bank
from personal_manager import PersonalManager
from table_filling import Table


def main():
    assiatant = PersonalManager()
    table = Table()
    table.add_bank(Bank('SuperBank',
                            480,
                            'card *',
                            [6678, 6623],
                            'Withdrawal:',
                            'Transfer:',
                            'balance: '))

    table.add_bank(Bank('GorgeousBank',
                            720,
                            '*',
                            [1238, 1253],
                            ': -',
                            ': +',
                            'left: '))
    assiatant.add_bank(Bank('SuperBank',
                            480,
                            'card *',
                            [6678, 6623],
                            'Withdrawal:',
                            'Transfer:',
                            'balance: '))

    assiatant.add_bank(Bank('GorgeousBank',
                            720,
                            '*',
                            [1238, 1253],
                            ': -',
                            ': +',
                            'left: '))
    table.fill()

    # assiatant.work()


if __name__ == '__main__':
    main()
