import doctest


def borsch_ingredients(portions):
    '''
    (int) -> list

    Return list of tuples of ingridients and their weight

    >>> borsch_ingredients(8)
    [('яловичина', 700), ('буряк', 500), ('картопля', 500), ('морква', 200), ('цибуля', 200), ('помідори', 300), ('капуста', 300)]
    >>> borsch_ingredients(10)
    [('яловичина', 900), ('буряк', 700), ('картопля', 700), ('морква', 300), ('цибуля', 300), ('помідори', 400), ('капуста', 400)]
    '''
    result = []
    array = [700, 500, 500, 200, 200, 300, 300]
    array_ing = ['яловичина', 'буряк', 'картопля',
                 'морква', 'цибуля', 'помідори', 'капуста']
    for each in range(len(array)):
        if (array[each] / 8 * portions <=
                round(array[each] / 8 * portions, -2)):
            result.append((array_ing[each], int(
                round(array[each] / 8 * portions, -2))))
        else:
            result.append((array_ing[each], int(
                round((array[each]) / 8 * portions, -2)) + 100))
    return (result)


# print(borsch_ingredients(10))
doctest.testmod()
