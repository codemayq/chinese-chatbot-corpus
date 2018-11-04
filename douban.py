import codecs
import os
from config import *
from util import *


def prepocess(raw_corpus_file_name, result_file_name, single_result_file_name):
    positive_label = "1"
    negative_label = "0"

    raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=encoding, errors="replace")
    result_file = codecs.open(result_file_name, "a", encoding=encoding)
    single_result_file = codecs.open(single_result_file_name, "a", encoding=encoding)

    session_lengths = []

    for index, line in enumerate(raw_corpus_file):
        if index % 10000 == 0:
            print(index)
        if line.startswith(positive_label):
            label_and_utterances = line.strip().split("\t")
            utterances = label_and_utterances[1:]
            pairs = generate_single_pairs_from_multi_turn(utterances)
            single_result_file.write("\t".join(pairs[0]) + "\n")
            for pair in pairs:
                result_file.write("\t".join(pair) + "\n")
            session_lengths.append(len(utterances))

    print("avg session length", sum(session_lengths) / len(session_lengths))
    raw_corpus_file.close()
    result_file.close()


if __name__ == '__main__':
    root = r"C:\Users\mayongqiang\Desktop\corpus\chat\douban-100w-multiturn"
    data_types = ["train", "dev", "test"]
    result_file_name = os.path.join(result_root, "douban.tsv")
    single_result_file_name = os.path.join(result_root, "single_douban.tsv")

    if os.path.exists(result_file_name):
        os.remove(result_file_name)
    for data_type in data_types:
        print(data_type)
        raw_corpus_file_name = os.path.join(root, data_type + ".txt")
        prepocess(raw_corpus_file_name, result_file_name, single_result_file_name)

    format_refine(result_file_name)
    format_refine(single_result_file_name)
