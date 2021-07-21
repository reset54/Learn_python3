<<<<<<< HEAD
import time

# quicksort recursive from book Grokking Algorithms (str 92)
# супер книга, всем рекомендую!

def quicksort_recursive(array):
    if len(array) < 2:
        return array
    else:
        # опорный элемент, рекурсивный случай
        pivot = array[0]
        # подмассив всех элементов Меньше, либо равных опорному
        less = [i for i in array[1:] if i <= pivot]
        # подмассив элементов Больше опорного
        greater = [i for i in array[1:] if i > pivot]
        # less и greater передаются в качестве аргумента функции!
        result = quicksort_recursive(less) + [pivot] + quicksort_recursive(greater)
        return (result)
        # print(result)

# массив для примера
massiv_1 = [35, 10, -16, 0, 6, 15, 28, 100, 132, 1018, 156, 230, -29]

# вызов
print(quicksort_recursive(massiv_1))

# https://coderoad.ru/2662140/%D0%BA%D0%B0%D0%BA-%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B8%D1%82%D1%8C-%D0%B2%D1%80%D0%B5%D0%BC%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%BE%D0%B2-%D0%B2-python
# https://www.yuripetrov.ru/edu/python/ch_06_01.html

# def timeit(func(**kwargs)):
#     """Выполнить функицю 'func' с параметрами '*args', '**kw' и
#     вернуть время выполнения в мс."""
#     time_start = time.time()
#     res = func(kwargs)
#     time_end = time.time()
#     return (time_end - time_start) * 1000.0
=======
import time

# quicksort recursive from book Grokking Algorithms (str 92)
# супер книга, всем рекомендую!

def quicksort_recursive(array):
    if len(array) < 2:
        return array
    else:
        # опорный элемент, рекурсивный случай
        pivot = array[0]
        # подмассив всех элементов Меньше, либо равных опорному
        less = [i for i in array[1:] if i <= pivot]
        # подмассив элементов Больше опорного
        greater = [i for i in array[1:] if i > pivot]
        # less и greater передаются в качестве аргумента функции!
        result = quicksort_recursive(less) + [pivot] + quicksort_recursive(greater)
        return (result)
        # print(result)

# массив для примера
massiv_1 = [35, 10, -16, 0, 6, 15, 28, 100, 132, 1018, 156, 230, -29]

# вызов
print(quicksort_recursive(massiv_1))

# https://coderoad.ru/2662140/%D0%BA%D0%B0%D0%BA-%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B8%D1%82%D1%8C-%D0%B2%D1%80%D0%B5%D0%BC%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%BE%D0%B2-%D0%B2-python
# https://www.yuripetrov.ru/edu/python/ch_06_01.html

# def timeit(func(**kwargs)):
#     """Выполнить функицю 'func' с параметрами '*args', '**kw' и
#     вернуть время выполнения в мс."""
#     time_start = time.time()
#     res = func(kwargs)
#     time_end = time.time()
#     return (time_end - time_start) * 1000.0
>>>>>>> refs/remotes/origin/readme
# print(timeit(quicksort(massiv_1)))