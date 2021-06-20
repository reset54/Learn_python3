# alghorithm finding sample numbers
array = [2]                     # beginning, start number = 2
n = 1000                        # before number = n
for i in range(3, n + 1):       # range(start, stop[, step]) -> range object
    k = 0                       # 
    for j in array:
        if i % j == 0:
            k = 1
    if k == 0:
        array.append(i)
print(array)