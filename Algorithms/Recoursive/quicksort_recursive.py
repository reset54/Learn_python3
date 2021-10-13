import time
# quicksort recursive from book Grokking Algorithms (str 92)
some_arr_1 = [35, 10, -16, 0, 6, 15, 28, 100, 132, 1018, 156, 230, -29]


def quicksort_recursive(array: list):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        result = quicksort_recursive(less) + [pivot] + quicksort_recursive(greater)
        return (result)

        
def test_and_print(array: list) -> list:
    print(f"{quicksort_recursive(array)}")

    
# Run test
test_and_print(some_arr_1)

# https://coderoad.ru/2662140/%D0%BA%D0%B0%D0%BA-%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B8%D1%82%D1%8C-%D0%B2%D1%80%D0%B5%D0%BC%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%BE%D0%B2-%D0%B2-python
# https://www.yuripetrov.ru/edu/python/ch_06_01.html

# def timeit(func(**kwargs)):
#     """
#     Выполнить функцию 'func' с параметрами '*args', '**kw' и
#     вернуть время выполнения в мс.
#     """
#     time_start = time.time()
#     res = func(kwargs)
#     time_end = time.time()
#     return (time_end - time_start) * 1000.0
