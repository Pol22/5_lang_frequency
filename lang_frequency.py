import sys
import os


def load_data(filepath):
    with open(filepath, 'r', encoding='utf') as file_handler:
        return file_handler.read()


def get_most_frequent_words(text):
    dict_counter = dict()
    word = ''
    for char in text:
        low_char = char.lower()
        if low_char.isalpha():
            word = word + low_char
        else:
            if word:
                dict_counter.setdefault(word, 0)
                dict_counter[word] += 1
            word = ''

    sort_words = sorted(dict_counter, key=dict_counter.get, reverse=True)
    return_dict = dict()
    for i in range(10):
        return_dict[sort_words[i]] = dict_counter[sort_words[i]]
    return return_dict


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Input path to the text file second argument")
        exit()
    filepath = sys.argv[1]
    if not os.path.exists(filepath):
        print("Incorrect path")
        exit()
    text = load_data(filepath)
    ret_words = get_most_frequent_words(text)
    sort_words = sorted(ret_words, key=ret_words.get, reverse=True)
    for word in sort_words:
        print(word, ret_words[word])
