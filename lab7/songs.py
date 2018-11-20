#!/usr/bin/env python
#coding=utf-8
# -*- coding: utf-8 -*-


def song_length(each):
    '''
    (str) -> int

    Return time of song
    >>> song_length(('Янанебібув', '3.19'))
    '3.19'
    '''
    return each[1]


def title_length(each):
    '''
    (str) -> int

    Return length of the title of inputed song
    >>> title_length(('Янанебібув', '3.19'))
    10
    '''
    return len(each[0])


def last_word(array):
    '''
    (str) -> str

    Return last word of the inputed sentence
    >>> last_word(('Той день', "3.58"))
    'д'
    >>> last_word(('Янанебібув', '3.19'))
    'я'
    '''
    return array[0].split()[-1][0].lower()


def sort_songs(song_titles, length_songs, key):
    '''
    (list, list, string) -> list
    song_titles - list of song`s names
    length_songs - list of song`s lengths
    key - "song_length" or "title_length" or "last_word"

    Return sorted list of songs during the key
    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд'], [ '3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21'], last_word)
    [('Африка', '4.24'), ('Відпусти', '3.52'), ('Той день', '3.58'), ('Етюд', '2.21'), ('Кавачай', '4.39'), ('Мало мені', '5.06'), ('Коли тебе нема', '3.17'), ('Поясни', '3.39'), ('Сосни', '4.31'), ('Фіалки', '3.43'), ('Янанебібув', '3.19')]
    '''
    if ((len(song_titles) != len(length_songs)) or
            (type(song_titles) != list or type(length_songs) != list)):
        return None
    result = []
    for each in range(len(song_titles)):
        result.append((song_titles[each], length_songs[each]))
    return (sorted(result, key=key))


array_t = [
    'Янанебібув',
    'Той день',
    'Мало мені',
    'Сосни',
    'Кавачай',
    'Відпусти',
    'Африка',
    'Поясни',
    'Фіалки',
    'Коли тебе нема',
    'Етюд'
]

array_l = [ '3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21']

print(sort_songs(array_t, array_l, last_word))
import doctest
print(doctest.testmod())
