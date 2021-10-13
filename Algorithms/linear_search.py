# option search, when checking all elements
# Алгоритм линейный поиск, линейная сложность O(N) поиск подходящего или наиболее подходящего элемента


our_array = [1, 2, 1, 3, 3, 7, 10, 12, 2, 4]
our_array_2 = "aabbbccccddeeeeeeeffffggggggggghhhhhhhhhjj"


def find_left_index(sequence: list, element) -> int:
    ans = -1 
    for i in range(len(sequence)):                  # enumerate
        if ans == -1 and sequence[i] == element:    # check
            ans = i
    return(f"Option 1: {ans}")


def find_right_index(sequence: list, element) -> int:
    ans = -1 
    for i in range(len(sequence)):                  # enumerate
        if sequence[i] == element:                  # check
            ans = i
    return(f"Option 2: {ans}")


def find_max_index(sequence: list) -> int, int:
    max = sequence[0]
    index_max = 0
    for i in range(len(sequence)):
        if sequence[i] > max:                       # statement find max
            max = sequence[i]
            if sequence[i] == max:
              index_max = i
    return(f"Option 3: max = {max}, index_max = {index_max}")
    

# def find_max_symbols(sequence):
#     max_char = i
#     index_max = 0
#     for i in range(len(sequence)):
#         if sequence[i] > sequence[max_char]:
#             max = sequence[i]
#         index_max = i
#     return(f"Option 4: sequence[max_char] = {sequence[max_char]}")
    

# test
def test_array(array: list):
    print(f"Первое вхождение element {7} \nstart (left) index element in sequence = {find_left_index(array, 7)}")
    print(f"Последнее вхождение element {2} \nlast (right) index element in sequence = {find_right_index(array, 2)}")
    print(f"Max element \nmax index element in sequence = {find_max_index(array)}")
    # print(f"Максимальное количество элементов следующих друг за другом\nMaximum number of elements following each other in sequence = {find_max_index(array)}")
    
# run tests
test_array(our_array)
test_array(our_array_2)
test_array(input())
