import bank_account_variables
import getpass
import os
from file import save_money_slips
# from bank_account_variables import accounts_list, money_slips outra forma de acessa
def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)
    
    elif option_typed == '2':
        
        withdraw(account_auth)
        
    elif option_typed == '10' and bank_account_variables.accounts_list[account_auth]['admin']:
            
       insert_money_slips()

def show_balance(account_auth):
     #  %s pq e uma stringer
    print('Seu saldo é %s' % bank_account_variables.accounts_list[account_auth]['value'])

def insert_money_slips():
    amount_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed= input('Digite a cédula a ser incluída: ')
    money_slips[money_bill_typed] = bank_account_variables.money_slips[money_bill_typed] + int(amount_typed)
    #money_slips[money_bill_typed] += int(amount_typed)
    print(bank_account_variables.money_slips)

def withdraw(account_auth):

    value_typed = input('Digite o valor a ser sacado: ')
    money_slips_user = { }
    value_int = int(value_typed)
    desconto = value_int
    if value_int <= bank_account_variables.accounts_list[account_auth]['value']:
        
        if value_int // 100 > 0 and value_int // 100 <= bank_account_variables.money_slips['100']:
            money_slips_user['100'] = value_int // 100
            value_int = value_int - value_int // 100 * 100
        if value_int // 50 > 0 and value_int // 50 <= bank_account_variables.money_slips['50']:
            money_slips_user['50'] = value_int // 50
            value_int = value_int - value_int // 50 * 50
        if value_int // 20 > 0 and value_int // 20 <= bank_account_variables.money_slips['20']:
            money_slips_user['20'] = value_int // 20
            value_int = value_int - value_int // 20 * 20
        if value_int != 0:
            print("O caixa não tem cédulas disponíveis para este valor")
        else:
            for money_bill in money_slips_user:
                bank_account_variables.money_slips[money_bill] -= money_slips_user[money_bill]
             
            bank_account_variables.accounts_list[account_auth]['value'] = bank_account_variables.accounts_list[account_auth]['value'] - desconto
            save_money_slips()
            print("Pegue as notas: ")
            print(money_slips_user)
    else:
        print("Saldo indisponivel")

def get_menu_options_typed(account_auth):
    print("1 - Saldo")
    print("2 - Saque")
    if bank_account_variables.accounts_list[account_auth]['admin']:    
        print("10 - Incluir cédulas")
    return input('Escolha uma das opções acima: ')
        
def auth_account():

    account_auth = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua password: ')
    print(account_auth)
    print(password_typed)
    
    if account_auth in bank_account_variables.accounts_list and password_typed == bank_account_variables.accounts_list[account_auth]['password']:
        return account_auth
    else:
        return False
from file import BASE_PATH
def delete_file():
    file = open(BASE_PATH+'/file_to_delete.dat')
    file.close()
    #os.unlink(BASE_PATH+'/file_to_delete.dat')