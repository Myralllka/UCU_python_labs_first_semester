# При розробці модуля було використано матеріали лекції теми 13 предмету
# Основи програмування 2018 УКУ

import time


def numbers_time_test(function, type_of_function, number, verbose=0):
    """
    string, string, int, int -> None

    main function for appreciation time of usage different functions

    :param function: fibonacci or factorial
    :param type_of_function: recursion or loop
    :param number: needed value for the function
    :param verbose: 1 or 0: if you need the information about stack or not
    :return: None
    """

    try:
        verbose = int(number[1])
        number = int(number[0])
    except:
        number = int(number[0])

    assert number >= 0, "number need to be positive"

    def factorial_recursion(n, depth=0, verbose=0):
        """
        int, int, int -> int

        calculate the factorial of the input variable using factorial

        :param n: needed value for the function
        :param depth: information about the stack
        :param verbose: 0 or 1: if you need the information about stack or not
        :return: nth factorial value

        >>> factorial_recursion(10)
        3628800
        """
        if verbose:
            print("|   " * depth, "factorial(", n, "):")
        if n < 2:
            result = 1
        else:
            result = n * factorial_recursion(n - 1, depth + 1, verbose)
        if verbose:
            print("|   " * depth, "-->", result)
        return result

    def fibonacci_recursion(n, depth=0, verbose=0):
        """
        int, int, int -> int

        calculate the nth fibonacci number using recursion

        :param n: needed value for the function
        :param depth: information about the stack
        :param verbose: 0 or 1: if you need the information about stack or not
        :return: nth fibonacci number

        >>> fibonacci_recursion(10)
        55
        """
        assert number > 0, "number need to be positive"
        if verbose:
            print("|   " * depth, "fibonacci(", n, "):")
        if n < 3:
            result = 1
        else:
            if verbose:
                print("|   " * depth, "-->", 'fibonacci(', n - 1, ') '
                                                                 '+ fibonacci(',
                      n - 2, ')')
            result = (fibonacci_recursion(n - 1, depth + 1, verbose) +
                      fibonacci_recursion(n - 2, depth + 1, verbose))
        if verbose:
            print("|   " * depth, "-->", result)
        return result

    def factorial_loop(n, verbose=0):
        """
        int, int -> int

        calculate the factorial of the input variable using loop

        :param n: needed value for the function
        :return: nth factorial value

        >>> factorial_loop(10)
        3628800
        """
        result = 1
        for i in range(n):
            result *= (i + 1)
        return result

    def fibonacci_loop(n, verbose=0):
        """
        int, int -> int

        calculate the nth fibonacci number using loop

        :param n: needed value for the function
        :return: nth fibonacci number

        >>> fibonacci_loop(10)
        55
        """
        assert number > 0, "number need to be positive"
        curr = 1
        prev = 1
        for i in range(n - 2):
            curr, prev = curr + prev, curr
        return curr

    time1 = time.time()
    a = eval(function + "_" + type_of_function +
             '(' + str(number) + ', verbose=' + str(verbose) + ')')
    if verbose:
        print("time: {:.15f}".format(float(time.time() - time1)))
    print("result:", a)


if __name__ == "__main__":
    print("usage: [function_name] [function_type] [number] <verbose>\
    \n\tfunction name: factorial or fibonacci\
    \n\tfunction_type: loop or recursion \
    \n\tnumber: positive int\
    \n\tverbose: 0 or 1")
    a = input().split()
    numbers_time_test(a[0], a[1], (a[2:]))

    # numbers_time_test('fibonacci', "loop", 1, 0)
    # numbers_time_test("factorial", "loop", 1, 0)
    # numbers_time_test('fibonacci', 'recursion', 1, 0)
    # numbers_time_test("factorial", 'recursion', 1, 0)
