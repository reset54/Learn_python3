#import quicksort_recursive

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        
        mid = int((low + high)//2)
        # print("stage = " + str(mid), end=";\n") # test finding index
        guess = list[mid]   # mid - index
        
        if guess < item:
            low = mid + 1   # our finding value index element
        elif guess > item:
            high = mid - 1
        else:
          return mid  
    return(-1)

def check_exist_element(list, item):
    result = binary_search(list, item)
    if result != -1:
      return("Inlement is present at index", str(result))
    else:
      return("Index of element isn't present in array")


input_number = int(input())
array_1 = [1, -6, 17, 29, 105, -30, 0 , -1000, 24, 220]
print(f'Наш массив : {array_1}\nНаше вводимое число : {input_number}')

array_sort = sorted(array_1)
print(f"Array_sort : \n{array_sort}")
print(check_exist_element(array_sort, input_number))