import jieba

jieba.load_userdict("./data/userdict.txt")

import jieba.posseg as pseg

words = pseg.cut('江西省九江瑞昌市洪一乡麦良村三组， 今天发生了一件大事，。。。#')

for w in words:
    print("{0} ---{1}".format(w.word, w.flag))

print(type(w.flag))
