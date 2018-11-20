def is_power_of_two(val):
    """
    (int) -> bool

    Determine if a number is a power of two.

    >>> is_power_of_two([0])

    >>> is_power_of_two("0")

    >>> is_power_of_two(0)
    False
    >>> is_power_of_two(1)
    True
    >>> is_power_of_two(2)
    True
    >>> is_power_of_two(15)
    False
    >>> is_power_of_two(16)
    True
    """
    try:
        return (list(bin(val)[2:]).count('1') == 1) and val > 0
    except TypeError:
        return None


def has_unique_chars(string):
    """
    (str) -> bool

    An algorithm to determine if a string has all unique characters.

    >>> has_unique_chars(None)
    False
    >>> has_unique_chars('')
    True
    >>> has_unique_chars('foo')
    False
    >>> has_unique_chars('bar')
    True
    """
    try:
        for each in string:
            if (string.count(each) > 1):
                return False
        return True
    except TypeError:
        return False


def compress(string):
    """
    (str) -> str

    Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.

    >>> compress(None)

    >>> compress('')
    ''
    >>> compress('AABBCC')
    'AABBCC'
    >>> compress('AAABCCDDDDE')
    'A3BC2D4E'
    >>> compress('BAAACCDDDD')
    'BA3C2D4'
    >>> compress('AAABAACCDDDD')
    'A3BA2C2D4'
    """
    try:
        result, letter, counter = '', '', 1
        for each in range(len(string)):
            new_letter = string[each]
            if new_letter == letter:
                counter += 1
            else:
                if (counter > 1):
                    result += letter + str(counter)
                else:
                    result += letter
                counter, letter = 1, new_letter
        if (counter > 1):
            result += letter + str(counter)
        else:
            result += letter
        if(len(result) < len(string)):
            return result
        return string
    except TypeError:
        return None

import doctest
doctest.testmod()
