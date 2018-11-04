import os

from config import Config
from process_pipelines.chatterbot import chatterbot_process_pipeline
from process_pipelines.douban import douban_process_pipeline
from process_pipelines.ptt import ptt_process_pipeline
from process_pipelines.qingyun import qingyun_process_pipeline
from process_pipelines.subtitle import subtitle_process_pipeline
from process_pipelines.tieba import tieba_process_pipeline
from process_pipelines.weibo import weibo_process_pipeline
from process_pipelines.xiaohuangji import xiaohuangji_process_pipeline


def process_all_corpus():
    if not os.path.exists(Config.clean_chat_corpus_root):
        os.mkdir(Config.clean_chat_corpus_root)

    douban_process_pipeline()
    chatterbot_process_pipeline()
    ptt_process_pipeline()
    qingyun_process_pipeline()
    subtitle_process_pipeline()
    tieba_process_pipeline()
    weibo_process_pipeline()
    xiaohuangji_process_pipeline()


if __name__ == '__main__':
    process_all_corpus()
