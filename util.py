import codecs

import chardet

from config import Config


def str_q2b(s):
    res = ""
    for u in s:
        c = ord(u)
        if c == 12288:
            c = 32
        elif 65281 <= c <= 65374:
            c -= 65248
        res += chr(c)
    return res


def check_file_encoding(file_name):
    f = open(file_name, 'rb')
    data = f.read()
    detect_result = chardet.detect(data)
    print(detect_result)
    return detect_result


def generate_single_pairs_from_multi_turn(utterances):
    pairs = []
    for index in range(len(utterances) - 1):
        pairs.append((utterances[index], utterances[index + 1]))
    return pairs


def check_format(file_name):
    file = codecs.open(file_name, encoding=Config.encoding)
    for index, line in enumerate(file):
        pair = line.split("\t")
        if not len(pair) == 2:
            print("error", file_name)
            print(line, index, len(pair))
            break

    file.close()


def format_refine(file_name):
    file = codecs.open(file_name, encoding=Config.encoding)
    valid_lines = []
    for index, line in enumerate(file):
        pair = line.split("\t")
        if len(pair) == 2:
            valid_lines.append(line)
    file.close()

    file = codecs.open(file_name, "w", encoding=Config.encoding)
    for line in valid_lines:
        file.write(line)
    file.close()
