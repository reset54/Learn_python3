import re
import unittest


def is_password_hard(password: str) -> bool:
    """This function return True, if `password` hard, otherwise return False!"""
    if len(password) < 12:
        # print(password)
        # print(len(password))
        # print("Длина пароля слишком мала")
        return False
    else: 
        down_register_pattern = re.search('[a-z]', password) 
        #print(down_register_pattern)
        up_register_pattern = re.search('[A-Z]', password)
        #print(up_register_pattern)
        is_digit_pattern = re.search('[\d]', password)
        #print(is_digit_pattern)
        if down_register_pattern and up_register_pattern and is_digit_pattern:
            return True
        else:
            return False  


def test_is_password_hard(func, arg_1, arg_2, arg_3):
    print(f"Тест 1: {func(arg_1)}")
    print(f"Тест 2: {func(arg_2)}")
    print(f"Тест 3: {func(arg_3)}")

test_is_password_hard(is_password_hard, "YouTube1999noName","YOUTUBE1993NONAME", "youtube1991noname")   


class Test_is_password_hard(unittest.TestCase):
    def test_is_password_hard(self):
       self.assertEqual(is_password_hard("YouTube1991noName"), True)
       self.assertEqual(is_password_hard("dsmkhfshdfjahsfjkh"), False)
       self.assertEqual(is_password_hard("1dskfj oaid1"), False)
       self.assertEqual(is_password_hard("1Dskfjoaid11"), True)


if __name__ == '__main__':
    unittest.main()

