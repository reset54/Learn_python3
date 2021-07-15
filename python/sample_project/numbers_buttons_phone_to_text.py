# взято с https://stepik.org/lesson/520943/step/7?unit=513462
from typing import Optional


str = "5555 6 4 222 33 666 11 0 4444 999 22 4 5 2 9999 1111"

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

