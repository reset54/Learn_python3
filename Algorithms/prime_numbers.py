num = int(input())

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
            #print(number)
            number += 1    
        else:
            number += 1 
            print("end cycle")
            break
    print(number)

print(is_prime_number(num))
print()
get_next_prime_number(num)