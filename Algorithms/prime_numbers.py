import unittest


num = int(input()) # -> int

def is_prime_number(number: int) -> bool:
    """Returns True, if `number` is prime, otherwise returns False
    Функция is_prime_number - 
    проверка переданного числа на простоту
    """
    check = 0
    if number == 1 or number == 2:
        check = True
        return check
    
    for i in range(2, number+1):
        if number % i == 0:
            print(i, number % i)
            return(False) 
            break
        else:
            print(i, number % i)
            check = "True"
    return check

def get_next_prime_number(number: int) -> int:
    """Returns next primer number after `number`
    get_next_prime_number - вернёт следующее простое число, большее, чем введённое 
    (независимо простое оно или нет)
    """
    check = (is_prime_number(number))
    number += 1
    while(True):
        if(check == False):
            print(number)
            number += 1    
        else:
            # number += 1 
            print("end cycle")
            break
    print(number)




#class Test_is_prime_number(unittest.TestCase):
    
#   def test_is_prime_number(self): 
#        self.assertEqual(is_prime_number(30), False)
#        self.assertEqual(is_prime_number(77), False)
#        self.assertEqual(is_prime_number(7), True)

#    def test_get_next_prime_number(self):
        #self.assertEqual(get_next_prime_number(30), 31)
        #self.assertEqual(get_next_prime_number(77), 79)
        #self.assertEqual(get_next_prime_number(7), 11)
        #self.assertEqual(get_next_prime_number(11), 13)
        #self.assertEqual(get_next_prime_number(115), 127)
        #self.assertEqual(get_next_prime_number(1975), 1979)
#        pass

#if __name__ == '__main__':
#    unittest.main()




print(f"\nCheck on prime number = {is_prime_number(num)}")

print(f"\nNext prime number = {get_next_prime_number(num)}")