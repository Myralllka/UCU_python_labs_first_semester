import functools


@functools.lru_cache(maxsize=None)
def print_result(i, j, checker=1):
    """
    recursive function to print table like

    1    1    1    1    1
    1    2    3    4    5
    1    3    6   10   15
    1    4   10   20   35
    1    5   15   35   70

    :param i: list index of rows
    :param j: list index of columns
    :param checker: print first '1'
    """
    if checker:
        print("1".rjust(5), end='')
        checker = 0
    if i == 0 and j == 0:
        # print("1".rjust(5), end='')
        return 1
    elif j == 0:
        print('\n' + '1'.rjust(5), end='')
        return print_result(i-1, j, checker)
    elif i == 0:
        print('1'.rjust(5), end='')
        return print_result(i, j-1, checker)
    else:
        print(str(print_result(i - 1, j, checker) +
              print_result(i, j - 1, checker)).rjust(5), end='')
        return (print_result(i - 1, j, checker) +
                print_result(i, j - 1, checker))


n, m = map(int, input().strip().split())
print_result(n - 1, m - 1)
# main()
