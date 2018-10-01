from operator import itemgetter
import matplotlib.pyplot as plt
import extract_json_data


def occurrences(input_list):
    unique = set(input_list)
    dictionary = {}
    for i in unique:
        dictionary[i] = 0
    for i in input_list:
        dictionary[i] += 1

    return sorted(list(dictionary.items()), key=itemgetter(1))


def bar_graph(list_of_tups):
    x = []
    y = []
    for t in list_of_tups:
        if t[0] is not None and t[1] is not None:
            x.append(t[0])
            y.append(t[1])

    font = {'family': 'monospace',
            'weight': 'normal',
            'size': 8}
    plt.rc('font', **font)

    plt.bar(x, y)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def get_index(list_of_tups, search_term):
    for i in range(len(list_of_tups)):
        if list_of_tups[i][0] == search_term:
            return i


extracted_data = extract_json_data.extract('result.json')
date_list = extracted_data[0]
from_list = extracted_data[1]
message_list = extracted_data[2]

generate_messagecount_graph = True
generate_wordcount_graph = False

if generate_messagecount_graph:
    message_leaderboard = list(reversed(occurrences(from_list)))
    bar_graph(message_leaderboard)

if generate_wordcount_graph:
    words_split = []
    for i in message_list:
        message_split = i.split(' ')
        for j in message_split:
            words_split.append(j.lower())

    most_used_words = list(reversed(occurrences(words_split)))
    bar_graph(most_used_words[:50])
    #bar_graph(most_used_words[get_index(most_used_words, 'lmao'):get_index(most_used_words, 'lmao')+50])
