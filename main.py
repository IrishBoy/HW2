from banks import Bank
from personal_manager import PersonalManager


def main():
    assiatant = PersonalManager()

    assiatant.add_bank(Bank('SuperBank',
                            480,
                            [6678, 6623],
                            'Withdrawal',
                            'Transfer',
                            'balance:'))

    assiatant.add_bank(Bank('GorgeousBank',
                            720,
                            [1238, 1253],
                            '-',
                            '+',
                            'left:'))
    assiatant.work()


if __name__ == '__main__':
    main()
