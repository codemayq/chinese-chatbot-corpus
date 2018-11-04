import os


class Config(object):
    encoding = "utf-8"

    clean_chat_corpus_root = "clean_chat_corpus"
    raw_chat_corpus_root = "raw_chat_corpus"

    raw_chatterbot_corpus_root = os.path.join(raw_chat_corpus_root, "chatterbot-1k", "chinese")
    raw_douban_corpus_root = os.path.join(raw_chat_corpus_root, "douban-multiturn-100w")
    raw_ptt_corpus_path = os.path.join(raw_chat_corpus_root, "ptt-42w", "Gossiping-QA-Dataset.txt")

    raw_qingyun_corpus_path = os.path.join(raw_chat_corpus_root, "qingyun-11w", "12万对话语料青云库.csv")
    raw_subtitle_corpus_path = os.path.join(raw_chat_corpus_root, "subtitle-useless", "dgk_shooter_min.conv")
    raw_tieba_corpus_path = os.path.join(raw_chat_corpus_root, "tieba-305w", "tieba.dialogues")

    raw_weibo_post_corpus_path = os.path.join(raw_chat_corpus_root, "weibo-400w", "stc_weibo_train_post")
    raw_weibo_response_corpus_path = os.path.join(raw_chat_corpus_root, "weibo-400w", "stc_weibo_train_response")

    raw_xiaohuangji_corpus_path = os.path.join(raw_chat_corpus_root, "xiaohuangji-40w", "xiaohuangji50w_nofenci.conv")
