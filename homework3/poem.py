#!/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys


def generate_text(N, articles, nouns, verbs, adjectives):
    '''
    (None) -> string

    Return random generated poem from five lines

    >>> random.seed(1)
    >>> generate_text(5, ['the', 'a', 'my', 'his', 'her', 'its', 'our', 'your'], ['cat', 'dog', 'pig', 'mouse', 'boy','mother', 'father', 'woman', 'man'], ['sang', 'run', 'swim', 'born', 'heard', 'listen', 'talk'], ['well', 'bad', 'slow', 'hard', 'loud', 'fine', 'wonderful'])
    'her dog born bad\\nyour father talk\\nyour cat talk bad\\nthe woman swim\\na mother sang fine\\n'
    '''
    result = ''

    for i in range(N):
        adj = " " + random.choice(adjectives)
        if (random.randint(0, 1)):
            adj = ""
        result += random.choice(articles) + " " + random.choice(nouns) + \
            " " + random.choice(verbs) + adj + '\n'
    return result


if __name__ == '__main__':
    articles = ['the', 'a', 'my', 'his', 'her', 'its', 'our', 'your']
    nouns = ['cat', 'dog', 'pig', 'mouse', 'boy',
             'mother', 'father', 'woman', 'man']
    verbs = ['sang', 'run', 'swim', 'born', 'heard', 'listen', 'talk']
    adjectives = ['well', 'bad', 'slow', 'hard', 'loud', 'fine', 'wonderful']
    try:
        N = int(sys.argv[1])
    except IndexError:
        N = 5
    # import doctest
    # doctest.testmod()
    print(generate_text(N, articles, nouns, adjectives, verbs))
