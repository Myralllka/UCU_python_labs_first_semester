import doctest


def egg_carton_box(eggs):
    '''
    (number) -> list
    Return list of values
    the minimum number of boxes and which of boxes (4, 6, 10) we need

    >>> egg_carton_box(12)
    [6, 6]
    >>> egg_carton_box(28)
    [10, 10, 10]
    >>> egg_carton_box(10)
    [10]
    >>> egg_carton_box(41)
    [6, 6, 10, 10, 10]
    >>> egg_carton_box(122)
    [6, 6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    >>> egg_carton_box(27)
    [10, 10, 10]
    '''
    result = []
    helped_var = eggs
    while (helped_var > 12):
        helped_var -= 10
        result.append(10)
    if (helped_var == 10):
        result.append(10)
    elif (helped_var % 10 in range(1, 3)):
        result.append(6)
        result.append(6)
    elif (helped_var in range(3, 5)):
        result.append(4)
    elif (helped_var in range(5, 7)):
        result.append(6)
    elif (helped_var == 0):
        return ([])
    else:
        result.append(10)
    return (sorted(result))


doctest.testmod()
# print(egg_carton_box(0))
