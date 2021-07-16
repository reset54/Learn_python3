# взято с https://stepik.org/lesson/520943/step/7?unit=513462
from typing import Optional


def test(func, arg1, arg2, arg3, arg4):
    print( func(arg1) )
    print( func(arg2) )
    print( func(arg3) )
    print( func(arg4) )


def numbers_buttons_phone_to_text(numbers: str) -> Optional[str]:
    """
    mobile phone buttons for text message on Russian language (T9)
    |  1  |  2  |  3  |
    |  4  |  5  |  6  |
    |  7  |  8  |  9  |
          |  0  |
    one button contains many symbols
    registr - only lower!
    b1 = button_1
    """     
    b1 = [".", ",", "?", "!", ":", ";"]
    b2 = ["а", "б", "в", "г"]
    b3 = ["д", "е", "ж", "з"]
    b4 = ["и", "й", "к", "л"]
    b5 = ["м", "н", "о", "п"]
    b6 = ["р", "с", "т", "у"]
    b7 = ["ф", "х", "ц", "ч"]
    b8 = ["ш", "щ", "ъ", "ы"]
    b9 = ["ь", "э", "ю", "я"]
    b0 = [" "]

    result = str()
    new_list = numbers.split(" ")

    for item in new_list:
        # print(set(item))
        count = -1                      # to compare with button[index]
        if len(set(item)) == 1:         # если все символы одинаковы, то пересчитываем сколько их, если нет, то return None
            try:
                for i in item:
                    count += 1
                # print(f" for item {i} = index {count}") # -> test
                if set(item) == {"1"}:
                    result += b1[count] # количество символов - 1 = index по button
                elif set(item) == {"2"}:
                    result += b2[count]
                elif set(item) == {"3"}:
                    result += b3[count]
                elif set(item) == {"4"}:
                    result += b4[count]
                elif set(item) == {"5"}:
                    result += b5[count]
                elif set(item) == {"6"}:
                    result += b6[count]
                elif set(item) == {"7"}:
                    result += b7[count]
                elif set(item) == {"8"}:
                    result += b8[count]
                elif set(item) == {"9"}:
                    result += b9[count]
                elif set(item) == {"0"}:
                    result += b0[count]
                else:
                    result = None
                    return(result)
            except IndexError:
                result = None
                return(result)
        else:
            result = None
            return(result)

    return(result)

# Run test
print("\nOption 1:")
test(numbers_buttons_phone_to_text, "2222 2 222", "2232 2 222", "5555 4 55 333 2222 44", "5555 6 4 222 33 666 11 0 4444 999 22 4 5 2 9999 1111")



#_________________________________Option_2______________________________________
keyboard = {
	'1': ['.', ',', '?', '!', ':', ';', ],
	'2': ['а', 'б', 'в', 'г', ],
	'3': ['д', 'е', 'ж', 'з', ],
	'4': ['и', 'й', 'к', 'л', ],
	'5': ['м', 'н', 'о', 'п', ],
	'6': ['р', 'с', 'т', 'у', ],
	'7': ['ф', 'х', 'ц', 'ч', ],
	'8': ['ш', 'щ', 'ъ', 'ы', ],
	'9': ['ь', 'э', 'ю', 'я', ],
	'0': [' '],
}

def numbers_buttons_phone_to_text_2(numbers: str) -> Optional[str]:
    numbers_layout = numbers.split()
    text = str()
    for value in numbers_layout:
        if len(value) > 4:
            return None
        if value != (value[0] * len(value)):
            return None
        text = text + keyboard[value[0]][len(value) - 1]
    return text

# Run
print("\nOption 2:")
test(numbers_buttons_phone_to_text_2, "2222 2 222", "2232 2 222", "5555 4 55 333 2222 44", "5555 6 4 222 33 666 11 0 4444 999 22 4 5 2 9999 1111")