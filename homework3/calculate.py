def calculate(numbers):
    '''
    (list) -> int

    Return list of numbers, length of list, sum of numbers, min and max
    values, average value and middle value of inputed list of numbers.

    >>> calculate(([2, 3, 1, 3, 4, 1, 0]))
    ([2, 3, 1, 3, 4, 1, 0], 7, 14, 0, 4, 2.0, 2)
    '''
    def sorting(lst):
        '''
        (list) -> list

        Return sorted list using bubble sort

        >>> sorting([2, 3, 1, 3, 4, 1, 0])
        [0, 1, 1, 2, 3, 3, 4]
        '''
        for i in range(len(lst) - 1, 0, -1):
            for j in range(i):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst
    lstt = numbers.copy()
    middle_value = sorting(lstt)[len(lstt) // 2]
    if (len(lstt) % 2 == 0):
        middle_value = (sorting(lstt)[len(lstt) // 2 - 1] +
                        sorting(lstt)[len(lstt) // 2]) / 2
    return (numbers, len(numbers), sum(numbers), min(numbers),
            max(numbers), sum(numbers) / len(numbers), middle_value)

if __name__ == '__main__':
    d, list_numbers = "1", []
    while(d):
        d = input('enter a number or Enter to finish: ')
        if len(d) > 0:
            try:
                list_numbers.append(int(d))
            except ValueError:
                print("you need to input only int")
    tuple_res = calculate(list_numbers)
    print('numbers: ', tuple_res[0])
    print('count = %s sum = %s lowest = %s highest = %s mean = %s middle = %s'
          % (tuple_res[1:]))
