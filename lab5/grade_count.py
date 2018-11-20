import doctest


def grade_count(grades):
    '''
    (list) -> tuple

    >>> grade_count([85, 90, 67, 70, 87])
    (79.8, 'C')
    >>> grade_count([97, 93, 84, 78, 80])
    (86.4, 'B')
    '''
    dictionary = {
        "F": range(6000),
        "E": range(6000, 6700),
        "D": range(6700, 7500),
        "C": range(7500, 8200),
        "B": range(8200, 9000),
        "A": range(9000, 10100)
    }
    for each in grades:
        if not (each in range(101)):
            return(None, None)
    middle_of_grades = sum(grades) / 5 * 100
    for each in dictionary:
        if (middle_of_grades in dictionary[each]):
            return((middle_of_grades / 100, each))


doctest.testmod()
