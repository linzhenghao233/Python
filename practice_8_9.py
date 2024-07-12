#8.9
def show_messages(messages):
    for message in messages:
        print(message)

sayhi = ['hi', 'hello', 'How are you']
show_messages(sayhi)

#8.10
def send_messages(list1, list2):
    while list1:
        temp = list1.pop()
        print(temp)
        list2.append(temp)

sent_messages = []
send_messages(sayhi, sent_messages)
for message in sayhi:
    print(message)
for message in sent_messages:
    print(message)

#8.11
sayhi = ['hi', 'hello', 'How are you']
def send_messages(list1, list2):
    while list1:
        temp = list1.pop()  #for加pop会出bug，pop缩短了列表的长度导致提前结束循环
        print(temp)
        list2.append(temp)

sent_messages = []
send_messages(sayhi[:], sent_messages)
for message in sayhi:
    print(message)
for message in sent_messages:
    print(message)