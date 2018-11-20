import sys


def return_digits(number=0):
    '''
    (int) -> str

    Return number written by big digits
    >>> return_digits(123)
    ' 1  222  333 \\n11 2   23   3\\n 1 2  2     3\\n 1   2    33 \\n 1  2       3\\n 1 2    3   3\\n11122222 333 '
    '''

    Zero = ["  ***  ",
            " *   * ",
            "*     *",
            "*     *",
            "*     *",
            " *   * ",
            "  ***  "]
    One = [" * ",
           "** ",
           " * ",
           " * ",
           " * ",
           " * ",
           "***"]
    Two = [" *** ",
           "*   *",
           "*  * ",
           "  *  ",
           " *   ",
           "*    ",
           "*****"]
    Three = [" *** ",
             "*   *",
             "    *",
             "  ** ",
             "    *",
             "*   *",
             " *** "]
    Four = ["   *  ",
            "  **  ",
            " * *  ",
            "*  *  ",
            "******",
            "   *  ",
            "   *  "]
    Five = ["*****",
            "*    ",
            "*    ",
            " *** ",
            "    *",
            "*   *",
            " *** "]
    Six = [" *** ",
           "*    ",
           "*    ",
           "**** ",
           "*   *",
           "*   *",
           " *** "]
    Seven = ["*****",
             "    *",
             "   * ",
             "  *  ",
             " *   ",
             "*    ",
             "*    "]
    Eight = [" *** ",
             "*   *",
             "*   *",
             " *** ",
             "*   *",
             "*   *",
             " *** "]
    Nine = [" ****",
            "*   *",
            "*   *",
            " ****",
            "    *",
            "    *",
            "    *"]
    Digits = [Zero, One, Two, Three,
              Four, Five, Six, Seven, Eight, Nine]

    try:
        try:
            digits = sys.argv[1]
        except:
            digits = str(number)
        row = 0
        result = ""
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                line += digit[row].replace("*", str(number))
                column += 1
            result += line + "\n"
            row += 1
        return result[:-1]
    except IndexError:
        print("usage: bigdigits.py <number>")
    except ValueError as err:
        print(err, "in", digits)


if __name__ == '__main__':
    print(return_digits(120))


import doctest
doctest.testmod()
