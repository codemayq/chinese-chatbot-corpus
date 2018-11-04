import codecs
import os
from config import *
from util import check_file_encoding, generate_single_pairs_from_multi_turn, check_format

def total_format_check():
    for file_name in os.listdir(result_root):
        print(file_name)
        raw_corpus_file_name = os.path.join(result_root, file_name)
        os.system("wc -l " + raw_corpus_file_name)

        # check_format(raw_corpus_file_name)


def special_words_filter():
    pass


def rule_filter():
    pass


if __name__ == '__main__':
    total_format_check()
