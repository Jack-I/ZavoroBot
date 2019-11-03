"""
This script clears target message history from various garbage and all other users
messages, except one, your busy friend's.
"target" variable should contain the name of your busy friend.

First, you have to open group chat and save message history to some local folder.
Then you need to rename a first file (messages.html) to messages1.html
After that just fill "mes" variable with the path to your folder with chat history. (don't
change "messages{i}.html" at the end). Also, fill "max_file" variable with the maximum X listed
in your messagesX.html
It will iterate through all html files, cleaning them and save the result in Uras_speech.txt
"""

content = []
max_file = 16
target = "Юрий Заворотный\n"
for i in range(1, max_file+1):  # read all group message history files, one after another
    mes = f'messages/messages{i}.html'

    with open(mes, 'r', encoding='utf-8') as f:
        content += f.readlines()
# var content - contain the text of all html files now

i = 0
print('Cleaning service info:')
while i < len(content):
    # deleting html-tags, whitespaces, timestamps, initials, "In reply to", "Video message"
    # attached stuff, strings with any numerals
    if content[i].lstrip().startswith("<") or content[i] == "\n" or content[i][0].isdigit() or \
            len(content[i]) <= 3 or content[i].startswith("In reply to") or \
            content[i].startswith("Video message") or content[i].endswith("png\n") or \
            any(map(str.isdigit, content[i])):  # check for containing any numeral
        del content[i]
    else:
        i += 1
        if (not i%500):
            print(".", end='')

# var "content" - contains purified messages
print("\nDone.\nNow cleaning from other user's messages:")
# now move only target-human messages from var "content" to var "result"
result = []
# TODO: scan not only first target's message in the sequence
exceptions = ("Photo\n", "Sticker\n", "Евгений Петухов\n", "Егор Егоров\n", \
              "Jack \n", "Илья Рыжий\n", "Саня Осокин\n", "Location\n", "Voice message\n", \
              "Video file\n", "Даша Чилякова\n", "Юля Матрехина\n", "💥💥💥\n")
for i, line in enumerate(content):
    if content[i] == target and content[i + 1] not in exceptions:
        result.append(content[i + 1])  # adding every message from our target to var "result"
    if (not i % 500):
        print(".", end='')

# from pprint import pprint
# pprint(result)  # if you want to see content of var "result" on the screen in a nice way

with open("Uras_speech.txt", "w+", encoding='utf-8') as f:
    f.writelines(result)
    # Uras_speech.txt - file with target's speech

del result, content
