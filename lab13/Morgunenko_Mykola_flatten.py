def flatten(in_array):
    """
    recursion function that make list linear, (without lists inside)

    :param in_array: any type (list recommended)
    :return: inline-list (or element if input id not the list)

    examples:

    flatten([1,[2]]) -> returns [1,2]
    flatten([1,2,[3,[4,5],6],7]) -> returns [1,2,3,4,5,6,7]
    flatten(['wow', [2,[[]]], [True]]) -> returns ['wow', 2, True]
    flatten([]) -> returns []
    flatten([[]]) -> returns []
    flatten(3) -> returns 3 (not a list)
    """
    res = []
    if type(in_array) != list:
        return in_array
    for each in in_array:
        if type(each) == list:
            res.extend(flatten(each))
        else:
            res.append(each)
    return res
