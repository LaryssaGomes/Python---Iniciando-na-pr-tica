import getpass # O cusor esconde senha
import os  #  Gerencia coisas do sistama
accounts_list = {
    '0001-02':{
        'password': '1234',
        'name': 'John',
        'value': 2200,
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
while True:
    print("****************************************")
    print("*** School of Net - Caixa Eletrônico ***")
    print("****************************************")
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua password: ')
    print(account_typed)
    print(password_typed)
    
    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        os.system('cls'if os.name == 'nt' else 'clear')
    
        print("****************************************")
        print("*** School of Net - Caixa Eletrônico ***")
        print("****************************************")
        print("1 - Saldo")
        print("2 - Saque")
        if accounts_list[account_typed]['admin']:
            
            print("10 - Incluir cédulas")
        option_typed = input('Escolha uma das opções acima: ')
        if option_typed == '1':
            #  %s pq e uma stringer
            print('Seu saldo é %s' % accounts_list[account_typed]['value'])
        elif option_typed == '2':
            
            value_typed = input('Digite o valor a ser sacado: ')
            money_slips_user = { }
            value_int = int(value_typed)
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
                print("Pegue as notas: ")
                print(money_slips_user)
        elif option_typed == '10' and accounts_list[account_typed]['admin']:
            
            amount_typed = input('Digite a quantidade de cédulas: ')
            money_bill_typed= input('Digite a cédula a ser incluída: ')
            money_slips[money_bill_typed] = money_slips[money_bill_typed] + int(amount_typed)
            #money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
    else:
        print('Conta inválida')
    input('Precione <ENTER> para continuar ..')
    os.system('cls'if os.name == 'nt' else 'clear')