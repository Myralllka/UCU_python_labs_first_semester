def input_from_file():
    """
    Returns the list of tuple and generator of dictionary
    """

    file_name = input("Please type the file name and path to file if need: ")
    start = []
    while True:
        starts = input("Please type the first start line symbols or Enter: ")
        if starts:
            start.append(starts[:-1])
        else:
            break
    end = []
    while True:
        ends = input("Please type the first symbols of end line or Enter: ")
        if ends:
            end.append(ends[:-1])
        else:
            break

    f = open(file_name, encoding='utf-8', errors='ignore')
    for item in zip(start, end):
        print(item)
        lst = [data for data in read_line(f, start=item[0], end=item[1])]

    keywords = [w.split("\t") for w in lst]
    keywords = [(int(w.split()[1][1:-1]), w.split()[0])
                for lst1 in keywords[:-1] for w in lst1 if w]

    film_keywords = {}
    line_strip = [data for data in read_line(f, start=start[-1])]
    for line in line_strip:
        film, keyword = line.split("\t")[0], line.split("\t")[-1]
        if keyword not in film_keywords:
            film_keywords[keyword] = [film]
        else:
            film_keywords[keyword].append(film)

    print(len(film_keywords))
    print(len(lst))
    f.close()
    return lst


def read_line(f, start=None, end=None):
    if start and end:
        data = f.readline()
        while not data.startswith(start):
            data = f.readline()

        while not data.startswith(end):
            data = f.readline().strip()
            yield data
    elif start:
        data = f.readline()
        while not data.startswith(start):
            data = f.readline()
            for line in f:
                yield line.strip()


input_from_file()
