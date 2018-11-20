def equal_parts(numbers):
    ''''
    list(int) -> (list(int),list(int))

    Return two integers list of equal sum as an attempt \
    at a partition of input numbers

    if it is impossible, function return approximated result

    >>> equal_parts([2, 4, 5, 6, 7, 12, 13, 23, 1, 1, 34])
    ([23, 13, 7, 6, 4, 1], [34, 12, 5, 2, 1])
    >>> equal_parts([-2, 4, -5, 6, 7, 12, -13, 23, 1, 1, 34, 34, 12, 1, 67, 34, 98])
    ([67, 34, 34, 12, 12, 6, 1, 1], [98, 34, 23, 7, 4, 1, -2, -5, -13])
    '''
    array1, array2 = [], []
    for each in reversed(sorted(numbers)):
        if (sum(array1) < sum(array2)):
            array1.append(each)
        else:
            array2.append(each)
    return (array1, array2)
    # print(array1, array2, sum(array1), sum(array2))

# print(equal_parts([2, 4, 5, 6, 7, 12, 13, 23, 1, 1, 34]))
import doctest
print(doctest.testmod())