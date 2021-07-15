# взято с ресурса:
# https://www.youtube.com/watch?v=IXElBJqJAy4&t=267s&ab_channel=soumilshah1995

class Authentication():

    def __init__(self, user_name=""):
        self.user_name = user_name

    def __lower(self):
        lower = any(char.islower() for char in self.user_name)
        return lower
    
    def __upper(self):
        upper = any(char.isupper() for char in self.user_name)
        return upper

    def __digit(self):
        digit = any(char.isdigit() for char in self.user_name)
        return digit

    def validate(self):
        lower = self.__lower()
        upper = self.__upper()
        digit = self.__digit()
        length = len(self.user_name)
        report = lower and upper and digit and length >= 12

        if report:
            print("User_name passed all checks")
            return True

        elif not lower:
            print("You didn't use Lower case letter")
            return False

        elif not upper:
            print("You didn't use Upper case letter")
            return False

        elif not digit:
            print("You didn't use Digit case letter")
            return False

        elif length < 12:
            print("Username should Atleast have 12 characters")
            return False
        
        else:
            print("all statement isn/'t truth")


if __name__ == "__main__":
    C = Authentication("YoutubeYesterday1991")
    print(C.validate()) 