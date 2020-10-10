import getpass # O cusor esconde senha
import os  #  Gerencia coisas do sistama
"""
    Para saber se tem muita responsabilidade em uma mesma função.
        Pergunta o que ela faz
"""
accounts_list = {
    '0001-02':{
        'password': '1234',
        'name': 'John',
        'value': 2000,
        'admin':False
        },
    '0002-02':{
        'password': '1234',
        'name': 'Maria',
        'value': 10,
        'admin':False
        },
    '1111-11':{
        'password': '1234',
        'name': 'Admin',
        'value': 1200,
        'admin':True
        }
}
money_slips = {
    '20':5,
    '50':5,
    '100':5
}
def main():
    header()
    account_auth = auth_account()
    
    if account_auth:

        clear()
        header()
        
        option_typed = get_menu_options_typed(account_auth)
        do_operation(option_typed, account_auth)
    else:
        print('Conta inválida')

def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)
    
    elif option_typed == '2':
        
        withdraw(account_auth)
        
    elif option_typed == '10' and accounts_list[account_auth]['admin']:
            
       insert_money_slips()

def show_balance(account_auth):
     #  %s pq e uma stringer
    print('Seu saldo é %s' % accounts_list[account_auth]['value'])

def insert_money_slips():
    amount_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed= input('Digite a cédula a ser incluída: ')
    money_slips[money_bill_typed] = money_slips[money_bill_typed] + int(amount_typed)
    #money_slips[money_bill_typed] += int(amount_typed)
    print(money_slips)

def withdraw(account_auth):

    value_typed = input('Digite o valor a ser sacado: ')
    money_slips_user = { }
    value_int = int(value_typed)
    desconto = value_int
    if value_int <= accounts_list[account_auth]['value']:
        
        if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
            money_slips_user['100'] = value_int // 100
            value_int = value_int - value_int // 100 * 100
        if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
            money_slips_user['50'] = value_int // 50
            value_int = value_int - value_int // 50 * 50
        if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
            money_slips_user['20'] = value_int // 20
            value_int = value_int - value_int // 20 * 20
        if value_int != 0:
            print("O caixa não tem cédulas disponíveis para este valor")
        else:
            for money_bill in money_slips_user:
                money_slips[money_bill] -= money_slips_user[money_bill]
                
            accounts_list[account_auth]['value'] = accounts_list[account_auth]['value'] - desconto
            print("Pegue as notas: ")
            print(money_slips_user)
    else:
        print("Saldo indisponivel")

def get_menu_options_typed(account_auth):
    print("1 - Saldo")
    print("2 - Saque")
    if accounts_list[account_auth]['admin']:    
        print("10 - Incluir cédulas")
    return input('Escolha uma das opções acima: ')
        
def auth_account():

    account_auth = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua password: ')
    print(account_auth)
    print(password_typed)
    
    if account_auth in accounts_list and password_typed == accounts_list[account_auth]['password']:
        return account_auth
    else:
        return False

def clear():

     os.system('cls'if os.name == 'nt' else 'clear')

def header():

    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")

while True:
    main()

    input('Precione <ENTER> para continuar ..')
    clear()