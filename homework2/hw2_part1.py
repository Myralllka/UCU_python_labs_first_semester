import doctest
import string


myprog = [1, 2, 4, 7, 10, 11, 14, 15, 16, 20, 23, 24]

'''
Problem 4
mistake in spelling "obutuse triangle", i correct to "obtuse triangle"
'''


def get_number():
    number = 41
    return number


# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file.

# The doctests are just examples. Feel free to add your own doctests.

# ****************************************
# Problem 1
# ****************************************


def get_position(ch):
    """
    str -> int
    Return positon of letter in alphabet. If argument is not a letter function
    should return None.

    >>> get_position('A')
    1
    >>> get_position('a')
    1
    >>> get_position('Dj')

    >>> get_position('z')
    26
    >>> get_position('Z')
    26
    >>> get_position('3')

    >>> get_position(3)

    """
    if (str(type(ch)) != "<class 'str'>") or ch.isdigit() or (len(ch) > 1):
        return None
    ch = ch.upper()
    if (ord(ch) - 64) in range(1, 27):
        return (ord(ch) - 64)
    return (None)


# ****************************************
# Problem 2
# ****************************************


def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('d', 'ad')

    >>> compare_char('z', "2")

    >>> compare_char("V", "V")
    False
    >>> compare_char('z', 2)

    """
    if ((str(type(ch1)) != "<class 'str'>") or
            (str(type(ch2)) != "<class 'str'>")):
        return None
    if ((len(ch1) > 1) or (len(ch2) > 1)):
        return (None)
    ch1, ch2 = ch1.upper(), ch2.upper()
    ch1, ch2 = ord(ch1), ord(ch2)
    if (str(chr(ch1)).isalpha() and str(chr(ch2)).isalpha()):
        return (ch2 < ch1)
    else:
        return None


# ****************************************
# Problem 4
# ****************************************


def type_by_angles(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and
    return type as string
    ("right angled triangle", "obtuse triangle", "acute triangle").
    If there is no
    triangle with such angles, then function should return None.

    >>> type_by_angles(60, 60, 60)
    'acute triangle'
    >>> type_by_angles(90, 30, 60)
    'right angled triangle'
    >>> type_by_angles(2015, 2015, 2015)

    >>> type_by_angles(460, 60, 380)
    'obtuse triangle'
    >>> type_by_angles(0, 60, 120)

    >>> type_by_angles(-60, -60, -60)
    'acute triangle'
    """
    a, b, c = abs(a) % 360, abs(b) % 360, abs(c) % 360
    if (a + b + c != 180) or (a == 0 or b == 0 or c == 0):
        return None
    if (a == 90 or b == 90 or c == 90):
        return ("right angled triangle")
    if (a > 90 or b > 90 or c > 90):
        return ("obtuse triangle")
    else:
        return ("acute triangle")


# ****************************************
# Problem 7
# ****************************************


def convert_to_column(s):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> convert_to_column("Revenge is a dish that tastes \
best when served cold.")
    'revenge\\nis\\na\\ndish\\nthat\\ntastes\\nbest\\nwhen\\nserved\\ncold\\n'
    >>> convert_to_column("Never hate your enemies. It affects your judgment.")
    'never\\nhate\\nyour\\nenemies\\nit\\naffects\\nyour\\njudgment\\n'
    >>> convert_to_column(2015)

    """
    if (str(type(s)) != "<class 'str'>") or s.isdigit():
        return None
    s = s.lower().replace(".", "").replace(",", "").replace(" ", "\n")
    return s+"\n"

# ****************************************
# Problem 10
# ****************************************


def encrypt_message(s):
    """
    str -> str
    Replace all letters in string with next letters in aplhabet.
    If argument is not a string
    function should return None.

    >>> encrypt_message("Revenge is a dish that tastes best when served cold.")
    'Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.'
    >>> encrypt_message("Never hate your enemies. It affects your judgment.")
    'Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.'
    >>> encrypt_message(2015)

    >>> encrypt_message("2015")

    """
    if (str(type(s)) != "<class 'str'>") or s.isdigit():
        return None
    result = ""
    for each in s:
        if (each in ". "):
            result += each
            continue
        if not(each in string.ascii_letters):
            continue
        elif(each == "z"):
            result += "a"
            continue
        result += chr(ord(each) + 1)
    return result


# ****************************************
# Problem 11
# ****************************************


def decrypt_message(s):
    """
    str -> str
    Replace all letters in string with previous letters in aplhabet.
    If argument isn't a string
    function should return None.

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpmea.")
    'Revenge is a dish that tastes best when served coldz.'
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    'Never hate your enemies. It affects your judgment.'
    >>> decrypt_message(2015)

    >>> decrypt_message('2015')
    """
    if (str(type(s)) != "<class 'str'>") or s.isdigit():
        return None
    result = ""
    for each in s:
        if (each in ". "):
            result += each
            continue
        if not(each in string.ascii_letters):
            continue
        elif(each == "a"):
            result += "z"
            continue
        result += chr(ord(each) - 1)
    return (result)


# ****************************************
# Problem 14
# ****************************************


def get_letters(n):
    """
    int -> str
    Create and return string of first n letters of an alphabet.
    If arguments isn't
    positive integer number function should return None.

    >>> get_letters(0)

    >>> get_letters(1)
    'a'
    >>> get_letters(-2015)

    >>> get_letters(26)
    'abcdefghijklmnopqrstuvwxyz'
    >>> get_letters(27)

    """
    if (n not in range(1, 27)):
        return None
    alphabetca = string.ascii_lowercase[:n:]
    return alphabetca


# ****************************************
# Problem 15
# ****************************************


def find_intersection(s1, s2):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    'b'
    >>> find_intersection("aZAbc", "zzYYxp")
    'z'
    >>> find_intersection("sfdfsdf", 2015)

    """
    if ((str(type(s1)) != "<class 'str'>") or
            (str(type(s2)) != "<class 'str'>")):
        return None
    s1, s2, result = s1.lower(), s2.lower(), ""
    for each in string.ascii_lowercase:
        if (each in s1) and (each in s2) and not (each in result):
            result += each
    return result


