# with open("text.txt", "w") as output_file:
#     print("Hello", end="!", sep="!", file=output_file)

# def onesDigit(n):
#     return n % 10


# def testOneDigit():
#     print("Testing onesDigit()...", end="")
#     assert(onesDigit(5) == 5)
#     assert(onesDigit(123) == 3)
#     assert(onesDigit(100) == 0)
#     assert(onesDigit(999) == 9)
#     assert(onesDigit(-123) == 3)
#     print("passed!")


# testOneDigit()

import doctest


def area(side, height):
    '''
    (number, number) -> number
    Return the area of a rombus with dimentions side and height.
    >>> area(11, 11)
    120
    >>> area(5.5, 7)
    38.5
    '''
    return side * height

doctest.testmod()