<<<<<<< HEAD
number = int(input("Введите сумму/мес для сдачи квартиры в аренду : ")) 
long_time = int(input("Введите срок (месяцев) аренды : "))
cost_based = int(input("Введите сумму для сравнения : "))

def return_cost_percent(number: int, long_time: int, cost_based: float) -> float:
    result = (long_time * number)/cost_based * 100
    return result

=======
number = int(input("Введите сумму/мес для сдачи квартиры в аренду : ")) 
long_time = int(input("Введите срок (месяцев) аренды : "))
cost_based = int(input("Введите сумму для сравнения : "))

def return_cost_percent(number: int, long_time: int, cost_based: float) -> float:
    result = (long_time * number)/cost_based * 100
    return result

>>>>>>> refs/remotes/origin/readme
print(return_cost_percent(number, long_time, cost_based))