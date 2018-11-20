import doctest


def rps_game(lst):
    '''
    (list) -> list

    Return list of tuples - results in game rock-scissors-paper

    >>> rps_game(['SS', 'RS', 'PS'])
    [(False, False), (True, False), (False, True)]
    >>> rps_game(['PR'])
    [(True, False)]
    '''

    result_list = []
    for each in lst:
        each = each.upper()
        if (each == "SS" or each == "PP" or each == "RR"):
            result_list.append((False, False))
        elif (each == "SP" or each == "PR" or each == "RS"):
            result_list.append((True, False))
        elif (each == "PS" or each == "RP" or each == "SR"):
            result_list.append((False, True))
    return(result_list)

doctest.testmod()
