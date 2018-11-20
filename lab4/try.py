import doctest


def sqrt(x):
    '''
    (number) -> number

    Return square root of number by Newton`s Method
    guess = 1.0
    new_guess = 1/2(guess + x/guess)

    >>> sqrt(0.023)
    0.15165750888103102

    >>> sqrt(72)
    8.485281374239733
    '''

    def sqrtIter():
        numeric = 1
        while (goodEnough(numeric)):
            numeric = average(numeric, x / numeric)
        return numeric

    def average(a, b):
        return(a + b) / 2

    def goodEnough(res):
        if(round(res ** 2, 10) == x):
            return 0
        else:
            # print(res ** 2)
            return 1

    return sqrtIter()
# print(sqrt(72))


doctest.testmod()
