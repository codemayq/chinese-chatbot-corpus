import codecs
import os
import json
from config import *
from util import *


def check_filter(utterance):
    if len(utterance) <= 2:
        return False

    if "\\" in utterance:
        return False

    if len(utterance) <= 5 and (utterance.isalnum()):
        return False

    return True


def prepocess(raw_corpus_file_name, result_file_name):
    raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=encoding, errors="replace")
    result_file = codecs.open(result_file_name, "a", encoding=encoding)

    for index, line in enumerate(raw_corpus_file):
        if index % 1000 == 0:
            print(index)
        line = line.replace("\n", "").replace("\r\n", "").replace("\r", "").replace("\t", "").strip()
        try:
            pair_json = json.loads(line, encoding=encoding)
        except Exception as e:
            continue

        q = pair_json["Q"]
        a = pair_json["A"]
        if isinstance(q, str) and isinstance(a, str):
            q = str_q2b(q).strip()
            a = str_q2b(a).strip()

            if check_filter(q) and check_filter(a):
                result_file.write(q + "\t" + a + "\n")

    raw_corpus_file.close()
    result_file.close()


if __name__ == '__main__':
    root = r"C:\Users\mayongqiang\Desktop\corpus\chat\turing"
    data_types = ["sentences1.txt.qa", "sentences2.txt.qa"]
    result_file_name = os.path.join(result_root, "turing.tsv")
    if os.path.exists(result_file_name):
        os.remove(result_file_name)
    for data_type in data_types:
        print(data_type)
        raw_corpus_file_name = os.path.join(root, data_type)
        prepocess(raw_corpus_file_name, result_file_name)

    format_refine(result_file_name)
