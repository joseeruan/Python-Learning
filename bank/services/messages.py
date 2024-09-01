def menu() -> str:
    return input('''
    *******************************
    *       Banking System Menu    *
    *******************************
    *                               *
    * 1. Deposit                    *
    * 2. Withdraw                   *
    * 3. Extract                    *
    * 4. Exit                       *
    *                               *
    *******************************
    Choose an option: ''')

def read_deposit() -> float:
    while True:
        try:
            value = float(input('Enter the amount you want to deposit: '))
            if value <= 0:
                print('Invalid value. The amount must be greater than 0.')
            else:
                return value
        except ValueError:
            print('Invalid input. Please enter a valid number.')

def read_withdrawal(balance: float, count: int, limit_count: int, max_withdrawal: float) -> float:
    if count >= limit_count:
        print('Maximum withdrawal limit reached.')
        return 0

    while True:
        try:
            value = float(input('Enter the amount you want to withdraw: '))
            if value > max_withdrawal:
                print('Withdrawal amount exceeds the allowed limit.')
            elif value > balance:
                print('Withdrawal amount exceeds the account balance.')
            elif value <= 0:
                print('Enter an amount greater than 0.')
            else:
                return value
        except ValueError:
            print('Invalid input. Please enter a valid number.')

def read_extract(balance: float, withdrawal_list: list) -> None:
    print(f"\nCurrent balance: R$ {balance:.2f}")
    print("Transaction History:")

    if not withdrawal_list:
        print("No transactions recorded.")
    else:
        for transaction in withdrawal_list:
            for type_, value in transaction.items():
                print(f"Type: {type_.title()}, Amount: R$ {value:.2f}")