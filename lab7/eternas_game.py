import random


def board_generation():
    """
    () -> list

    Generates a game board of 16 x 4 size,
    i.e. two dimensional list (array) of
    'g's, 'w's and '0's  that is used for the game.

    # 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0, 0, 0, 0],
    [0, 0, 0, 'w'],
    [0, 0, 'g', 'g'],
    [0, 0, 'g', 'g'],
    [0, 'w', 'w', 'w'],
    [0, 0, 'w', 'g'],
    [0, 0, 0, 'g'],
    [0, 0, 'g', 'w'],
    [0, 'g', 'g', 'w'],
    [0, 0, 0, 0],
    ['w', 'g', 'w', 'w'],
    [0, 0, 0, 'g'],
    [0, 0, 0, 'g'],
    ['w', 'g', 'g', 'w'],
    [0, 'w', 'w', 'w'],
    [0, 0, 'g', 'w']]

    """
    def create_line():
        '''
        () -> list

        Return random generated line for the field
        '''
        result = ""
        while len(result) < 4:
            r = random.randint(0, 2)
            if ((len(result) > 0) and (result[-1] == "0")):
                break
            else:
                if (r == 0):
                    result += "0"
                elif (r == 1):
                    result += "w"
                elif (r == 2):
                    result += "g"

        while len(result) < 4:
            result += "0"
        result = list(result[::-1])
        for each in range(4):
            if result[each] == "0":
                result[each] = 0
        return result
    res = []
    for each in range(16):
        res.append(create_line())
    return res

for each in range(10):
    print(board_generation())


