import codecs
import os

from config import Config
from util import *


def prepocess(raw_corpus_file_name, result_file_name):
    post_symbol = "- -"
    response_symbol = "  -"

    raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=Config.encoding, errors="replace")
    result_file = codecs.open(result_file_name, "a", encoding=Config.encoding)

    post = None

    for index, line in enumerate(raw_corpus_file):
        if index % 100000 == 0:
            print(raw_corpus_file_name, index)
        if line.startswith(post_symbol):
            post = line.lstrip(post_symbol).strip()
        elif line.startswith(response_symbol):
            if post:
                response = line.lstrip(response_symbol).strip()
                result_file.write(post + "\t" + response + "\n")

    raw_corpus_file.close()
    result_file.close()


def chatterbot_process_pipeline():
    print("chatterbot_process_pipeline")

    raw_root = Config.raw_chatterbot_corpus_root
    result_file_name = os.path.join(Config.clean_chat_corpus_root, "chatterbot.tsv")
    if os.path.exists(result_file_name):
        os.remove(result_file_name)
    for file_name in os.listdir(raw_root):
        raw_corpus_file_name = os.path.join(raw_root, file_name)
        prepocess(raw_corpus_file_name, result_file_name)

    format_refine(result_file_name)
