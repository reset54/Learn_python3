# 1 принимает на вход целое положительное число и 
# 2 возвращает первое простое число, большее заданного.
# Простое число — это число, которое делится без остатка только на себя и на единицу. Примером могут быть числа 2, 3, 5, 7, 11 и так далее.

num = int(input())

def is_prime_number(number: int) -> bool:
    """Returns True, if `number` is prime, otherwise returns False"""
    if number % number == 0 and number % 1 == 0:
        return (True)
    else:
        return (False)


def get_next_prime_number(number: int) -> int:
    """Returns next primer number after `number`"""
    # alghorithm finding sample numbers
    array = [2]                     # beginning, start number = 2
    n = 10000                       # before number = n
    for i in range(3, n + 1):       # range(start, stop[, step]) -> range object
        k = 0                       # 
        for j in array:
            if i % j == 0:
                k = 1
            if k == 0:
                array.append(i)
    if is_prime_number(number) in array:
        for (number == array[i]):
            return array[i+1] 

print( is_prime_number(num) )
print( get_next_prime_number(num) )