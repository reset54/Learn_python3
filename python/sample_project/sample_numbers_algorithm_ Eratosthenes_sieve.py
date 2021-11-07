def alg_sieve_of_Eratosthenes(num: int) -> list:    # cycle go before number = num
    """ alghorithm finding sample numbers """
    array = [2]                                     # beginning, start number = 2                      
    for i in range(3, num + 1):                     # range(start, stop[, step]) -> range object
        k = 0                            
        for j in array:
            if i % j == 0:
                k = 1
        if k == 0:
            array.append(i)         
    return(array)

# run func
print(alg_sieve_of_Eratosthenes(1000))
print(alg_sieve_of_Eratosthenes(100))
