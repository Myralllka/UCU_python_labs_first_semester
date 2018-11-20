import doctest


def egg_carton_box(eggs):
    '''
    (number) -> number
    Return float value, minimuym number of boxes to pack all eggs
    >>> egg_carton_box(12)
    2
    >>> egg_carton_box(28)
    3
    >>> egg_carton_box(10)
    1
    '''
    if (eggs % 10):
        return (eggs // 10) + 1
    else:
        return (eggs // 10)


doctest.testmod()
