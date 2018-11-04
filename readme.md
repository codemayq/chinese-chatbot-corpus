# 说明
该库是对目前市面上已有的开源中文聊天语料的搜集和系统化整理工作

该库搜集了包含
- chatterbot
- 豆瓣多轮
- PTT八卦语料
- 青云语料
- 电视剧对白语料
- 贴吧论坛回帖语料
- 微博语料
- 小黄鸡语料

共8个公开闲聊常用语料和短信，白鹭时代问答等语料。

并对8个常见语料的数据进行了统一化规整和处理，达到直接可以粗略使用的目的。
# 环境
python3
# 处理过程
将各个来源的语料按照其原格式进行提取，提取后进行繁体字转换，然后统一变成一轮一轮的对话。
# 数据来源及说明
语料名称 | 语料数量 | 语料来源说明 | 语料特点 | 语料样例 | 是否已分词
---|---|---|---|---|---
chatterbot | 560 | 开源项目 | 按类型分类，质量较高  | Q:你会开心的 A:幸福不是真正的可预测的情绪。 | 否
douban（豆瓣多轮） | 352W | 来自北航和微软的paper, 开源项目 | 噪音相对较少，原本是多轮（平均7.6轮）  | Q:烟台 十一 哪 好玩 A:哪 都 好玩 · · · · | 是
ptt（PTT八卦语料） | 40W | 开源项目，台湾PTT论坛八卦版 | 繁体，语料较生活化，有噪音  | Q:为什么乡民总是欺负国高中生呢QQ	A:如果以为选好科系就会变成比尔盖兹那不如退学吧  | 否
qingyun（青云语料） | 10W | 某聊天机器人交流群 | 相对不错，生活化  | Q:看来你很爱钱 	 A:噢是吗？那么你也差不多了 | 否
subtitle（电视剧对白语料） | 274W | 开源项目，来自爬取的电影和美剧的字幕 | 有一些噪音，对白不一定是严谨的对话，原本是多轮（平均5.3轮）  | Q:京戏里头的人都是不自由的	A:他们让人拿笼子给套起来了了 | 否
tieba（贴吧论坛回帖语料） | 232W | 偶然找到的 | 多轮，有噪音  | Q:前排，鲁迷们都起床了吧	A:标题说助攻，但是看了那球，真是活生生的讽刺了 | 否
weibo（微博语料） | 443W | 来自华为的paper | 仍有一些噪音  | Q:北京的小纯洁们，周日见。#硬汉摆拍清纯照# A:嗷嗷大湿的左手在干嘛，看着小纯洁撸么。 | 否
xiaohuangji（小黄鸡语料） | 45W | 原人人网项目语料 | 有一些不雅对话，少量噪音 | Q:你谈过恋爱么	A:谈过，哎，别提了，伤心..。 | 否

语料名称 | 语料URL 
---|---
chatterbot | https://github.com/gunthercox/chatterbot-corpus/tree/master/chatterbot_corpus/data/chinese
douban（豆瓣多轮） | https://github.com/MarkWuNLP/MultiTurnResponseSelection 
ptt（PTT八卦语料）| https://github.com/zake7749/Gossiping-Chinese-Corpus 
qingyun（青云语料） | 无 
subtitle（电视剧对白语料） | https://github.com/fateleak/dgk_lost_conv 
tieba（贴吧论坛回帖语料）  | https://pan.baidu.com/s/1mUknfwy1nhSM7XzH8xi7gQ 密码:i4si 
weibo（微博语料）  | 61.93.89.94/Noah_NRM_Data/ 
xiaohuangji（小黄鸡语料） | https://github.com/candlewill/Dialog_Corpus 


# 使用方法
下载语料 https://pan.baidu.com/s/1szmNZQrwh9y994uO8DFL_A  提取码：f2ex

将解压后的raw_chat_corpus文件夹放到当前目录下
目录结构为
```
raw_chat_corpus
-- language
-- process_pipelines
-- raw_chat_corpus
---- chatterbot-1k
---- douban-multiturn-100w
---- ....
-- main.py
-- ...
```
执行命令即可
```bash
python main.py
```
或者
```bash
python3 main.py
```
# 生成结果
每个来源的语料分别生成一个独立的*.tsv文件，都放在新生成的clean_chat_corpus文件夹下。

生成结果格式为 tsv格式，每行是一个样本，先是query，再是answer
```
query \t answer
```
# 结果的使用
这个就根据每个人不同的情况自主使用即可

# 版权说明
本项目为非商业项目，为纯搜集和汇总资料，如有侵权，请在issue下留言。
