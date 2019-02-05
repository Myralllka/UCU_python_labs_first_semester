last_actor_number = ("tt0000001", "nm1588970")
MAXRATING = 1.0


def film_year_generator():
    """
    generator of films and their years
    generate tuple with parameters (film_number, year_of_production)
    """
    with open("title.basics.tsv", "r") as title_file:
        for each in title_file.readlines():
            smth = each.split("\t")
            if smth[1] == "movie" and smth[5] != "\\N":
                smth = (smth[0], smth[5])
                yield smth


def ratings_generator():
    """
    generator of films and their rating
    generate tuple with parameters (film_number, rating_number)
    """
    with open("title.ratings.tsv", "r") as title_file:
        for each in title_file.readlines()[1:]:
            smth = each.split("\t")
            if float(smth[1]) > MAXRATING:
                smth = (smth[0], float(smth[1]))
                yield smth


def actors_generator():
    """
    generator of film`s actors
    generate tuple with parameters ((film_number, actor_number),
    (last_film_number, last_actor_number))
    """
    global last_actor_number
    with open("title.principals.tsv", "r") as title_file:
        for each in title_file.readlines()[2:]:
            smth = each.split("\t")
            smth = (smth[0], smth[2])
            last = last_actor_number
            last_actor_number = smth
            yield (last, smth)
