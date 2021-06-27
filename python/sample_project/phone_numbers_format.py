import re 


pn = input()
# https://coderoad.ru/1450897/%D0%A3%D0%B4%D0%B0%D0%BB%D0%B8%D1%82%D1%8C-%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8B-%D0%BA%D1%80%D0%BE%D0%BC%D0%B5-%D1%86%D0%B8%D1%84%D1%80-%D0%B8%D0%B7-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D1%8C%D1%8E-Python

def phone_numbers_formatter(pn):
    """Format your string on (XXX) XXX XX XX or return only numbers, if your phone not consist 11, 10 digits"""
    pattern = r'\D'
    # ignore all symbols other than numbers (sustitute empty str '')
    pn = re.sub(pattern, '', pn)
    count = 0
    for digit in pn:
        count += 1
    if count ==  11 or count == 10 and pn[-10] == "9":
        return(f'8 ({pn[-10:-7]}) {pn[-7:-4]}-{pn[-4:-2]}-{pn[-2:-1]}{pn[-1]}')
    else:
        try:
            return(f'{pn[:-1]}{pn[-1]}')
        except IndexError:
            print("IndexError, please input correct number")


def testingcode(phone):
    phone_number = ''.join([x for x in phone if x.isdigit()])
    print(f"phone_number = {phone_number}")
    phone_number_2 = ''.join(filter(str.isdigit, phone))
    print(f"phone_number_2 = {phone_number_2}")
    phone_number_3 = "".join(list(filter(lambda i: re.match(r"\d", i), list(phone))))
    phone_number_3 = re.sub(r"^(7|8)*(9\d\d)(\d\d\d)(\d\d)(\d\d)$", r"8 (\2) \3-\4-\5", phone_number_3) # format
    print(f"phone_number_3 = {phone_number_3}")
    

def test_phone_numbers_formatter(func, pn):
    print("start tests:")
    print(f"Test input: {func(pn)}")
    print(f"Test 1: {func('8 912 345 67 89')}")
    print(f"Test 2: {func('8 (912)345-6789')}")
    print(f"Test 3: {func('912)345-6789')}")
    print(f"Test 4: {func('7912345 67-89')}")
    print(f"Test 5: {func('+79123456789')}")
    print(f"Test 6: {func('+7 912-(34)-5-6-7-89')}")
    print(f"Test 7: {func('3 45 678 90-98-76-54-32')}")
    print(f"Test 8: {func('(123) 456 78 91')}")
    print(f"Test 9: {func('(343) 33 33')}")

# run functions:
#test_phone_numbers_formatter(phone_numbers_formatter, pn)
test_phone_numbers_formatter(testingcode, pn)