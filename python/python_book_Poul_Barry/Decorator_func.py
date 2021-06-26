a = int( input("введите необходимое число: ") )
name = input("Введите имя: ")

def cuadratic_num():
    x = a*a
    return x

# decorator
#@decorator
def decorator(func):
    def func_1(*args, **kwargs):
        print("▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲")
        print("...start decorater...")
        func(*args, **kwargs)
        print("...finish decorater...")
        print("▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼")
    return func_1

def say(name, surname):
    print("Hello! ", name, surname)

print(cuadratic_num())

cuadratic_num = decorator(cuadratic_num)
print(cuadratic_num())

say = decorator(say)
say("What do you say me", name + "?")