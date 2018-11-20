import random


def generate_grid():
    """
    () -> list(list)

    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    array = [[], [], []]
    for each in array:
        for i in range(3):
            each.append(chr(random.randint(65, 90)))
    if len(get_words("en", [n.lower() for each in array for n in each])) <= 1:
        return generate_grid()
    return array


def get_words(f, letters):
    """
    (list, list) -> list()

    Checks the words with rules and returns a new list of words.
    >>> get_words('en', [el for el in 'emxpczwpi'])
    ['cimex', 'epic', 'mice', 'pice', 'wice']
    >>> get_words('en', [el for el in 'jniarnoah'])
    ['aaron', 'ahir', 'aira', 'airan', 'ajar', 'ajari', 'ajhar', 'arain', 'aria', 'arian', 'arion', 'arna', 'arni', 'aronia', 'hair', 'haori', 'harn', 'hiro', 'hoar', 'hora', 'horn', 'inro', 'iran', 'iroha', 'iron', 'jara', 'nahor', 'nair', 'noir', 'nonair', 'nora', 'norah', 'nori', 'noria', 'norn', 'norna', 'orna', 'raia', 'rain', 'raja', 'rajah', 'rana', 'rani', 'ranina', 'rann', 'rhina', 'rhino', 'roan', 'rohan', 'ronni']
    """
    def read_dict(f):
        """
        (list) -> list

        Reads the file (f) and returns a list with the words from this file.
        """
        res = []
        en = open(f, "r")
        for each in en.readlines():
            each = each.replace("\n", "")
            if ((len(each) < 10) and (len(each) > 3)):
                res.append(each.lower())
        return res

    words = read_dict(f)
    result = []
    mid = letters[4]
    for each in words:
        each = list(each)
        if each == [a for a in each if a in letters] and mid in each:
            result.append("".join(each))
    array_letters = []
    for each in result:
        if result.count(each) > 1:
            result.remove(each)
    for each in letters:
        if ((each, letters.count(each)) in array_letters):
            continue
        else:
            array_letters.append((each, letters.count(each)))
    array_letters.sort()
    for k in (result[::1]):
        res = []
        flag = False
        for each in k:
            if ((each, k.count(each)) in res):
                continue
            else:
                res.append((each, k.count(each)))
        res.sort()
        for i in array_letters:
            for j in res:
                if i[0] == j[0] and i[1] < j[1]:
                    flag = True
        if flag:
            result.remove(k)
    return result


def get_user_words():
    """
    () -> list

    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    array = []
    while (True):
        try:
            array.append(input("input here your word: "))
        except EOFError:
            return array


def get_pure_user_words(user_words, letters, words_from_dict):
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    >>> get_pure_user_words(["hal", "hello", "heyho", 'hallio', "hoil", "hlal", "halloeyihh"], list("halloeyhi"), get_words("en", list("halloeyhi")))
    ['heyho', 'hallio', 'hoil']
    """
    result = []
    mid = letters[4]
    for each in user_words:
        each = list(each)
        if each == [a for a in each if a in letters] and \
                mid in each and \
                (4 <= len(each) < 10):
            result.append("".join(each))
    array_letters = []
    for each in result:
        if result.count(each) > 1:
            result.remove(each)
    for each in letters:
        if ((each, letters.count(each)) in array_letters):
            continue
        else:
            array_letters.append((each, letters.count(each)))
    array_letters.sort()
    for k in (result[::1]):
        res = []
        flag = False
        for each in k:
            if ((each, k.count(each)) in res):
                continue
            else:
                res.append((each, k.count(each)))
        res.sort()
        for i in array_letters:
            for j in res:
                if i[0] == j[0] and i[1] < j[1]:
                    flag = True
        if flag:
            result.remove(k)
    for each in result[::1]:
        if each in words_from_dict:
            result.remove(each)
    return result


def results():
    '''
    main game
    '''
    grid = generate_grid()
    for each in grid:
        for every in each:
            print(every, end="\t")
        print("\n\n", end="\n")
    user_words = get_user_words()
    words = get_words("en", [n.lower() for each in grid for n in each])
    print()
    print("\n" + "WORDS FROM DICT".center(74) + "\n\n", end="│")
    counter = 0
    for each in words:
        if counter < 6:
            print(each.center(11), end="│")
            counter += 1
        else:
            print("\n" + "├" + "───────────┼" * 5 + "───────────┤")

            print("│", end="")
            counter = 0
    print("\n\n" + "USER WORDS".center(74) + "\n\n", end="│")
    counter = 0
    for each in user_words:
        if counter < 6:
            print(each.center(11), end="│")
            counter += 1
        else:
            print("\n" + "├" + "───────────┼" * 5 + "───────────┤")

            print("│", end="")
            counter = 0
    print("\n" + "PURE USER WORDS".center(74) + "\n\n", end="│")
    counter = 0
    for each in get_pure_user_words(user_words,
                                    [n.lower() for each in grid for n in each],
                                    words):
        if counter < 6:
            print(each.center(11), end="│")
            counter += 1
        else:
            print("\n" + "├" + "───────────┼" * 5 + "───────────┤")

            print("│", end="")
            counter = 0


# import doctest
# doctest.testmod()
if __name__ == "__main__":
    results()
