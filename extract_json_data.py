import json


def extract(filename):
    json_file = open(filename,encoding='utf-8')
    json_data = json.loads(json_file.read())
    chat_no = 0
    messages=json_data['chats']['list'][chat_no]['messages']

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
    return date_list, from_list, message_list

