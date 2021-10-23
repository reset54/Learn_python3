import time


def binary_search(list, item: int) -> int:
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high)//2)
        # print(f"stage = {mid}", end=";\n") # test finding index
        guess = list[mid]   # mid - index
        if guess < item:
            low = mid + 1   # our finding value index element
        elif guess > item:
            high = mid - 1
        else:
          return mid  
    return(-1)


def check_exist_element(list, item: int) -> str:
    result = binary_search(list, item)
    if result != -1:
      return("Inlement is present at index", str(result))
    else:
      return("Index of element isn't present in array")


# tests
input_number = int(input())
array_1 = [1, -6, 17, 29, 105, -30, 0 , -1000, 24, 220]
print(f'Тестовый массив : {array_1}\nНаше вводимое число : {input_number}')

start = time.time()
array_sort = sorted(array_1)
end = time.time()
print(f"\nВремя, затраченное на сортировку тестового массива: \n{end - start}")

print(f"\nArray_sort : \n{array_sort}\n")
start = time.time()
print(check_exist_element(array_sort, input_number))
end = time.time()
print(f"время, затраченное на выполнение функции: \ncheck_exist_element = \n{end - start}")
