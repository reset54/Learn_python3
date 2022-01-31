#-----------------------------------------------

a = int( input("введите необходимое число: ") )
name = input("Введите имя: ")

def cuadratic_num():
    x = a*a
    return x

def say(name, surname):
    print("Hello! ", name, surname)


#-----------------------------------------------


def decor_1(func):
    def wrapper():
        print()
        func()
        print("<\______/>")
    return wrapper


#-----------------------------------------------


def a_decorator_take_any_arguments(function_to_decorate):
    # this "wrapper" takes any arguments
    def wrapper_take_any_arguments(*args, **kwargs):
        print("Передали ли мне что-нибудь?:")
        print(f"args = {args}")
        print(f"kwargs = {kwargs}")
        function_to_decorate(*args, **kwargs)
    return wrapper_take_any_arguments

a_decorator_take_any_arguments


#-----------------------------------------------


def decorator(func):
    def wrapper(*args, **kwargs):
        print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        print("...start decorator...")
        func(*args, **kwargs)
        print("...finish decorator...")
        print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    return wrapper

say(name, "Pushkin")
say = decorator(say)
print(say)

cuadratic_num = decorator(cuadratic_num)
print(cuadratic_num())


#-----------------------------------------------
