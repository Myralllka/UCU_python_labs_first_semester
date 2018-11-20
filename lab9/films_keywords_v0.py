# Print an Introduction
# Get the inputs from file: file_name
# Find two keywords with maximal frequency on data from input file
# Find how many films are using those keywords
# Print a report on the number of films

# First-level Design


def film_analysis():
    """

    """
    print_intro()
    keywords, film_keywords = input_from_file()
    keyw1, keyw2 = freq_keywords(keywords)
    number_films = find_films(film_keywords, keyw1, keyw2)
    print_report(number_films, keyw1, keyw2)


def print_intro():
    print("This program find number of films")
    print("that use two keywords with maximal frequency.")
    print("This program use data from imdb database file keywords.list.")


def input_from_file():
    """
    Returns the list of tuple and generator of dictionary
    """

    # file_name = input(
    # "Please type the name of file and path to file if need: ")
    file_name = 'keywords.list'
    f = open(file_name, encoding='utf-8', errors='ignore')
    data = f.readline()
    while not data.startswith("   keywords in use:"):
        data = f.readline()
    lst = []
    while not data.startswith("5: Sub"):
        data = f.readline().strip()
        lst.append(data)

    keywords = [w.split("\t") for w in lst]
    keywords = [(int(w.split()[1][1:-1]), w.split()[0])
                for lst1 in keywords[:-1] for w in lst1 if w]

    while not data.startswith("8: THE"):
        data = f.readline()

    film_keywords = {}
    for line in f:
        film, keyword = line.strip().split(
            "\t")[0], line.strip().split("\t")[-1]

        if keyword not in film_keywords:
            film_keywords[keyword] = [film]
        else:
            film_keywords[keyword].add(film)

    return keywords, film_keywords


# def freq_keywords(keywords):
#     """
#     Find and return two keywords
#     (find the indexes of two maximum items in the tuple list)
#     """
#     pass


# def find_films(film_keywords, keyw1, keyw2):
#     """
#     Return number of films that using keywords
#     """
#     pass


def print_report(number_films, keyw1, keyw2):
    """
    Print a report on the number of films
    """
    print("\nFilms analysis result")
    print("Keywords {0} and {1} are using".format(keyw1, keyw2))
    print("in {0} films".format(number_films / n))


# Second-level Design (find the indexes of two maximum items in tuple list)


def freq_keywords(keywords):
    """
    Find and return two keywords 
    (find the indexes of two maximum items in the tuple list)
    """
    keyw1 = keywords[find_two_biggest1(keywords)[0]][1]
    keyw2 = keywords[find_two_biggest1(keywords)[1]][1]

    return keyw1, keyw2

# 1. Find, remove, find. Find the index of the maximum, remove that item from
# the list, and find the index of the new maximum item in the list. After we
# have the second index, we need to put back the value we removed and,
# if necessary, adjust the second index to account for that reinsertion.
# 2. Sort, identify maximum, get indices. Sort the list, get the two biggest
# numbers, and then find their indices in the original list.
# 3. Walk through the list. Examine each first tuple value in the list in order,
# keep track of the two biggest values found so far, and update these values when a
# new biggest value is found.

# 1. Find, remove, find.


def find_two_biggest1(lst):
    """ (list of tuple) -> tuple of (int, int)
    Return a tuple of the indices of the two tuple with biggest first values 
    in list lst.
    >>> find_two_biggest([(1, '102-convictions'), 
                                            (1, '102-pushups'), 
                                            (3, '1020s'), 
                                            (1, '102nd-century'), 
                                            (2, '102nd-street-manhattan-new-york-city')])
    (2, 4)
    """
    # Find the index of the max item in lst
    # Get the max item in lst
    # Find the index of that max item
    # Remove that item from the list
    # Find the index of the new max item in the list
    # Put the biggest item back in the list
    # If necessary, adjust the second index
    # Fix max2 in case it was affected by the reinsertion:
    # If max1 comes before max2, add 1 to max2
    # Return the two indices

    # Find the index of the max and remove that item
    biggest = max(lst)
    max1 = lst.index(biggest)
    lst.remove(biggest)
    # Find the index of the new max
    next_biggest = max(lst)
    max2 = lst.index(next_biggest)
    # Put biggest back into lst
    lst.insert(max1, biggest)
    # Fix max2 in case it was affected by the reinsertion
    if max1 <= max2:
        max2 += 1

    return (max1, max2)

# 2. Sort, identify maximum, get indices.


def find_two_biggest2(lst):
    """ (list of tuple) -> tuple of (int, int)
    Return a tuple of the indices of the two tuple with biggest first values 
    in list lst.
    >>> find_two_biggest2([(1, '102-convictions'), 
                                            (1, '102-pushups'), 
                                            (3, '1020s'), 
                                            (1, '102nd-century'), 
                                            (2, '102nd-street-manhattan-new-york-city')])
    (2, 4)
    """
    # Sort a copy of lst
    # Get a sorted copy of the list so that the two biggest items
    # are at the front
    # Get the two biggest numbers
    # Find their indices in the original list lst
    # Return the two indices

    # Get a sorted copy of the list so that the two biggest items
    # are at the front
    temp_list = sorted(lst)
    biggest = temp_list[-1]
    next_biggest = temp_list[-2]
    # Find the indices in the original list L
    max1 = lst.index(biggest)
    max2 = lst.index(next_biggest)

    return (max1, max2)

# 3. Walk through the list.


def find_two_biggest3(lst):
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
    if lst[0] > lst[1]:
        max1, max2 = 0, 1
    else:
        max1, max2 = 1, 0

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


def find_films(film_keywords, keyw1, keyw2):
    """
    Return number of films that using keywords
    """
    return sum([len(film_keywords[keyw1]), len(film_keywords[keyw2])])
if __name__ == '__main__':
    film_analysis()
