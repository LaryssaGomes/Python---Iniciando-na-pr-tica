import utils
import operations
from bank_account_variables import money_slips, accounts_list
from file import load_bank_data
"""
    Para saber se tem muita responsabilidade em uma mesma função.
        Pergunta o que ela faz
"""

def main():
    load_bank_data()

    print(money_slips)
    print(accounts_list)
    utils.header()
    account_auth = operations.auth_account()
    
    if account_auth:

        utils.clear()
        utils.header()
        
        option_typed = operations.get_menu_options_typed(account_auth)
        operations.do_operation(option_typed, account_auth)
    else:
        print('Conta inválida')


if __name__ == '__main__':
    while True:
        main()

        input('Precione <ENTER> para continuar ..')
        utils.clear()
