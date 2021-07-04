import codecs
import os
import csv
from config import Config
from language.langconv import *
from util import *

def prepocess_v1(raw_corpus_file_name, result_file_name):
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

def prepocess_v2(raw_corpus_file_name, result_file_name):
    raw_corpus_file = codecs.open(raw_corpus_file_name, encoding=Config.encoding, errors="replace")
    result_file = codecs.open(result_file_name, "w", encoding=Config.encoding)
    csv_raw_corpus = csv.DictReader(raw_corpus_file)
    for index, line in enumerate(csv_raw_corpus):
        if index % 100000 == 0:
            print(raw_corpus_file_name, index)
        question = line["question"]
        answer = line["answer"]
        if "沒有資料" in question or "沒有資料" in answer:
            continue

        question = tradition2simple(question)
        answer = tradition2simple(answer)

        result_file.write("\t".join([question, answer]) + "\n")

    raw_corpus_file.close()
    result_file.close()


def ptt_process_pipeline():
    print("ptt_process_pipeline")

    raw_corpus_file_name_v1 = Config.raw_ptt_corpus_path_v1
    raw_corpus_file_name_v2 = Config.raw_ptt_corpus_path_v2

    result_file_name = os.path.join(Config.clean_chat_corpus_root, "ptt.tsv")
    if os.path.exists(raw_corpus_file_name_v1):
        prepocess_v1(raw_corpus_file_name_v1, result_file_name)
        format_refine(result_file_name)
    elif os.path.exists(raw_corpus_file_name_v2):
        prepocess_v2(raw_corpus_file_name_v2, result_file_name)
        format_refine(result_file_name)
