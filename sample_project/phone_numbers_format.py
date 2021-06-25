# программа принимает на вход телефон и форматирует его, выводя в необходимом виде.
# Формат телефона на выходе: 8 (9xx) xxx-xx-xx
# Форматы телефонов на входе:
# 89xxxxxxxxx
# 9xxxxxxxxx — пропущена первая 7 или 8, в выходном формате первая 9 меняется на 8 (9
# 79xxxxxxxxx — в выходном формате первые символы 79 меняются на 8 (9
# +79xxxxxxxxx — в выходном формате первые символы +79 меняются на 8 (9 
# Если номер телефона не подходит по формату, программа должна вывести на печать 
# исходный телефон, только цифры.
import re 

phone_number_input = input()
a = phone_number_input.strip(" ")
a = a.strip(" -()")
print(a)

result = re.match(, phone_number_input)
print(result)

class Phone_number():
    def __init__(self, phone):
        pass
    #def check


pn_1 = Phone_number(input)
