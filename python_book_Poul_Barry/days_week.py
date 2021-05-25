import pip3




days_week = [
    "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение"
]
print( len(days_week) )


def returnDaysWeek(day):
     if day in days_week:
        i=1
        for i in range(i, len(days_week)+1):
            return days_week[i-1]
        # else:
        #     return "Error"
     else:
         return "No such day"

print( returnDaysWeek(days_week[9]) )
print( TEST_DaysWeek_input_Type_Correct(days_week[9]) )

def TEST_DaysWeek_input_Type_Correct(type_param):
    try:
        if isinstance(type_param,(str, float)):
            return Exception("input_Type_error, please input correct type (int)")
        else:
            return "OK! Type CORRECT!"
    except: