import doctest


def dyvo_insert(sentence, flag):
    """
    (str, str) -> None

    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті.", "ки")
    'диво Кит кота по хвилях катав - диво кит у воді, кіт на диво киті.'
    """
    result = ''
    while (sentence.lower().find(flag) != -1):
        result += \
            sentence[0:sentence.lower().find(flag):] + \
            "диво " + \
            sentence[sentence.lower().find(flag)]
        sentence = sentence[sentence.lower().find(flag) + 1::]
    result += sentence
    return(result)


doctest.testmod()
