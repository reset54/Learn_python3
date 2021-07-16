# option search, when checking all elements
print("\nАлгоритм линейный поиск, линейная сложность O(N)\nпоиск подходящего или наиболее подходящего элемента")


array = [1, 2, 1, 3, 3, 7, 10, 12, 2, 4]
array_2 = "aabbbccccddeeeeeeeffffggggggggghhhhhhhhhjj"

#_____________________________Option 1_________________________________
print("\nOption 1:")
def find_left_index(sequence, element):
    ans = -1 
    for i in range(len(sequence)):                # enumerate
        if ans == -1 and sequence[i] == element:  # check
            ans = i
    return ans


print(f"Первое вхождение element {7} \nstart (left) index element in sequence = {find_left_index(array, 7)}")

#_____________________________Option 2_________________________________
print("\nOption 2:")
def find_right_index(sequence, element):
    ans = -1 
    for i in range(len(sequence)): # enumerate
        if sequence[i] == element: # check
            ans = i
    return ans
print(f"Последнее вхождение element {2} \nlast (right) index element in sequence = {find_right_index(array, 2)}")

#_____________________________Option 3_________________________________
print("\nOption 3: find max")
def find_max_index(sequence):
    max = sequence[0]
    index_max = 0
    for i in range(len(sequence)):
        if sequence[i] > max:      # statement find max
            max = sequence[i]
            if sequence[i] == max:
              index_max = i
    return max, index_max
    
print(f"Max element \nmax index element in sequence = {find_max_index(array)}")

#_____________________________Option 4_________________________________
#print("\nOption 4: find max symbols one after another")
#def find_max_symbols(sequence):
#    max_char = i
    # index_max = 0
#    for i in range(len(sequence)):
#        if sequence[i] > sequence[max_char]:
#            max = sequence[i]
#        index_max = i
#    return sequence[max_char]
    
#print(f"Максимальное количество элементов следующих друг за другом\nMaximum number of elements following each other in sequence = {find_max_index(array)}")

