def read_data(path_file):
    """
    (str) -> (list)
    Return list of sequence lines from file
    """
    f = open(path_file, 'r', encoding='utf-8')
    sequence = [w.strip() for w in f.readlines()]
    f.close()
    return sequence


def seq_stat(sequence):
    """
    (sequence) -> int, int
    Return amount sequence elements and amount sequence unique elements
    """
    return len(sequence), len(set(sequence))


def skey(item):
    """
    Return key item for sorting
    """
    return item[1]


def dict_freq(sequence):
    """
    Return sorted dict from sequence
    """

    d_freq = dict()
    for word in sequence:
        d_freq[word] = d_freq.get(word, 0) + 1

    return d_freq


def bigrams_gen(sents):
    """
    Return bigrams from sents
    """

    n = 2
    bigrams_list = []
    for sent in sents:
        sent = [s for s in sent.split() if sent.split() and s.isalpha()]
        sent_bigrams = [sent[i:i + n] for i in range(len(sent) - n + 1)]
        bigrams_list.extend(sent_bigrams)
    return [tuple(bigram) for bigram in bigrams_list]


def words_seq_gen(seed_word, n=10):
    """
    Print n words from seed word
    """

    next_word = seed_word
    while n:
        print(next_word, end=" ")
        next_x = next_word_dict.get(next_word)
        if next_x:
            next_word = sorted(next_x, key=skey, reverse=True)[0][0]
        n -= 1


tokens = read_data('Romanyuk_wordslist.txt')
sents = read_data('Romanyuk_list.txt')

tokens_stat = seq_stat(tokens)
sents_stat = seq_stat(sents)
print('''tokens in text {}
         unique tokens in text {}'''.format(tokens_stat[0], tokens_stat[1]))
print('''sents in text {}
         unique sents in text {}'''.format(sents_stat[0], sents_stat[1]))

words = [word for word in tokens if word.isalpha()]
words_stat = seq_stat(words)
print('''words in text {}
         voc of text {} '''.format(words_stat[0], words_stat[1]))

freq_words = dict_freq(words)
print('items in frequence distribution of words {}'.format(len(freq_words)))

bigrams_list = bigrams_gen(sents)
print(len(bigrams_list))
print(len(set(bigrams_list)))

bigram_dict = dict_freq(bigrams_list)

next_word_dict = {}
for i in bigram_dict:
    if i[0] not in next_word_dict:
        next_word_dict[i[0]] = [(i[1], bigram_dict[i])]
    else:
        next_word_dict[i[0]].append((i[1], bigram_dict[i]))

print(words_seq_gen('чотири', n=5))
print(words_seq_gen('сім', n=5))
print(words_seq_gen('двадцять', n=5))
