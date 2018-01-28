
from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY, 'r') as (file):
        word_list = [ word.strip() for word in file.readlines() ]
    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    value = sum([ LETTER_SCORES[letter.upper()] for letter in word if letter.isalpha() ])
    return value


def max_word_value(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    words = words if words else load_words()
    value = 0
    maxw = ''
    for word in words:
        wordVal = calc_word_value(word)
        if wordVal > value:
            value = wordVal
            maxw = word

    return maxw


if __name__ == '__main__':
    pass