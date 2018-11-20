import doctest
import math


def four_line_area(k1, c1, k2, c2, k3, c3, k4, c4):
    '''
    (8 numbers) -> number
    Return area of quadrangle sated by four lines
    '''
    '''
    search if you have three or more parralel lines
    '''
    if (k1 == k2) and (k2 == k3) or \
            (k1 == k2) and (k2 == k4) or \
            (k3 == k4) and (k1 == k3) or \
            (k2 == k3) and (k3 == k4):
        return ("You have three or more parallel lines")
    kes, ces = [k1, k2, k3, k4], [c1, c2, c3, c4]
    '''
    search if your lines crossed in one dot
    '''
    for i in ces:
        count = 0
        for j in ces:
            if (i == j):
                count += 1
        if (count > 2):
            return ("Three or more of your lines crossed in same dot")

    def make_list_of_dots():
        '''
        using arrays kes & ces return list of all dots
        '''
        nonlocal kes, ces, dots
        dots = []
        for i in range(4):
            for j in range(i + 1, 4):
                if (kes[i] == kes[j] and ces[i] == ces[j]):
                    continue
                if line_intersection(kes[i], ces[i], kes[j], ces[j]):
                    dots.append(line_intersection(
                        kes[i], ces[i], kes[j], ces[j]))
        return(dots)

    def is_on_same_line(x1, y1, x2, y2):
        '''
        return if dots are on the same line
        '''
        nonlocal kes
        nonlocal ces
        for each in range(4):
            # print(kes[each] * x1 + ces[each], "\r", y1, end="")
            # print(kes[each] * x2 + ces[each], "\r", y2, end="")
            if (round(kes[each] * x1 + ces[each], 2) == y1 and
                    y2 == round(kes[each] * x2 + ces[each], 2)):
                return (True)

    dots = make_list_of_dots()

    for each in range(4):
        count_top = 0
        count_down = 0
        for dot in dots:
            if (dot[1] > round((round(kes[each] * dot[0], 2) + ces[each]), 2)):
                print((str(dot[1]), ">", str(kes[each]),
                       "*", str(dot[0]), "+", str(ces[each])))
                count_top += 1
            elif (dot[1] < round((round(kes[each] * dot[0], 2) + ces[each]), 2)):
                count_down += 1
                print((str(dot[1]), "<", str(kes[each]),
                       "*", str(dot[0]), "+", str(ces[each])))
            else:
                print((str(dot[1]), "=", str(kes[each]),
                       "*", str(dot[0]), "+", str(ces[each])))
                continue
        if (count_down <= 1):
            for dot in dots:
                if (dot[1] < kes[each] * dot[0] + ces[each]):
                    dots.remove(dot)
        if (count_top >= 1):
            for dot in dots:
                if (dot[1] > kes[each] * dot[0] + ces[each]):
                    dots.remove(dot)

    list_of_distances = []
    pairs = []

    # for i in range(len(dots)):
    #     for j in range(i, len(dots)):
    #         if (i == j):
    #             continue
    #         elif is_on_same_line(dots[i][0],
    #                              dots[i][1],
    #                              dots[j][0],
    #                              dots[j][1]):
    #             list_of_distances.append(distance(dots[i][0],
    #                                               dots[i][1],
    #                                               dots[j][0],
    #                                               dots[j][1]))
    #             pairs.append((dots[i][0],
    #                           dots[i][1],
    #                           dots[j][0],
    #                           dots[j][1]))

    # list_of_rubish = []

    # for each in range(len(list_of_distances)):
    #     for each1 in range(len(list_of_distances)):
    #         for each2 in range(len(list_of_distances)):
    #             if (each == each1 or each1 == each2 or each == each2):
    #                 continue
    #             else:
    #                 if (round(list_of_distances[each]) +
    #                         round(list_of_distances[each1]) ==
    #                         round(list_of_distances[each2])):
    #                     if not(each2 in list_of_rubish):
    #                         list_of_rubish.append(each2)
    # print((list_of_distances[0], list_of_distances[1], list_of_distances[4]))
    return (dots)


def line_intersection(a1, b1, a2, b2):
    '''
    (4 numbers) -> tuple (x, y) # coordinates
    Return tuple - coordinates of dot where lines crossed
    >>> line_intersection(1, 0, 0, 1)
    (1.0, 1.0)
    '''
    if (a1 - a2 == 0):
        return None
    x = (b2 - b1) / (a1 - a2)
    return (round(x, 2), round(a1 * x + b1, 2))


def distance(x1, y1, x2, y2):
    '''
    (4 numbers) -> float # distance
    Return distance between two dots
    #>>> distance(2, 2, 6, 2)
    #4.0
    #>>> distance(1, 6, 1, 3)
    #3.0
    '''
    return (round((math.sqrt((x2 - x1)**2 + (y2 - y1)**2)), 2))


def quadrangle_area(a, b, c, d, f1, f2):
    '''
    (6 numbers) -> float # area
    Return area of sated quadrangle
    >>> quadrangle_area(4, 4, 4, 4, math.sqrt(32), math.sqrt(32))
    16.0
    >>> quadrangle_area(6, 3, 6, 3, round(math.sqrt(45), 2), \
    round(math.sqrt(45), 2))
    18.0
    '''
    try:
        f1, f2 = round(f1**2), round(f2**2)
        a, b, c, d = a**2, b**2, c**2, d**2
        return round(math.sqrt((4 * f1 * f2 - (b + d - a - c)**2) / 16), 2)
    except ValueError:
        return None


doctest.testmod()


# print(four_line_area(4, 8, 1, 1, -5, 4, -1, 10))
print(four_line_area(1, 0, -0.5, 5, 2, -6, -1, 3))
