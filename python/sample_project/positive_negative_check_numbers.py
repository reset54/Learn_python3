our_input_string = input()

our_input_string = our_input_string.replace(",", ".")

if (type(our_input_string) == "<class 'str'>"):
    print("Пожалуйста введите числовое значение аргумента фнкции, а не строковое")
elif (type(our_input_string) == True or type(our_input_string) == False):
    print("Пожалуйста введите числовое значение аргумента фнкции, а не булевое")
else:
    if (float(our_input_string) > 0):
        print("Это положительное число")
    elif (float(our_input_string) == 0):
        print("Это ноль")
    else:
        print("Это отрицательное число")