our_string = "".join(input())
new_set = set(our_string)
print(new_set)

# matches in order of meeting chars
print("".join(sorted(set(our_string), key=our_string.index)))


array_1 = [55, 11, 22]
print(id(array_1)) # id 140108065812736
array_1 = sorted([55, 11, 22])
print(id(array_1)) # id 140108066686272 , new array

array_2 = [525, 111, -23]
print(id(array_2)) # id 
array_2 = [525, 111, -23].sort()
print(id(array_2)) # id 94568679513312

