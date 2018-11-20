def common_names(female_names, male_names):
    '''
    (list, list) -> set

    Return set of both male and femail names
    '''
    return set(a for a in female_names if a in male_names)


def names_read(file_name):
    '''
    (string) -> list

    Read file with input name and return list of all strings in this file
    '''
    input_file = open(file_name, "r", encoding="utf-8")
    res = [a.replace("\n", "") for a in input_file.readlines()]
    input_file.close()
    return res
