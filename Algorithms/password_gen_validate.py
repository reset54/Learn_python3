import random
import re


def generate_password(length: int) -> str:
    pswd, add_pswd = '', ''
    # 'lI1oO0' - символы, которые можно легко перепутать не входят в генерируемые последовательности
    res = set('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ') - set('lI1oO0') 
    while len(pswd) != length:                  # generate
        add_pswd = random.choice(list(res))
        pswd = pswd + add_pswd
    if check_password(pswd):                    # check
        return pswd
    else:
        return generate_password(length)


def generate_passwords(amount_pswds: int, len_pswd: int) -> list:
    lst = []
    for i in range(amount_pswds):
        lst.append(generate_password(len_pswd))
    return lst


def check_password(s: str) -> bool:      
    '''check password on exist: 1 upper sym, 1 lower sym, 1 digit sym'''
    lowers = re.findall('[a-z]', s)
    uppers = re.findall('[A-Z]', s)
    digits = re.findall('[0-9]', s)
    if lowers == [] or uppers == [] or digits == []:
        return False
    else:
        return True

    
# n - количество паролей 
# m - длина паролей (кол-во символов)
n, m = int(input()), int(input())
[print(i) for i in generate_passwords(n, m)]