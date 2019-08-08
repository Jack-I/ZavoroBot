import random

# Open pre-filtered file with messages from one user-only (mostly :)
with open("Uras_speech.txt", "r", encoding='utf-8') as f:
    content = f.readlines()


def rand_uri():
    """
    rand_uri -> string

    Chooses one random message from 4 to 31 digits length from Uras_speech.txt
    :return: one random message
    """
    i = random.randint(0, len(content) - 1)
    a = content[i]
    if 4 < len(a) < 31:  # length of message: from 3 to 30 characters
        return a
    else:
        return rand_uri()
