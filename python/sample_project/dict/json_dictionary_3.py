import json


try:
    number = input()
    number = int(number)
    my_dict = {}
    for i in range(number):
        my_dict[str(i + 1)] = (i + 1)**2
    print(json.dumps(my_dict, ensure_ascii=False))

except TypeError:
    print("передайте число")
except ValueError:
    print("передайте число")
except NameError:
    print("передайте число")