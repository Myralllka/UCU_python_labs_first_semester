import progressbar


def year_counter(all_ages, film_production_year):
    """
    list, int ->
    :param all_ages:
    :param film_production_year:
    :return:
    """
    result = sum([(film_production_year - itr) for itr in all_ages]) // len(
        all_ages)
    if 100 > result > 0 and result != "one":
        return result


def bin_search(element, array_inp):
    """
    str, list -> tuple
    :param element: needed first element of searched tuple
    :param array_inp: array of tuples
    :return: needed tuple

    function to return needed element of sorted array using binary search

    >>> bin_search("nm0000007", [('nm0000001', 1899), ('nm0000002', 1924),
\('nm0000003', 1934), ('nm0000004', 1949), ('nm0000005', 1918),
\('nm0000006', 1915), ('nm0000007', 1899), ('nm0000008', 1924),
\('nm0000009', 1925), ('nm0000010', 1899)])\
('nm0000007', 1899)
    """
    left = 0
    r = len(array_inp)
    while True:
        if int(element[2:]) >= int(array_inp[(r + left) // 2][0][2:]):
            left = (r + left) // 2
        else:
            r = (r + left) // 2
        if abs(left - r) == 1:
            if (array_inp[left][0] == element and
                    array_inp[left][1] > 1800):
                return array_inp[left]
            else:
                return 0


def generate_actors_birthdays_list():
    """
    None -> tuple
    :return: list of all actors from the film

    returned tuple contained (actor_number, actor_birthday)
    """
    result = []
    bar = progressbar.ProgressBar(max_value=468900, prefix="Reading actors "
                                                           "list...")
    bar_counter = 0
    with open("name.basics.tsv", "r") as inp_file:
        for line in inp_file.readlines()[1:]:
            tmp = line.split("\t")
            if tmp[2] == "\\N":
                continue
            bar.update(bar_counter)
            bar_counter += 1
            result.append((tmp[0], int(tmp[2])))
    return result
