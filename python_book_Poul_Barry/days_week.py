days_week = [
    "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение"
]
print(len(days_week))


def days_week_return(day):
     if day in days_week:
        i=1
        for i in range(i, len(days_week)+1):
            return days_week[i-1]
        # else:
        #     return "Error"
     else:
         return "No such day"

def test_days_week_input_type_correct(type_param):
    try:
        if isinstance(type_param,(str, float)):
            return Exception("input_Type_error, please input correct type                     (int)")
        else:
            return "OK! Type CORRECT!"
    except ValueError:
        print(" ValueError exception!") 
    except TypeError:
        print(" TypeError exception!") 

print(days_week_return(days_week[9]))
print(test_days_week_input_type_correct(days_week[9]))