num = int(input())

print("\nФункция \nis_prime_number - \n    проверка переданного числа на простоту;\nget_next_prime_number - \n    вернёт следующее простое число, большее, чем введённое \n    (независимо простое оно или нет)")

def is_prime_number(number: int) -> bool:
    """Returns True, if `number` is prime, otherwise returns False"""
    check = 0
    for i in range(2, number+1):
        
        if number % i == 0:
            #print(i, number % i)
            return(False)
            break
        else:
            #print(i, number % i)
            check = "True"
    return check

def get_next_prime_number(number: int) -> int:
    """Returns next primer number after `number`"""
    check = (is_prime_number(number))
    number += 1
    while(True):
        if(check == False):
            # print(number)
            number += 1    
        else:
            # number += 1 
            print("end cycle")
            break
    print(number)


print(f"\nCheck on prime number = {is_prime_number(num)}")

print(f"\nNext prime number = {get_next_prime_number(num)}")