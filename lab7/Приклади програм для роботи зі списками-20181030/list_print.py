# Print lists of list on one per row.


def max_item_length(listx):
    '''
    (list) -> (int)
    Return maximum length of the string representation of any item
    in the list
    '''
    max_len = 0
    rows = len(listx)
    cols = len(listx[0])
    for row in range(rows):
        for col in range(cols):
            max_len = max(max_len, len(str(listx[row][col])))
    return max_len


def print_list(listx):
    '''
    (list) -> None
    Print lists of list on one per row.
    '''
    if (listx == []):
        # corect work with listx[0]
        print([])
        return
    rows = len(listx)
    cols = len(listx[0])
    field_len = max_item_length(listx)
    print("[ ", end="")
    for row in range(rows):
        if (row > 0):
            print("\n  ", end="")
        print("[ ", end="")
        for col in range(cols):
            if (col > 0):
                print(", ", end="")
            # The next lines print listx[row][col] with the given field_width
            field_width = field_len - len(str(listx[row][col]))
            print(' ' * field_width, "{}".format(str(listx[row][col])), end="")
        print(" ]", end="")
    print("]")

list1 = [["Luke", "Skywalker", 172],
         ["Han", "Solo", 185],
         ["Darth", "Vader", 188]]

print_list(list1)
