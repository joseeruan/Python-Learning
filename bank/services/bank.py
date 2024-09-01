from .messages import *
from .config import data_bank


def account() -> None:
    balance = 0.0
    withdrawal_count = 0
    withdrawal_list = []
    option = True

    while option:
        option = menu()

        match option:
            case '1':
                deposit_aux = make_deposit()
                balance += deposit_aux
               
            case '2':
                withdrawal_aux = make_withdrawal(balance, withdrawal_count)
                balance -= withdrawal_aux
                withdrawal_list.append({'withdrawal': withdrawal_aux})
                withdrawal_count += 1
            case '3':
                get_extract(balance, withdrawal_list)
            case '4':
                print('exiting...')
                option = False
            case _:
                print('Option is invalid.')


def make_deposit() -> float:
    value = read_deposit()
    return value


def make_withdrawal(balance: float, withdrawal_count: int) -> float:
    max_withdrawal = data_bank.get('max_withdrawal')
    limit_count = data_bank.get('withdrawal_limit')
    value = read_withdrawal(balance, withdrawal_count, limit_count, max_withdrawal )

    return value

def get_extract(balance: float, withdrawal_list: list) -> None:
    read_extract(balance, withdrawal_list)

