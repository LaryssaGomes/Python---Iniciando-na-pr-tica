import os
from main_test import test
print('file',__name__)
from bank_account_variables import money_slips ,accounts_list
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
def open_file_bank(mode):
    return open(BASE_PATH + "/__bank_file.dat", mode)
# qual e a cedula = quantidade delas;qual e a cedula = quantidade delas
def write_money_slips(file):
    for money_bill, value in money_slips.items():
        file.write(money_bill +'='+str(value)+';')

def write_bank_accounts(file):
    for account , account_data in accounts_list.items():
        file.writelines((
            account, ';',
            account_data['name'], ';',
            account_data['password'], ';',
            str(account_data['value']), ';',
            str(account_data['admin']), ';'
            '\n'
        ))
    print('Contas gravadas com sucesso')

def read_money_slips(file):
    line = file.readline()
    while line.find(';') != -1:
        semicolor_pos = line.find(';')
        money_bill_value = line[0:semicolor_pos] 
        set_money_bill_value(money_bill_value)
        if semicolor_pos + 1 == len(line):
            break
        else:
            line = line[semicolor_pos+1:len(line)]

def read_bank_accounts(file):
    lines = file.readlines()
    lines = lines[1:len(lines)]
    for account_line in lines:
        extract_bank_account(account_line)

def extract_bank_account(account_line):
    account_data = []
    while account_line.find(';') != -1:
        semicolor_pos = account_line.find(';')
        data = account_line[0:semicolor_pos] 
        account_data.append(data)
        if semicolor_pos + 1 == len(account_line):
            break
        else:
            account_line = account_line[semicolor_pos+1:len(account_line)]
    add_bank_account(account_data)

def add_bank_account(account_data):
    accounts_list[account_data[0]] = {
        'name': account_data[1],
        'password': account_data[2],
        'value': float(account_data[3]),
        'admin': bool(account_data[4])
    }

def set_money_bill_value(money_bill_value):
    equal_pos = money_bill_value.find('=')
    money_bill = money_bill_value[0:equal_pos]
    cont_money_bill_value = len(money_bill_value)
    value = money_bill_value[equal_pos + 1:cont_money_bill_value]
    print(money_bill, value)
    money_slips[money_bill] = int(value)

def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)
    file.close()
    file = open_file_bank('r')
    read_bank_accounts(file)
    file.close()

def save_money_slips():
    file = open_file_bank('r')
    lines = file.readlines()
    file.close()
    file = open_file_bank('w')
    lines[0] = ""
    for money_bill, value in money_slips.items():
        lines[0] += (money_bill + "=" + str(value)+';')
    lines[0]+='\n'
    file.writelines(lines)
    file.close()