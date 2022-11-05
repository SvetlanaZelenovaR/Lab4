from random import randint


def generator():
    start = randint(1, 19)
    end = start + 7

    if start < 10:
        Key = '0' + str(start) + ' '
    else:
        Key = str(start) + ' '

    for i in range(1, 8):
        Key += chr(randint(start + 64, end + 64))

    if end < 10:
        Key += ' ' + '0' + str(end)
    else:
        Key += ' ' + str(end)

    return Key
