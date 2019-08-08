"""
This script clears target message history from various garbage and all other users
messages, except one, your busy friend's.

First, you have to open group, save message history
"""

content = []
for i in range(1, 13):  # read all group message history files, one after another
    mes = "C:\\Users\Jack\Documents\Jupyter_Notebook\\messages\messages{}.html".format(i)
    # TODO: перенести в папку и указать относ. путь
    with open(mes, 'r', encoding='utf-8') as f:
        content += f.readlines()
# content - содержимое html файла с сообщениями

i = 0
while i < len(content):
    # удаляем html-тэги, пробелы, таймстампы, инициалы, "In reply to", "Video message"
    # прикрепы, цифры
    if content[i].lstrip().startswith("<") or content[i] == "\n" or content[i][0].isdigit() or \
            len(content[i]) <= 3 or content[i].startswith("In reply to") or \
            content[i].startswith("Video message") or content[i].endswith("png\n") or \
            any(map(str.isdigit, content[i])): #есть ли цифры в строке
        del content[i]
    else:
        i += 1

# в итоге в content - переписка без тегов и пустых строк

# теперь перекидываем из content в result только Юрины фразы
result = []
exceptions = ("Photo\n", "Sticker\n", "Евгений Петухов\n", "Егор Егоров\n", "Юрий Заворотный\n", \
              "Jack \n", "Илья Рыжий\n", "Саня Осокин\n", "Location\n", "Voice message\n", \
              "Video file\n", "Даша Чилякова\n", "Юля Матрехина\n", "💥💥💥\n")
for i, line in enumerate(content):
    if content[i] == "Юрий Заворотный\n" and content[i + 1] not in exceptions:
        result.append(content[i + 1])  # записываем все реплики Юры в result

# from pprint import pprint
# pprint(result) #чтобы красиво посмотреть, что в result'e

with open("Uras_speech.txt", "w+", encoding='utf-8') as f:
    f.writelines(result)
    # Uras_speech.txt - файл c репликами Юры

del result, content
