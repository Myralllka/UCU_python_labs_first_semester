import time


def film_analysis():
    """
    None -> None

    Main function of our program
    """
    print_intro()
    keywords, film_keywords = input_from_file()
    keyw1, keyw2 = freq_keywords(keywords)
    number_films = (lambda a, b, c: sum([len(a[b]), len(a[c])]))(
        film_keywords, keyw1, keyw2)
    print_report(number_films, keyw1, keyw2)


def print_intro():
    '''
    None -> None

    Pprint Introduction functions
    '''
    print("This program find number of films")
    print("that use two keywords with maximal frequency.")
    print("This program use data from imdb database file keywords.list.")


def input_from_file():
    """
    None - list, dict

    Returns the list of tuple and dictionary
    """
    file_name = input("Please type the file name and path to file if need: ")
    # file_name = 'keywords.list'
    f = open(file_name, encoding='utf-8', errors='ignore')
    data = f.readline()
    keywords = []
    while not data.startswith("   keywords in use:"):
        data = f.readline()
    while not data.startswith("5: Sub"):
        data = f.readline().strip()
        keywords.append(data.split('\t'))

    keywords = [(int(w.split()[1][1:-1]), w.split()[0])
                for lst1 in keywords[:-1] for w in lst1 if w]

    while not data.startswith("8: THE"):
        data = f.readline()

    film_keywords = {}
    for line in f:
        line = line.strip().split('\t')
        film, keyword = line[0], line[-1]
        if keyword not in film_keywords:
            film_keywords[keyword] = [film]
        else:
            film_keywords[keyword].append(film)

    def gen_film_keyword(film_dict):
        '''
        (dict) -> generator

        Return generator of items from film_dict
        '''
        yield (film_dict[each] for each in film_dict)

    return keywords, film_keywords


def freq_keywords(keywords):
    """

    Find and return two keywords
    (find the indexes of two maximum items in the tuple list)
    """

    return (keywords[find_two_biggest1(keywords)[0]][1],
            keywords[find_two_biggest1(keywords)[1]][1])


def find_two_biggest1(lst):
    """ (list of tuple) -> tuple of (int, int)
    Return a tuple of the indices of the two tuple with biggest first values 
    in list lst.
    >>> find_two_biggest3([(1, '102-convictions'), 
                                                    (1, '102-pushups'), 
                                                    (3, '1020s'), 
                                                    (1, '102nd-century'), 
                                                    (2, '102nd-street-manhattan-new-york-city')])
    (2, 4)
    """
    # Keep track of the indices of the two biggest values found so far
    # Examine each first tuple value in the list in order
    # Update these values when a new biggest value is found
    # Return the two indices
    # Set max1 and max2 to the indices of the biggest and next-biggest
    # Values at the beginning of lst
    max1, max2 = 1, 0
    if lst[0] > lst[1]:
        max1, max2 = 0, 1
    # Examine each value in the list in order
    for i in range(2, len(lst)):
        # lst[i] is bigger than both max1 and max2, in between, or
        # smaller than both:
        # If lst[i] is bigger than max1 and max2, update them both
        # If lst[i] is in between, update max2
        # If lst[i] is smaller than both max1 and max2, skip it
        if lst[i] > lst[max1]:
            max2 = max1
            max1 = i
        elif lst[i] > lst[max2]:
            max2 = i
    return (max1, max2)


def print_report(number_films, keyw1, keyw2):
    """
    (int, list, list) -> None

    Print a report on the number of films
    """
    print("\nFilms analysis result")
    print("Keywords {0} and {1} are using".format(keyw1, keyw2))
    print("in {0} films".format(number_films))


if __name__ == '__main__':
    time1 = time.time()
    film_analysis()
    time2 = time.time()
    print(time2 - time1)
