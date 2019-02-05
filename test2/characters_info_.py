def input_data(path):
    """
    str -> list

    Returns the list of characters from the file.
    """
    result = []
    with open(path, "r", encoding='utf-8') as file:
        for i in file.readlines():
            result.append(i.strip())
    return result


def row_extend(row):
    """
    list -> list

    Returns the extended row with sorted vowels by their frequency in the row.
    """
    tmp_dict = dict()
    result = ''
    for line in row:
        tmp_line = ''
        for n in line:
            if n in tmp_dict:
                tmp_dict[n] += 1
            elif n in "euioa":
                tmp_dict[n] = 1
        for each in sorted(tmp_dict.keys()):
            tmp_line += each
        result += line + tmp_line + '\n'
    print(result[:-1])


def column_extend(column):
    """
    list -> list

    Returns the extended column with sorted consonants without duplication.
    """
    line = 'bcdfghjklmnpqrstvwxyz'
    # tmp_list
    # for line in column:
    #     for n in line:


def characters_info(in_path, out_path):
    """
    str, str -> None

    The main function that reads the data from the file, processes it and
    outputs to the other file.
    """
    with open(out_path, "w") as file:
        print(row_extend(input_data(in_path)), file=file)


a = input_data("text_1.txt")
row_extend(a)
