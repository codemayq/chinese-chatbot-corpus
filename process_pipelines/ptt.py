import codecs
import os

from config import Config
from language.langconv import *
from util import *


def prepocess(raw_corpus_file_name, result_file_name):
    raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=Config.encoding, errors="replace")
    result_file = codecs.open(result_file_name, "w", encoding=Config.encoding)

    for index, line in enumerate(raw_corpus_file):
        if index % 100000 == 0:
            print(raw_corpus_file_name, index)

        if "沒有資料" in line:
            continue

        line = tradition2simple(line)

        pair = line.strip().split()

        result_file.write("\t".join(pair) + "\n")

    raw_corpus_file.close()
    result_file.close()


def ptt_process_pipeline():
    print("ptt_process_pipeline")

    raw_corpus_file_name = Config.raw_ptt_corpus_path
    result_file_name = os.path.join(Config.clean_chat_corpus_root, "ptt.tsv")
    prepocess(raw_corpus_file_name, result_file_name)
    format_refine(result_file_name)
