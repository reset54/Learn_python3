# please enter one integer number
nuuum = int(input())

# prime_numbers recursive
def check_is_prime(number, divided = None):
    if divided is None:
        divided = number - 1
    while divided >= 2:
        if number % divided == 0:
            print("Число не простое")
            return False
        else:
            return check_is_prime(number, divided-1)
    else:
        print("Число простое")
        return True

# prime_numbers 
def check_is_prime_2(number: int) -> bool:
    """Returns True, if `number` is prime, otherwise returns False"""
    for i in range(2, number):
        counter = 0
        if number % i == 0:
            print('Is not a prime number', number , "number % divided = " + str(number%i))
            break
        else:
            print(f'is a prime number     {number} number % divided = {number%i}')


check_is_prime_2(nuuum)
print()
print(check_is_prime(nuuum))