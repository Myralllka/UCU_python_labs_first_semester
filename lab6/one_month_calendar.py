'''
url in description was crashed so i use this one
https://www.e-reading.club/chapter.php/1047250/60/Bendzhamin_-_Magiya_chisel._Mentalnye_vychisleniya_v_ume_i_drugie_matematicheskie_fokusy.html
'''


def weekday_by_number(number):
    """
    (int) -> str

    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [1, 7]

    >>> weekday_by_number(3)
    'wed'
    """
    week = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return week[number - 1]


def month_by_number(number):
    '''
    (int) -> str

    number: an integer in range[1, 12]
    Return a string representing a month

    '''
    monthes = [
        "January",
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    return monthes[number - 1]


def get_weekday(date):
    """
    (str) -> int
    Return an integer representing a weekday(0 represents Monday and so on)
    date : a string of form "day.month.year"
    if the date is invalid raises AssertionError with corresponding message

    >>> get_weekday("12.08.2015")
    2
    >>> get_weekday("28.02.2016")
    6
    """
    assert (date[2] == "." or date[5] == "."), \
        "day must be in form 'day.month.year'"
    assert (int(date[3:5]) <= 12 or date == "0"), \
        "not right month, it must be in range(1-12)"

    def is_lips():
        '''
        (None) -> bool

        return if year is lisp or not
        '''
        lvar = int(date[6:])
        return (((lvar % 4 == 0) and
                 (not (lvar % 100 == 0))) or (lvar % 400 == 0))

    def month_code(var):
        '''
        (int) -> int

        return code of the month
        '''
        var = int(var)
        if is_lips():
            codes = [5, 1, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        else:
            codes = [6, 2, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        return (codes[var - 1])

    def year_code(var):
        '''
        (int) -> int

        Return code of the year
        '''
        var = int(var)

        if (var > 2400):
            var = (var % 400) + 2000
        else:
            while (var < 2000):
                var += 400
        code = (((var % 100) // 4) + var % 100) % 7
        if (var > 2100) and (var < 2200):
            code += 5
        elif (var > 2200) and (var < 2300):
            code += 3
        elif (var > 2300) and (var < 2400):
            code += 1
        return code % 7

    weekday = (int(month_code(date[3:5])) +
               year_code(int(date[6:])) +
               int(date[:2])) % 7
    if (weekday == 0):
        return 7
    return weekday


def get_calendar(month, year, orientation):
    """
    (int, int, str) -> str

    Return a string representing a calendar for given month and year

    month : an integer in range[1 , 12]
    year : an integer (strictly speaking the algorithm in getWeekday works
    orientation: horizontal, vertical
    correctly only for Gregorian calendar, so year must be greater
    than 1583)
    when arguments are invalid raises AssertionError with corresponding message

    """
    assert (year > 1583), "not a Gregorian calendar year"
    assert not ((int(month) < 0) or (int(month) > 12)), "not a month"
    assert (orientation != "horizontal" or
            orientation != "vertical"), \
        "incorrect orientation"

    def make_same_len(lst):
        '''
        (list) -> list

        Return array with same number of elements in each element
        '''
        for i in lst:
            for j in lst:
                if len(i) != len(j):
                    if(len(i) > len(j)):
                        j.append(0)
                    else:
                        i.append(0)
        return lst

    def print_vertical_cal(lst_of_days, month, year, checker):
        '''
        (list, int, int, int) -> str

        list - array of dates by weeks
        month - number of the month MM
        year - number of the year YYYY
        checker - number of needed sqr`s for calendar
        Return vertical calendar, like this

        ╭───────────────────────────╮
        │            2018           │
        │          NOVEMBER         │
        │                           │
        │MON│TUE│WED│THU│FRI│SAT│SUN│
        ├ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┤
        │   │   │   │  1│  2│  3│  4│
        ├───┼───┼───┼───┼───┼───┼───┤
        │  5│  6│  7│  8│  9│ 10│ 11│
        ├───┼───┼───┼───┼───┼───┼───┤
        │ 12│ 13│ 14│ 15│ 16│ 17│ 18│
        ├───┼───┼───┼───┼───┼───┼───┤
        │ 19│ 20│ 21│ 22│ 23│ 24│ 25│
        ├───┼───┼───┼───┼───┼───┼───┤
        │ 26│ 27│ 28│ 29│ 30│   │   │
        ╰───┴───┴───┴───┴───┴───┴───╯

        ╭───────────────────────────╮
        │            2018           │
        │          DECEMBER         │
        │                           │
        │MON│TUE│WED│THU│FRI│SAT│SUN│
        ├ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┤
        │   │   │   │   │   │  1│  2│
        ├───┼───┼───┼───┼───┼───┼───┤
        │  3│  4│  5│  6│  7│  8│  9│
        ├───┼───┼───┼───┼───┼───┼───┤
        │ 10│ 11│ 12│ 13│ 14│ 15│ 16│
        ├───┼───┼───┼───┼───┼───┼───┤
        │ 17│ 18│ 19│ 20│ 21│ 22│ 23│
        ├───┼───┼───┼───┼───┼───┼───┤
        │ 24│ 25│ 26│ 27│ 28│ 29│ 30│
        ├───┼───┼───┼───┼───┼───┼───┤
        │ 31│   │   │   │   │   │   │
        ╰───┴───┴───┴───┴───┴───┴───╯

        ╭───────────────────────────╮
        │            2021           │
        │          FEBRUARY         │
        │                           │
        │MON│TUE│WED│THU│FRI│SAT│SUN│
        ├ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┤
        │  1│  2│  3│  4│  5│  6│  7│
        ├───┼───┼───┼───┼───┼───┼───┤
        │  8│  9│ 10│ 11│ 12│ 13│ 14│
        ├───┼───┼───┼───┼───┼───┼───┤
        │ 15│ 16│ 17│ 18│ 19│ 20│ 21│
        ├───┼───┼───┼───┼───┼───┼───┤
        │ 22│ 23│ 24│ 25│ 26│ 27│ 28│
        ╰───┴───┴───┴───┴───┴───┴───╯
        '''
        result = "\n" + "╭───────────────────────────╮" + "\n"

        result += '│' + str(year).center(27) + '│' + "\n"

        result += '│' + month_by_number(month).upper().center(27) + \
            '│' + "\n" + "│" + "".center(27) + "│" + "\n" + "│"

        for each in range(1, 8):
            result += weekday_by_number(each).upper() + '│'
        result += ("\n" + '├ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┼ ─ ┤' + "\n" + "│")
        counter_of_days = 1
        counter_of_weeks = 1
        weekday = 1
        while (counter_of_days <= checker):
            if (weekday == 8):
                weekday -= 7
            else:
                if (lst_of_days[weekday][counter_of_weeks - 1] == 0):
                    result += "   " + "│"
                else:
                    result += str(lst_of_days[weekday]
                                  [counter_of_weeks - 1]).rjust(3) + "│"
                weekday += 1
                if (counter_of_days % 7 == 0) and (counter_of_days != checker):
                    counter_of_weeks += 1
                    result += "\n" + "├───┼───┼───┼───┼───┼───┼───┤" + \
                        "\n" + "│"
                counter_of_days += 1
        result += "\n" + '╰───┴───┴───┴───┴───┴───┴───╯'
        return result

    def print_horizontal_cal(lst_of_days, month, year, checker):
        '''
        (list, int, int, int) -> str

        list - lst of dates by weeks
        month - number of the month MM
        year - number of the year YYYY
        checker - number of needed sqr`s for calendar
        Return horizontal calendar like this
        ╭─────────────────────────╮
        │           1650          │
        │         DECEMBER        │
        │                         │
        │  MON│   │ 5 │ 12│ 19│ 26│
        ├─ ─ ─┼───┼───┼───┼───┼───┤
        │  TUE│   │ 6 │ 13│ 20│ 27│
        ├─ ─ ─┼───┼───┼───┼───┼───┤
        │  WED│   │ 7 │ 14│ 21│ 28│
        ├─ ─ ─┼───┼───┼───┼───┼───┤
        │  THU│ 1 │ 8 │ 15│ 22│ 29│
        ├─ ─ ─┼───┼───┼───┼───┼───┤
        │  FRI│ 2 │ 9 │ 16│ 23│ 30│
        ├─ ─ ─┼───┼───┼───┼───┼───┤
        │  SAT│ 3 │ 10│ 17│ 24│ 31│
        ├─ ─ ─┼───┼───┼───┼───┼───┤
        │  SUN│ 4 │ 11│ 18│ 25│   │
        ╰─────┴───┴───┴───┴───┴───╯

        ╭─────────────────────────────╮
        │             2018            │
        │           DECEMBER          │
        │                             │
        │  MON│   │ 3 │ 10│ 17│ 24│ 31│
        ├─ ─ ─┼───┼───┼───┼───┼───┼───┤
        │  TUE│   │ 4 │ 11│ 18│ 25│   │
        ├─ ─ ─┼───┼───┼───┼───┼───┼───┤
        │  WED│   │ 5 │ 12│ 19│ 26│   │
        ├─ ─ ─┼───┼───┼───┼───┼───┼───┤
        │  THU│   │ 6 │ 13│ 20│ 27│   │
        ├─ ─ ─┼───┼───┼───┼───┼───┼───┤
        │  FRI│   │ 7 │ 14│ 21│ 28│   │
        ├─ ─ ─┼───┼───┼───┼───┼───┼───┤
        │  SAT│ 1 │ 8 │ 15│ 22│ 29│   │
        ├─ ─ ─┼───┼───┼───┼───┼───┼───┤
        │  SUN│ 2 │ 9 │ 16│ 23│ 30│   │
        ╰─────┴───┴───┴───┴───┴───┴───╯

        ╭─────────────────────╮
        │         2021        │
        │       FEBRUARY      │
        │                     │
        │  MON│ 1 │ 8 │ 15│ 22│
        ├─ ─ ─┼───┼───┼───┼───┤
        │  TUE│ 2 │ 9 │ 16│ 23│
        ├─ ─ ─┼───┼───┼───┼───┤
        │  WED│ 3 │ 10│ 17│ 24│
        ├─ ─ ─┼───┼───┼───┼───┤
        │  THU│ 4 │ 11│ 18│ 25│
        ├─ ─ ─┼───┼───┼───┼───┤
        │  FRI│ 5 │ 12│ 19│ 26│
        ├─ ─ ─┼───┼───┼───┼───┤
        │  SAT│ 6 │ 13│ 20│ 27│
        ├─ ─ ─┼───┼───┼───┼───┤
        │  SUN│ 7 │ 14│ 21│ 28│
        ╰─────┴───┴───┴───┴───╯
        '''
        result = "\n" + "╭─────" + "────" * (checker // 7) + "╮" + "\n"

        result += '│' + str(year).center(5 + 4 * (checker // 7)) + '│' + "\n"

        result += '│' + month_by_number(month).upper().center(
            5 + 4 * (checker // 7))\
            + '│' + "\n" + "│" + "".center(5 + 4 * (checker // 7)) + "│" + "\n"

        for i in range(1, len(lst_of_days)):
            result += "│" + weekday_by_number(i).rjust(5).upper() + "│"
            for j in range(len(lst_of_days[1])):
                if (lst_of_days[i][j] == 0):
                    result += " ".center(3)
                else:
                    result += str(lst_of_days[i][j]).center(3)
                result += "│"
            if (i != len(lst_of_days) - 1):
                result += "\n" + "├─ ─ ─" + "┼───" * \
                    (checker // 7) + "┤" + "\n"
            else:
                result += "\n"
        result += '╰─────' + "┴───" * (checker // 7) + '╯'

        return result

    month_str = str(month)
    if len(month_str) == 1:
        month_str = "0" + month_str

    result_month_by_days = [[], [], [], [], [], [], [], []]
    month_days_max = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    first_day_week_day = get_weekday("01" + "." + month_str + "." + str(year))
    counter_of_days = 1
    '''
    make list of dates by week days in needed month
    '''
    for i in range(1, first_day_week_day):
        result_month_by_days[i].append(0)
    while (counter_of_days <= month_days_max[month]):
        if (first_day_week_day == 8):
            first_day_week_day -= 7
        else:
            result_month_by_days[first_day_week_day].append(counter_of_days)
            first_day_week_day += 1
            counter_of_days += 1
    make_same_len(result_month_by_days)
    '''
    number of sqr - if there are 4 weeks in February
    and it starts from Monday - we need only 28 sqr`s
    in other situations we need 35 sqr`s, but there are months
    for example if it begins from Sunday often it needs 42 sqr`s.
    '''
    number_of_sqr = len(result_month_by_days[0]) * 7
    res = "_cal(result_month_by_days, month, year, number_of_sqr)"
    return eval("print_" + orientation + res)


if __name__ == '__main__':
    try:
        month = int(input("Type month: "))
        year = int(input("Type year: "))
        type_of_cal = int(
            input("Chose type of calendar \
(0-vertical, any other - horizontal): "))
        if (type_of_cal):
            type_of_cal = "horizontal"
        else:
            type_of_cal = "vertical"
        print("\n\nThe calendar is: ")
        print(get_calendar(month, year, type_of_cal))
    except ValueError as err:
        print(err)
