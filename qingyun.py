import codecs
import os
from config import *
from util import *
from language.langconv import *


def prepocess(raw_corpus_file_name, result_file_name):
    raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=encoding, errors="replace")
    result_file = codecs.open(result_file_name, "w", encoding=encoding)

    for index, line in enumerate(raw_corpus_file):
        if index % 10000 == 0:
            print(index)
        if "{" in line or "qq" in line or "菲菲" in line:
            continue
        pair = line.strip().split("|")

        result_file.write("\t".join(pair) + "\n")

    raw_corpus_file.close()
    result_file.close()


if __name__ == '__main__':
    raw_corpus_file_name = r"C:\Users\mayongqiang\Desktop\corpus\chat\qingyun\12万对话语料青云库.csv"
    result_file_name = os.path.join(result_root, "qingyun.tsv")
    prepocess(raw_corpus_file_name, result_file_name)
    format_refine(result_file_name)
