import doctest
import time
n = 2
arr = [[0] * n for i in range(n)]
numbers = list(map(int, input().strip().split()))


def smth(num):
    '''
    (type_input) -> type output
    Return ....

    >>> try1
    res1
    >>> try2
    res2

    '''
    try:
        month, year = int(input(month)), int(input(year))
        assert (1 <= month <= 12)
        assert isinstance(num, int), "Alert of eexeption"
        if (month == 1) or (month == 3):
            pass
        else:
            pass
    except ValueError:
        print("Please, type integers")
    except AssertionError:
        print("Please, type correct month number (from 1 to 12)")

    # here type your code


time_start = time.time()
smth(60)
time_end = time.time()
time_of_prog = time_end - time_start

doctest.testmod()
