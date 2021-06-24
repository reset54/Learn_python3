# please enter one integer number
nuuum = int(input())

# prime_numbers recursive
def check_is_prime(number, divided = None):
    if divided is None:
        divided = number - 1
    while divided >= 2:
        if number % divided == 0:
            print(f"Число {number} не простое")
            return False
        else:
            return check_is_prime(number, divided-1)
    else:
        print(f"Число {number} простое")
        return True

# prime_numbers 
def check_is_prime_2(number: int) -> bool:
    """Returns True, if `number` is prime, otherwise returns False"""
    for i in range(2, number):
        counter = 0
        if number % i == 0:
            return(f"Is not a prime number {number} number % divided = {number%i}")
            break
        else:
            return(f'is a prime number     {number} number % divided = {number%i}')



print("\nOption 1")
print(f"Check on prime number = {check_is_prime(nuuum)}")
print("\nOption 2")
print(f"Check on prime number = \n{check_is_prime_2(nuuum)}")

def test (func):
    print(f"\ntest1 {func.__name__}\n{func(2)}")
    print(f"\ntest2 {func.__name__}\n{func(3)}")
    print(f"\ntest3 {func.__name__}\n{func(4)}")
    print(f"\ntest4 {func.__name__}\n{func(5)}")
    print(f"\ntest5 {func.__name__}\n{func(100)}")
    print(f"\ntest6 {func.__name__}\n{func(111)}")


test(check_is_prime_2)