# ****************************************
# Problem 16
# ****************************************


def find_union(s1, s2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'AYZabcpxz'
    >>> find_union("sfdfsdf", 2015)

    """
    if ((str(type(s1)) != "<class 'str'>") or
            (str(type(s2)) != "<class 'str'>")):
        return None
    s1, result = (s1 + s2), ""
    for each in (string.ascii_uppercase + string.ascii_lowercase):
        if (each in s1) and not (each in result):
            result += each
    return result


# ****************************************
# Problem 20
# ****************************************


def polynomial_eval(coefficients, value):
    """
    (list, int) -> int
    list of coefficients and value of "x"
    return calculated polynome

    >>> polynomial_eval([2,3,0,4], 4)
    180
    >>> polynomial_eval([6], 42)
    6
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """
    result, degree = 0, (len(coefficients) - 1)
    for each in coefficients:
        result += each * (value ** degree)
        degree -= 1
    return result


# ****************************************
# Problem 23
# ****************************************


def one_swap_sorting(sequence):
    """
    (list) -> bool
    return True if list can be sorted by one swap and False if it can`t

    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    False
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """
    import copy
    perm_array = copy.copy(sequence)
    sequence.sort()
    if (len(sequence) == 0) or perm_array == sequence:
        return False
    for i in range(len(sequence)):
        for j in range(len(sequence)):
            new_arr = copy.copy(perm_array)
            new_arr[i], new_arr[j] = new_arr[j], new_arr[i]
            if (new_arr == sequence):
                return True
    return False


# ****************************************
# Problem 24
# ****************************************


def numbers_Ulam(n):
    """
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    >>> numbers_Ulam(6)
    [1, 2, 3, 4, 6, 8]
    >>> numbers_Ulam(100)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126, 131, 138, 145, 148, 155, 175, 177, 180, 182, 189, 197, 206, 209, 219, 221, 236, 238, 241, 243, 253, 258, 260, 273, 282, 309, 316, 319, 324, 339, 341, 356, 358, 363, 370, 382, 390, 400, 402, 409, 412, 414, 429, 431, 434, 441, 451, 456, 483, 485, 497, 502, 522, 524, 544, 546, 566, 568, 585, 602, 605, 607, 612, 624, 627, 646, 668, 673, 685, 688, 690]
    """
    assert (n > 0), "number must be integer more than 1"
    assert (type(n) == int), "input must be integer"
    result = [1, 2]
    if (n == 1):
        return [1]
    counter_of_iter = 1
    each = result[counter_of_iter]
    while True:
        counter_of_entry = 0
        for i in range(counter_of_iter + 1):
            for j in range(i, counter_of_iter + 1):
                if ((i != j) and (result[i] + result[j] == each)):
                    counter_of_entry += 1
        if (counter_of_entry == 1):
            result.append(each)
            counter_of_iter += 1
        each += 1
        if (len(result) == n):
            return result

print (doctest.testmod())