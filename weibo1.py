import codecs
import os
from config import *
from util import *


def preprocess(raw_corpus_post_file_name, raw_corpus_response_file_name, result_file_name):
    raw_corpus_post_file = codecs.open(raw_corpus_post_file_name, encoding=encoding)
    raw_corpus_response_file = codecs.open(raw_corpus_response_file_name, encoding=encoding)

    result = codecs.open(result_file_name, "w", encoding=encoding)

    for index, pair in enumerate(zip(raw_corpus_post_file, raw_corpus_response_file)):
        if index % 10000 == 0:
            print(index)

        post = pair[0].strip().replace(" ","")
        response = pair[1].strip().replace(" ","")

        result.write(post + "\t" + response + "\n")

    raw_corpus_post_file.close()
    raw_corpus_response_file.close()
    result.close()


if __name__ == '__main__':
    raw_corpus_post_file_name = r"C:\Users\mayongqiang\Desktop\corpus\chat\weibo1-400w\stc_weibo_train_post"
    raw_corpus_response_file_name = r"C:\Users\mayongqiang\Desktop\corpus\chat\weibo1-400w\stc_weibo_train_response"
    result_file_name = os.path.join(result_root, "weibo.tsv")

    preprocess(raw_corpus_post_file_name, raw_corpus_response_file_name, result_file_name)
    format_refine(result_file_name)

