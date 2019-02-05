#!/bin/env python3

import threading
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as mplb
import progressbar
import download_files
from generators import *
from functions import *

# these values were picked up
MAXEL = 186085  # 186085
MAXVAL = 203530  # 203530
actors_gen = actors_generator()


def thread(my_func):
    """
    function -> new_thread_function
    function-declaration to make new threads from other functions
    """

    def wrapper(*args, **kwargs):
        new_thread = threading.Thread(target=my_func, args=args, kwargs=kwargs)
        new_thread.start()

    return wrapper


def processing_actors(film_code):
    """
    string -> list
    :return: list of all actors from needed film

    function of processing - take film code and return list of all actors in
    this film
    """
    global actors_gen
    result = []
    actor = next(actors_gen)
    while int(actor[1][0][2:]) <= int(film_code[2:]):
        if (int(actor[1][0][2:]) == int(film_code[2:]) and
                int(actor[0][0][2:]) == int(film_code[2:])):
            result.append(actor[0][1])
        actor = next(actors_gen)
    result.append(actor[0][1])
    return result


@thread
def add_on_graph(ax, x_coor, y_coor, z_coor):
    """
    object, int, int, int -> None

    :param ax: subplot from matplotlib - field where situated result`s dots
    :param x_coor: x coordinate of dot
    :param y_coor: y coordinate of dot
    :param z_coor: z coordinate of dot

    function to take the dot and put it on the field
    """
    tmp_year, tmp_age, colour = y_coor // 1000, x_coor // 1000, "g"
    tmp_array_of_colors = [(1910, "#1218ac"),
                           (1920, "#2249ac"),
                           (1930, "#2a7fac"),
                           (1940, "#3cac9e"),
                           (1950, "#42ac63"),
                           (1960, "#1cac12"),
                           (1970, "#9aac38"),
                           (1980, "#ac8112"),
                           (1990, "#99512d"),
                           (2000, "#ce4e50"),
                           (2010, "#d34c8e"),
                           (2020, "#ac0013")]
    for each in tmp_array_of_colors:
        if each[0] > tmp_year:
            colour = each[1]
            break
    ax.scatter(x_coor, y_coor, z_coor, s=1, c=colour, marker=".")


def main():
    """
    main function of program
    """
    print("Preparing....")
    actors_dates = generate_actors_birthdays_list()
    film_gen, rating_gen = film_year_generator(), ratings_generator()
    film, rating, result, bar_counter = next(film_gen), next(rating_gen), [], 0
    newbar = progressbar.ProgressBar(max_value=MAXEL, prefix="Main program...")
    fig = mplb.figure()
    ax = fig.add_subplot(111, projection='3d')
    result = []
    for i in range(MAXVAL):
        while film[0] != rating[0]:
            if film[0] > rating[0]:
                rating = next(rating_gen)
            else:
                film = next(film_gen)
        film_rating_year = (film[0],
                            rating[1],
                            film[1])
        film, rating = next(film_gen), next(rating_gen)
        actors = processing_actors(film_rating_year[0])
        if len(actors) == 0:
            continue
        array_of_ages = []
        for each in actors:
            tmp = bin_search(each,
                             actors_dates)
            if tmp:
                array_of_ages.append(tmp[1])
            else:
                continue
        if len(array_of_ages) == 0:
            continue
        middle_value_of_age = year_counter(array_of_ages,
                                           int(film_rating_year[2]))
        try:
            add_on_graph(ax,
                         int(middle_value_of_age) * 1000,
                         int(film_rating_year[2]) * 1000,
                         int(film_rating_year[1] * 10) * 1000)
            result.append((str(middle_value_of_age),
                           str(film_rating_year[2]),
                           str(film_rating_year[1])))
        except TypeError:
            continue
        bar_counter += 1
        newbar.update(bar_counter)
    a = input("\nDo you want to display results?(y/n): ")
    if a == "y":
        a = input("Do you want to take it in graphic(1), file(2) or in "
                  "terminal?(3)")
        if a == '1':
            a = input("Do you want to continue? "
                      "It can take a lot of RAM (about 8Gb) and about "
                      "half of hour. (y/n): ")
            if a == 'y':
                print("Loading...")
                ax.set_xlabel('average age multiplied by 1000')
                ax.set_ylabel('film year production multiplied by 1000')
                ax.set_zlabel('film rating multiplied by 10000')
                mplb.show()
        elif a == '2':
            with open("h4_result.csv", 'w') as ress:
                for each in result:
                    print(",".join(each), file=ress)
            print("Results successfully writen.")
        elif a == '3':
            for each in result:
                print(",".join(each))
    print("Good bye!")


if __name__ == "__main__":
    urls = ["https://datasets.imdbws.com/title.principals.tsv.gz",
            "https://datasets.imdbws.com/name.basics.tsv.gz",
            "https://datasets.imdbws.com/title.basics.tsv.gz",
            "https://datasets.imdbws.com/title.ratings.tsv.gz"]
    a = input("Do you want to download needed files? (y/n): ")
    if a == "y":
        download_files.download_using_url(urls)
    main()
