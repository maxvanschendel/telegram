import json
from operator import itemgetter
import matplotlib.pyplot as plt

json_file = open('result.json',encoding='utf-8')
json_data = json.loads(json_file.read())
messages=json_data['chats']['list'][0]['messages']

from_list=[]
message_list=[]
date_list=[]

for m in range(len(messages)):
    if messages[m]['type'] == 'message':
        date = messages[m]['date']
        sender = messages[m]['from']
        message = messages[m]['text']

        if type(message) == str:
            date_list.append(date)
            from_list.append(sender)
            message_list.append(message)

        else:
            for i in range(len(message)):
                if type(message[i]) == dict:
                    message[i] = message[i]['text']

            date_list.append(date)
            from_list.append(sender)
            message_list.append(''.join(message))

json_file.close()

def occurrences(list):
    unique = set(list)
    dictionary = {}
    for i in unique:
        dictionary[i] = 0
    for i in list:
        dictionary[i] += 1
    return dictionary


message_leaderboard = list(reversed(sorted(list(occurrences(from_list).items()),key=itemgetter(1))))

words_split = []
for i in message_list:
    message_split = i.split(' ')
    for j in message_split:
        words_split.append(j.lower())


#print(words_split)
most_used_words = list(reversed(sorted(list(occurrences(words_split).items()),key=itemgetter(1))))

def bar_graph(list_of_tups):
    x = []
    y = []
    for i in list_of_tups:
        if i[0] != None and i[1] != None:
            x.append(i[0])
            y.append(i[1])

    font = {'family': 'monospace',
            'weight': 'normal',
            'size': 8}
    plt.rc('font', **font)
    plt.bar(x,y)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


#bar_graph(message_leaderboard)
def get_index(list_of_tups, search_term):
    for i in range(len(list_of_tups)):
        if list_of_tups[i][0] == search_term:
            return i
        print(i+1,list_of_tups[i+1])


bar_graph(most_used_words[get_index(most_used_words, 'stash'):125])