# При розробці модуля було використано матеріали лекції теми 13 предмету
# Основи програмування 2018 УКУ

import timeit

line = [i for i in range(10000001)]


def search(lst, value):
    """ (list, int) -> int
    Returns the position in the list where value occurs or -1 if
    x is not in the list.
    >>> search([3, 1, 4, 2, 5], 4)
    2
    >>> search([3, 1, 4, 2, 5], 7)
    -1
    """
    try:
        return lst.index(value)
    except:
        return -1


def linear_search_while_loop(lst, value):
    """ (list, object) -> int
    Return the index of the first occurrence of value in lst, or return
    -1 if value is not in lst.
    >>> linear_search_while_loop([2, 5, 1, -3], 5)
    1
    >>> linear_search_while_loop([2, 4, 2], 2)
    0
    >>> linear_search_while_loop([2, 5, 1, -3], 4)
    -1
    >>> linear_search_while_loop([], 5)
    -1
    """
    i = 0  # The index of the next item in lst to examine.
    # Keep going until we reach the end of lst or until we find value.
    while i != len(lst) and lst[i] != value:
        i = i + 1
    # If we fell off the end of the list, we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i


def linear_search_for_loop(lst, value):
    """
    >>> linear_search_for_loop([2, 5, 1, -3], 5)
    1
    >>> linear_search_for_loop([2, 4, 2], 2)
    0
    >>> linear_search_for_loop([2, 5, 1, -3], 4)
    -1
    >>> linear_search_for_loop([], 5)
    -1
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def linear_search_sentinel_while_loop(lst, value):
    """
    (list, object) -> int
    >>> linear_search_sentinel_while_loop([2, 5, 1, -3], 5)
    1
    >>> linear_search_sentinel_while_loop([2, 4, 2], 2)
    0
    >>> linear_search_sentinel_while_loop([2, 5, 1, -3], 4)
    -1
    >>> linear_search_sentinel_while_loop([], 5)
    -1
    """
    # Add the sentinel.
    lst.append(value)
    i = 0
    # Keep going until we find value.
    while lst[i] != value:
        i = i + 1
    # Remove the sentinel.
    lst.pop()
    # If we reached the end of the list we didn't find value.
    if i == len(lst):
        return -1
    else:
        return i


def print_time(in_list, in_index, next_txt, file):
    """
    function to print the information
    :param in_list: input list
    :param in_index: input index
    :param next_txt: the header
    :return: None
    """
    print("\n" + "-" * 66 + "\n|" + next_txt.ljust(12) + "|", end='',
          file=file)
    array_of_functions = [linear_search_while_loop,
                          linear_search_for_loop,
                          linear_search_sentinel_while_loop,
                          search]
    for each in array_of_functions:
        time1 = timeit.default_timer()
        each(in_list, in_index)
        print("{:.10f}".format(
                float(timeit.default_timer() - time1))
              .center(12) + '|', end='', file=file)


with open('search_time_test.txt', 'w') as result:
    print("All time printed in seconds, array contained 10000000 list\n\n" +
          '-' * 66 + '\n' + "|" + "case".center(12) +
          "|" +
          "while".center(12) + '|' +
          "for".center(12) + '|' +
          "sentinel".center(12) + '|' +
          "list.index".center(12) + '|', end='', file=result)
    print_time(line, line[0], "First", result)
    print_time(line, line[5000000], "Middle", result)
    print_time(line, line[-1], "Last", result)
    print('\n' + '-' * 66, file=result)
