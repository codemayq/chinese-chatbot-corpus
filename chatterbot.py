import codecs
import os
from config import *
from util import *


def prepocess(raw_corpus_file_name, result_file_name):
    post_symbol = "- -"
    response_symbol = "  -"

    raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=encoding, errors="replace")
    result_file = codecs.open(result_file_name, "a", encoding=encoding)

    post = None

    for index, line in enumerate(raw_corpus_file):
        if index % 10000 == 0:
            print(index)
        if line.startswith(post_symbol):
            post = line.lstrip(post_symbol).strip()
        elif line.startswith(response_symbol):
            if post:
                response = line.lstrip(response_symbol).strip()
                result_file.write(post + "\t" + response + "\n")

    raw_corpus_file.close()
    result_file.close()


if __name__ == '__main__':
    root = r"C:\Users\mayongqiang\Desktop\corpus\chat\chatterbot-1k\chinese"
    result_file_name = os.path.join(result_root, "chatterbot.tsv")
    if os.path.exists(result_file_name):
        os.remove(result_file_name)
    for file_name in os.listdir(root):
        print(file_name)
        raw_corpus_file_name = os.path.join(root, file_name)
        prepocess(raw_corpus_file_name, result_file_name)

    format_refine(result_file_name)

