

import time


def binary_search(arr: list, item: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high)//2)
        # print(f"stage = {mid}", end=";\n") # test finding index       # debug
        guess = arr[mid]                                               # mid - index
        if guess < item:
            low = mid + 1                                               # our finding value index element
        elif guess > item:
            high = mid - 1
        else:
          return mid  
    return(-1)


def check_exist_element(arr: list, item: int) -> str:
    result = binary_search(arr, item)
    if result != -1:
        return("Inlement is present at index", str(result))
    else:
        return("Index of element isn't present in array")



def test_time(func) -> str:
    '''tests the function for the elapsed time''' 
    input_number = int(input())                                # необходимо передать число!, которое будем искать в массиве
    test_array = [1, -6, 17, 29, 105, -30, 0 , -1000, 24, 220] # передайте в тестовую функцию другой массив, чтобы понять скорость работы функции по разнице времени
    start = time.time()
    func(test_array, input_number)
    end = time.time()
    print(f'\nТестовый массив : {test_array}\nНаше вводимое число : {input_number}')
    print(f"Время, затраченное на работу функции {func}: \n{end - start}")


# run test func
test_time(binary_search)
test_time(check_exist_element)
