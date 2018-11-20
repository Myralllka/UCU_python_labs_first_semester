def happy_number(number):
    '''
    (int) -> bool

    Return if inputed number is happy ticket`s number
    if sum of first for digits equal sum of last for digits
    >>> happy_number(191234)
    True
    >>> happy_number(43211234)
    True
    >>> happy_number(0)
    True
    >>> happy_number(12345)
    False
    '''
    assert ((number >= 0) and (number < 100000000)
            ), "input number is not number of ticket"

    def sum_of_digits(ll):
        '''
        (list) -> int

        return digit - sum of digits in number
        >>> sum_of_digits([1, 3, 4, 1])
        9
        >>> sum_of_digits([0])
        0
        >>> sum_of_digits([0, 9, 9, 1])
        1
        '''
        if (len(ll) == 1):
            return ll[0]
        else:
            return sum_of_digits(list(map(int, list(str(sum(ll))))))

    number = str(number)[::-1]
    while len(number) < 8:
        number += "0"
    list1, list2 = [], []
    for each in range(4):
        list1.append(int(number[each]))
        list2.append(int(number[each + 4]))

    return (sum_of_digits(list1) == sum_of_digits(list2))


def count_happy_numbers(number):
    '''
    (int) -> int

    Return number of happy number in range from 0 to nubmer
    '''
    counter = 0
    for i in range(number + 1):
        if happy_numbers(i):
            counter += 1
    return counter


def happy_numbers(m, n):
    '''
    (int, int) -> list

    Return list of happy numbers in range from m to n
    '''
    result = []
    for each in range(m, n + 1):
        if (happy_number(each)):
            result.append(each)
    return result


# print(happy_number(191234))
import doctest
print(doctest.testmod())
