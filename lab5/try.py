import doctest


def factorial(n):
    """
    int -> int

    Return factorial of n

    >>> factorial(5)
    120

    >>> factorial(0)
    1
    """

    result = n
    if n == 0:
        return 1
    elif (n == 1):
        return 1
    elif (n == 2):
        return 2
    else:
        return n * factorial(n - 1)


def repeated_digits(n):
    """
    int -> bool

    Return return True if the number n has at least one pair of sequentially 
    repeating digits and False otherwise 

    >>> 77
    True

    >>> 123
    False

    >>> -123
    False

    """
    if n > 0:
        remaining_digits = n
    else:
        n = -n
    while remaining_digits // 10 > 0:
        first_digit = remaining_digits % 10
        tens_digit = (remaining_digits // 10) % 10
        if first_digit == tens_digit:
            print(n, "has repeated digits!")
            return True
        remaining_digits = remaining_digits // 10
    print(n, "has no repeated digits...")
    return False

doctest.testmod()
