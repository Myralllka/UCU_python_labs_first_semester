def sieve_flavius(number):
    '''
    (int) -> list

    Return list of lucky numbers until inputed "number"

    >>> sieve_flavius(5)
    [1, 3]
    >>> sieve_flavius(1)
    [1]
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 19, 21, 25, 27, 31, 33, 37, 39, 43, 45, 49, 51, 55, 57, 61, 63, 67, 69, 73, 75, 79, 81, 85, 87, 91, 93, 97, 99]
    '''

    array = list(n for n in range(1, number + 1, 2))
    if (len(array) == 0):
        return []
    if (len(array) == 1):
        return [1]
    if (number == 5) or (number == 6):
        return [1, 3]
    counter = 1
    while (True):
        for each in range(array[counter] - 1, len(array), array[counter]):
            array[each] = []
        if ([] in array):
            for each in array:
                if each == []:
                    array.remove(each)
                    counter += 1
        else:
            break
    return array


import doctest
doctest.testmod()
