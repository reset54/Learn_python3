# Example run script from terminal debian or VS Code for 10 january: 
# echo "1 10" | python3._ zodiac.py
# Напиши программу, которая печатает знак зодиака по переданному номеру месяца и дню месяца. 
# number of month (1-31), after " " — month(jan-dec).

try:
    string = input()                
    numbers = string.split(" ")
    number_month = int(numbers[0])
    day_month = int(numbers[1])

    def zodiac_signs(arg1, arg2):
        if (number_month == 1 and 1 <= day_month <= 19) or (number_month == 12 and 31 >= day_month >= 22):
            return('Козерог')    # Козерог	22 декабря — 19 января     22.12-19.01
        elif (number_month == 2 and 1 <= day_month <= 18) or (number_month == 1 and 31 >= day_month >= 20):
            return('Водолей')    # Водолей	20 января — 18 февраля     20.01-18.02
        elif (number_month == 3 and 1 <= day_month <= 20) or (number_month == 2 and 29 >= day_month >= 19):
            return('Рыбы')       # Рыбы	19 февраля — 20 марта          19.02-20.03
        elif (number_month == 4 and 1 <= day_month <= 19) or (number_month == 3 and 31 >= day_month >= 21):
            return('Овен')       # Овен	21 марта — 19 апреля           21.03-19.04
        elif (number_month == 5 and 1 <= day_month <= 20) or (number_month == 4 and 30 >= day_month >= 20):
            return('Телец')      # Телец	20 апреля — 20 мая             20.04-20.05
        elif (number_month == 6 and 1 <= day_month <= 20) or (number_month == 5 and 31 >= day_month >= 21):
            return('Близнецы')   # Близнецы	21 мая — 20 июня           21.05-20.06
        elif (number_month == 7 and 1 <= day_month <= 22) or (number_month == 6 and 30 >= day_month >= 21):
            return('Рак')        # Рак	21 июня — 22 июля              21.06-22.07
        elif (number_month == 8 and 1 <= day_month <= 22) or (number_month == 7 and 31 >= day_month >= 23):
            return('Лев')        # Лев	23 июля — 22 августа           23.07-22.08
        elif (number_month == 9 and 1 <= day_month <= 22) or (number_month == 8 and 31 >= day_month >= 23):
            return('Дева')       # Дева	23 августа — 22 сентября       23.08-22.09
        elif (number_month == 10 and 1 <= day_month <= 22) or (number_month == 9 and 30 >= day_month >= 23):
            return('Весы')       # Весы	23 сентября — 22 октября       23.09-22.10 
        elif (number_month == 11 and 1 <= day_month <= 21) or (number_month == 10 and 31 >= day_month >= 23):
            return('Скорпион')   # Скорпион	23 октября — 21 ноября     23.10-21.11
        elif (number_month == 12 and 1 <= day_month <= 21) or (number_month == 11 and 30 >= day_month >= 22):
            return('Стрелец')   # Стрелец	22 ноября — 21 декабря     22.11-21.12
        else:
            return("некорректная дата")
    # run        
    zodiac_signs(number_month, day_month)

except ValueError:
    print("некорректная дата")