def winning_combination(board):
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning positions
    if there is winning combination or False if not.

    [
        ["g",   'W',     'g',   'g'],
        ['W',   'g',     'w',   'w'],
        [0,      0,      'g',   'w'],
        [0,      0,       0,     0],
        [0,      0,       0,    'g'],
        [0,      0,      'w',   'w'],
        ['w',   'g',     'g',   'G'],
        [0,      0,       0,    "G"],
        [0,      0,      'G',   'G'],
        [0,     'G',     'g',   'G'],
        ['G',   'w',     'w',   'G'],
        [0,     'g',     'w',   'w'],
        [0,      0,       0,     0],
        [0,      0,      'g',   'g'],
        [0,      0,       0,    'W'],
        ["g",   "g",     'W',   'g']
    ]

    There are four winning combinations (write in capital letters):
    [[(0, 1), (1, 0), (2, 15), (3, 14)],
    [(3, 6), (3, 7), (3, 8), (3, 9)],
    [(0, 10), (1, 9), (2, 8), (3, 7)]]

    >>> winning_combination([[0, 'g', 'g', 'g'], [0, 'g', 'w', 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 'g', 'g', 'g'], ['w', 'g', 'w', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], ['g', 'g', 'g', 'w'], [0, 0, 'w', 'g'], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], ['w', 'g', 'g', 'g'], ['w', 'w', 'g', 'w'], [0, 0, 0, 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 'g', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 'g', 'w', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w'], ['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], ['g', 'g', 'g', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'g'], [0, 0, 'w', 'w'], [0, 'w', 'w', 'g'], ['g', 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'w']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 'w', 'g'], ['g', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], ['g', 'w', 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g']])
    (True, [[(3, 7), (3, 8), (3, 9), (3, 10)]])
    >>> winning_combination([['g', 'w', 'w', 'w'], [0, 'g', 'g', 'w'], [0, 0, 'w', 'w'], [0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 'w', 'w', 'w'], ['w', 'w', 'w', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'g', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 'g', 'w']])
    (True, [[(3, 14), (3, 15), (3, 0), (3, 1)], [(3, 15), (3, 0), (3, 1), (3, 2)], [(3, 0), (3, 1), (3, 2), (3, 3)]])
    >>> winning_combination([[0, 0, 'w', 'g'], ['g', 'w', 'g', 'w'], [0, 0, 'g', 'g'], [0, 0, 'g', 'w'], ['w', 'w', 'g', 'w'], ['w', 'g', 'w', 'w'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'w', 'w'], [0, 0, 'w', 'w'], [0, 0, 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], [0, 0, 'w', 'w'], [0, 0, 0, 0], [0, 'w', 'w', 'w']])
    (True, [[(2, 1), (2, 2), (2, 3), (2, 4)], [(3, 8), (3, 9), (3, 10), (3, 11)], [(3, 9), (3, 10), (3, 11), (3, 12)], [(3, 10), (3, 11), (3, 12), (3, 13)]])
    >>> winning_combination([['g', 'g', 'w', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'w'], [0, 0, 'w', 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], ['w', 'g', 'w', 'g'], [0, 'w', 'g', 'g'], [0, 'w', 'w', 'w'], [0, 0, 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 0, 'w', 'g'], [0, 0, 0, 'g']])
    (True, [[(0, 8), (1, 9), (2, 10), (3, 11)], [(3, 12), (3, 13), (3, 14), (3, 15)]])

    """
    combinations = []
    lines = [0, 15, 14, 13]
    for each in range(16):
        list_ = [
            board[each],
            board[each - 1],
            board[each - 2],
            board[each - 3]
        ]
        '''
        counter contained count of occurrence each combination on the list_
        '''
        counter = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
        for i in range(4):
            counter[0] = [0, 0]
            for j in range(4):
                if (list_[i][j] == "w"):
                    counter[0][0] += 1
                elif (list_[i][j] == "g"):
                    counter[0][1] += 1
                if ((i == j)):
                    if (list_[i][j] == "w"):
                        counter[1][0] += 1
                    elif(list_[i][j] == "g"):
                        counter[1][1] += 1
                if (i + j == 3):
                    if (list_[i][j] == "w"):
                        counter[2][0] += 1
                    elif(list_[i][j] == "g"):
                        counter[2][1] += 1
                for smth in range(4):
                    if (j == smth):
                        if (list_[i][smth] == "w"):
                            counter[smth + 3][0] += 1
                        elif(list_[i][smth] == "g"):
                            counter[smth + 3][1] += 1
            '''
            after formating list of occurrence, we parse it
            and check if there are any win combinations
            '''
            if ((counter[0][0] == 4 or
                 counter[0][1] == 4) and
                (not ([(0, lines[i]),
                       (1, lines[i]),
                       (2, lines[i]),
                       (3, lines[i])] in combinations))):
                combinations.append([(0, lines[i]),
                                     (1, lines[i]),
                                     (2, lines[i]),
                                     (3, lines[i])])
            if (counter[1][0] == 4 or
                    counter[1][1] == 4):
                combinations.append([(0, lines[i - 3]),
                                     (1, lines[i - 2]),
                                     (2, lines[i - 1]),
                                     (3, lines[i])])
            if (counter[2][0] == 4 or
                    counter[2][1] == 4):
                combinations.append([(0, lines[i]),
                                     (1, lines[i - 1]),
                                     (2, lines[i - 2]),
                                     (3, lines[i - 3])])
            for smth in range(4):
                if (counter[smth + 3][0] == 4 or counter[smth + 3][1] == 4):
                    combinations.append([(smth, lines[i]),
                                         (smth, lines[i - 1]),
                                         (smth, lines[i - 2]),
                                         (smth, lines[i - 3])])
        for each in range(4):
            if (lines[each] == 15):
                lines[each] = 0
            else:
                lines[each] += 1
    if (len(combinations) > 0):
        result = (True, combinations)
    else:
        result = False
    return result


import doctest
doctest.testmod()
# print(board_generation())
# print(winning_combination(board_generation()))
# print(winning_combination(([[0, 0, 'w', 'g'],
#                             ['g', 'w', 'g', 'w'],
#                             [0, 0, 'g', 'g'],
#                             [0, 0, 'g', 'w'],
#                             ['w', 'w', 'g', 'w'],
#                             ['w', 'g', 'w', 'w'],
#                             [0, 0, 0, 0],
#                             [0, 0, 0, 'g'],
#                             [0, 0, 'w', 'w'],
#                             [0, 0, 'w', 'w'],
#                             [0, 0, 'w', 'w'],
#                             [0, 0, 0, 'w'],
#                             [0, 0, 0, 'w'],
#                             [0, 0, 'w', 'w'],
#                             [0, 0, 0, 0],
#                             [0, 'w', 'w', 'w']])))
# print(winning_combination([['g', 'g', 'w', 'w'],
#                            [0, 0, 'g', 'w'],
#                            [0, 0, 0, 'g'],
#                            [0, 0, 0, 'w'],
#                            [0, 0, 'w', 'w'],
#                            [0, 0, 'g', 'g'],
#                            [0, 0, 0, 'w'],
#                            [0, 0, 'g', 'g'],
#                            ['w', 'g', 'w', 'g'],
#                            [0, 'w', 'g', 'g'],
#                            [0, 'w', 'w', 'w'],
#                            [0, 0, 'w', 'w'],
#                            [0, 0, 0, 'g'],
#                            [0, 0, 0, 'g'],
#                            [0, 0, 'w', 'g'],
#                            [0, 0, 0, 'g']]))
