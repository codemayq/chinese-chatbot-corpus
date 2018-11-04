import codecs
import os
from config import *
from util import *

def prepocess(raw_corpus_file_name, result_file_name):
    start_end_symbol = "E"
    utterance_symbol = "M"

    raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=encoding, errors="replace")
    result_file = codecs.open(result_file_name, "w", encoding=encoding)

    single_session = []
    session_lengths = []

    for index, line in enumerate(raw_corpus_file):
        if index % 100000 == 0:
            print(index)
        if line.startswith(start_end_symbol):
            if len(single_session) == 2:
                pairs = generate_single_pairs_from_multi_turn(single_session)
                for pair in pairs:
                    result_file.write("\t".join(pair) + "\n")
                session_lengths.append(len(single_session))
            single_session = []
        elif line.startswith(utterance_symbol):
            line = line[1:].strip()
            utterance = line.strip()
            single_session.append(utterance)
        else:
            print(line, index)

    print("avg session length", sum(session_lengths) / len(session_lengths))
    raw_corpus_file.close()
    result_file.close()


if __name__ == '__main__':
    raw_corpus_file_name = r"C:\Users\mayongqiang\Desktop\corpus\chat\xiaohuangji-40w\xiaohuangji50w_nofenci.conv"
    result_file_name = os.path.join(result_root, "xiaohuangji.tsv")

    prepocess(raw_corpus_file_name, result_file_name)
    format_refine(result_file_name)
