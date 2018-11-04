import codecs
import os

from config import Config
from util import *


def prepocess(raw_corpus_file_name, result_file_name, single_result_file_name):
    positive_label = "1"
    negative_label = "0"

    raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=Config.encoding, errors="replace")
    result_file = codecs.open(result_file_name, "a", encoding=Config.encoding)
    single_result_file = codecs.open(single_result_file_name, "a", encoding=Config.encoding)

    session_lengths = []

    for index, line in enumerate(raw_corpus_file):
        if index % 100000 == 0:
            print(raw_corpus_file_name, index)
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


def douban_process_pipeline():
    print("douban_process_pipeline")

    data_types = ["train", "dev", "test"]
    multi_result_file_name = os.path.join(Config.clean_chat_corpus_root, "douban.tsv")
    single_result_file_name = os.path.join(Config.clean_chat_corpus_root, "douban_single_turn.tsv")

    if_need_multi = False

    if os.path.exists(multi_result_file_name):
        os.remove(multi_result_file_name)

    if os.path.exists(multi_result_file_name):
        os.remove(single_result_file_name)

    for data_type in data_types:
        raw_corpus_file_name = os.path.join(Config.raw_douban_corpus_root, data_type + ".txt")
        prepocess(raw_corpus_file_name, multi_result_file_name, single_result_file_name)

    format_refine(multi_result_file_name)
    format_refine(single_result_file_name)

    if if_need_multi is False and os.path.exists(multi_result_file_name):
        os.remove(multi_result_file_name)
