import copy


def input_data(path):
    """
    str -> list

    Returns the list of characters from the file.
    """
    result = []
    with open("text_1.txt", "r", encoding='utf-8') as file:
        for i in file.readlines():
            result.append(i.strip())
    return result


def column_extend(column):
    """
    list -> list

    Returns the extended column with sorted consonants without duplication.
    """
    line = 'bcdfghjklmnpqrstvwxyz'
    new_arr = [[] for i in range(len(column[0]))]
    for j in range(len(column) - 1):
        for i in range(len(column[0])):
            new_arr[i].append(column[j][i])
    for each in range(len(new_arr)):
        new_arr[each] = "".join(new_arr[each])
    new_lat_arr = copy.deepcopy(new_arr)
    for i in range(len(new_arr)):
        tmp = line
        for each in new_lat_arr[i]:
            if each in tmp:
                new_lat_arr[i] += each
                tmp = tmp[:tmp.index(each)] + tmp[tmp.index(each) + 1:]
                tmp.replace(each, '')
    return new_lat_arr


column_extend('as')


def characters_info(in_path, out_path):
    """
    str, str -> None

    The main function that reads the data from the file, processes it and 
    outputs to the other file.
    """
    lineline = input_data("text_1.txt")

    tmp = column_extend(lineline)
    for i in tmp:
        print(i)

characters_info("text_1.txt", "")
