def division_of_two(number, divisor):
    '''
    (number, number) -> bool
    Return True if number // divisor and False if not
    >>> division_of_two(81, 9)
    True
    >>> division_of_two(81, 2)
    False
    >>> division_of_two(11, 6)
    False
    '''
    return number % divisor == 0
