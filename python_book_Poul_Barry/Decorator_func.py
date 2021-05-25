a = int( input("введите необходимое число: ") )

def cuadratic_num():
    x = a*a
    return x
# decorator
#@decorator_cuadratic_num()
def decorator(func):
    def func_1(*args, **kwargs):
        print("...start decorater...")
        func(*args, **kwargs)
        print("...finish decorater...")
    return func_1

def say(name, surname):
    print("hello world!", name, surname)

print (cuadratic_num())
cuadratic_num = decorator(cuadratic_num)
cuadratic_num

say = decorator(say)
#say()
say("Vasyatka", "Pupkin")