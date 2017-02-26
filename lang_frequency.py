import argparse
import os
import re
from collections import *


def load_data(filepath):
    if not os.path.exists(filepath):
        print("Incorrect path")
        exit(-1)
    with open(filepath, 'r', encoding='utf8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text, number_of_top):
    dict_counter = {}
    all_words = re.findall('([^\W\d](\w|[-\']{1,2}(?=\w))+)', text)
    for word_ in all_words:
        word = word_[0]
        dict_counter.setdefault(word, 0)
        dict_counter[word] += 1
    ordered_dict = OrderedDict(sorted(dict_counter.items(),
                               key=lambda x: x[1], reverse=True))
    ret_dict = OrderedDict()
    for word, number_of_reps in ordered_dict.items():
        ret_dict[word] = number_of_reps
        if len(ret_dict) == number_of_top:
            break
    return ret_dict



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Word frequency in text')
    parser.add_argument('filepath', metavar='filepath', type=str, nargs=1,
                        help='path to text file')
    args = parser.parse_args()
    filepath = args.filepath[0]

    text = load_data(filepath)
    number_of_top = 10
    ret_top_of_words = get_most_frequent_words(text, number_of_top)
    print('word', '( number of reps )')
    print('--------------------')
    for word, number_of_reps in ret_top_of_words.items():
        print(word, '(', number_of_reps, ')')
