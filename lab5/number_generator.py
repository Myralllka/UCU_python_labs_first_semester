def number_generator(number, digit, position):
    '''
    (3 numbers) -> number
    (number, digit (in range[0, 9]), position) -> formated number
    Return formated number
    if number[position] > digit
    return number
    else return number with replaced digit and digin on that position
    >>> number_generarator(3746, 5, 0)
    3766
    >>> number_generarator(3746, 5, 3)
    5746
    >>> number_generarator(3746, 5, 7)
    50003746
    '''
    is_positiv = False
    if (abs(number) == number):
        is_positiv = True
    else:
        number = abs(number)
    calculate_variable = (number // pow(10, position + 1)) * \
        (pow(10, position + 1))
    differense = ((number - calculate_variable) // pow(10, position))
    if (differense < digit):
        number -= ((number - calculate_variable) //
                   pow(10, position) * pow(10, position))
        number += digit * pow(10, position)
    if is_positiv:
        return number
    else:
        return -number

print(number_generarator(-3746, 7, 7))
