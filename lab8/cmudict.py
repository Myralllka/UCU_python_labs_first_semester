def dict_reader_tuple(dictionary_file):
    '''
    (file) -> list

    Return list of tuples of word, number of the transcription and
    the transcription list(tuples(str, int, list))
    '''
    result = []
    input_file = open(dictionary_file, 'r', encoding='utf-8')
    for each in input_file.readlines():
        each = each.split()
        word, number, *spell = each[0], each[1], each[2:]
        result.append(tuple((word, int(number), spell[0])))
    return result


def dict_reader_dict(dictionary_file):
    '''
    (file) -> dict

    Return dictionary where keys are words and values are sets of tuples of
    sounds of transcription
    '''
    result = {}
    input_file = open(dictionary_file, 'r', encoding='utf-8')
    for each in input_file.readlines():
        each = each.split()
        word, *spell = each[0], each[2:]
        spell = tuple(i for i in spell[0])
        if not (word in result.keys()):
            result[word] = set()
        result[word].add(tuple(spell))
    input_file.close()
    return result


def dict_invert(input_item):
    '''
    (item) -> dict

    Take as parameter result of dict_reader_tuple or dict_reader_dict
    and return as result dictionary where keys are number of transcriptions
    and values are set of tuples, where tuple contain word with same
    transcriptions number as a key and tuple of sounds
    '''
    def dict_invert_list(input_list):
        '''
        (list) -> dict

        Return needed dictionary if input_item is list
        '''
        result = {}
        for each in input_list:
            if not (each[1] in result.keys()):
                result[each[1]] = set()
            item1 = each[0]
            item2 = tuple(i for i in each[2])
            tuple1 = (item1, item2)
            result[each[1]].add(tuple1)
        return result

    def dict_invert_dict(input_dict):
        '''
        (dict) -> dict

        Return needed dictionary if input_item is dict
        '''
        result = {}
        for each in input_dict:
            item1 = str(each)
            item2 = tuple(i for i in input_dict[each])
            if not (len(input_dict[each])) in result.keys():
                for i in item2:
                    tuple1 = (item1, i)
                    result[len(input_dict[each])] = set(tuple1)
            else:
                for i in item2:
                    tuple1 = (item1, i)
                    result[len(input_dict[each])].add(tuple1)

            result[len(input_dict[each])].add(tuple1)
        return result

    if type(input_item) == list:
        return dict_invert_list(input_item)
    elif type(input_item) == dict:
        return dict_invert_dict(input_item)
    return None


# output_file = open("cmuout.txt", "w")
# print(dict_invert(dict_reader_dict('./lecture_materials/cmudict')), file=output_file)
# output_file.close()
