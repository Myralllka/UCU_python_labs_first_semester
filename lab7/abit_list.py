import urllib.request
import ssl


def read_input_file(url, number=77):
    """
    (str, int) -> (list(list))

    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """

    context = ssl._create_unverified_context()
    urlfile_read = urllib.request.urlopen(url, context=context)
    result = []
    for each in urlfile_read.readlines():
        each = each.decode("utf-8")
        if (each[0] == "—"):
            result[-1][result[-1].index("")] = \
                each[each.rfind("\r") - 1]
        if (each[0:2] == " С"):
            result[-1].append(each[35:]
                              .replace("\r", "")
                              .replace("\n", ""))
        if ((each[0] in "#-— ") or
                (each[0:2] == "РK") or
                (each[0:2] == "CK")):
            continue
        if (each[0].isdigit()):
            number -= 1
        if (number == -1):
            break
        result.append(each[:each.rfind("\t")]
                      .replace("\t", ",")
                      .replace("До наказу", "")
                      .replace("Рекомендовано (контракт)", "").split(","))
    return result


def write_csv_file(url):
    '''
    (string(url)) -> None

    print all information from url to .csv file "total.csv"
    '''
    each = read_input_file(url)
    out = open("total.csv", "w")
    print("№,ПІБ,Д,Заг.бал,С.б.док.осв.", file=out)
    for i in each:
        s = ","
        print(s.join(i), file=out)
    out.close()


url = 'https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt'
# res = (read_input_file(url, 5))
# for each in res:
#     print(each)
write_csv_file(url)
# print(res)
import doctest
doctest.testmod()
