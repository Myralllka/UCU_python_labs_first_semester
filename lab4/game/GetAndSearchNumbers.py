import random


def ulam_list_generator(number):
    """
    (int) -> list

    Return the list of ulam numbers below or equal to given one

    >>> ulam_list_generator(20)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    """
    res = [1, 2]
    counter = 1
    for i in range(res[counter] + 1, number + 1):
        addition = 0
        for j in range(0, counter + 1):
            for k in range(j + 1, counter + 1):
                if res[j] != res[k] and res[j] + res[k] == i:
                    addition += 1
        if addition == 1:
            res.append(i)
            counter += 1
    return res


def ulam_number_generator(number):
    """
    (int) -> int

    Return a random ulam number below or equal to given number
    """
    return random.choice(ulam_list_generator(number))


def pair_number_generator(number):
    """
    (int) -> int

    Return a random pair number below or equal to given number
    """
    res = []
    for i in range(2, number + 1, 2):
        res.append(i)
    return random.choice(res)


def happy_number_generator(number):
    """
    (int) -> int

    Return a random happy number below or equal to given number
    """
    res = []
    for i in range(number + 1):
        if is_happy_number(i):
            res.append(i)
    return random.choice(res)


def is_happy_number(number):
    """
    (int) -> bool

    Checks if the number is happy

    >>> is_happy_number(13)
    True

    >>> is_happy_number(10)
    False
    """
    variations = {number}
    while number != 1:
        new_number = 0
        for i in str(number):
            new_number += int(i) * int(i)
        if new_number in variations:
            return False
        else:
            variations.add(new_number)
        number = new_number
    return True


def is_pair_number(number):
    """
    (int) -> bool

    Checks if the number is pair

    >>> is_pair_number(11)
    False

    >>> is_pair_number(10)
    True
    """
    return number % 2 == 0


def is_ulam_number(number):
    """
    (int) -> bool

    Checks if the number is ulam`s

    >>> is_ulam_number(11)
    True

    >>> is_ulam_number(10)
    False
    """
    return number in ulam_list_generator(number)
