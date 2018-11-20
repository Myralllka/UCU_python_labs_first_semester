import doctest


def add_digits(number):
    '''
    (int) -> int

    Return sum of numerical digit in number

    >>> add_digits(124)
    7
    >>> add_digits(45643)
    4
    >>> add_digits(0)
    0
    >>> add_digits(1)
    1
    '''
    # result = 0
    # for each in str(number):
    #     result += int(each)
    # if result > 9:
    #     return(add_digits(result))
    # return(result)

    if(number == 0):
        return 0
    elif (number % 9 == 0):
        return 9
    else:
        return number % 9


doctest.testmod()
