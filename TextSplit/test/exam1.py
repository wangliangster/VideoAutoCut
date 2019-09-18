# -*- encoding:utf-8 -*-
import codecs

from TextSplit.textrank4zh import TextRank4Keyword
from TextSplit.textrank4zh import TextRank4Sentence

text = codecs.open('./data/01.txt', 'r', 'utf-8').read()
tr4ke = TextRank4Keyword()

# you can give a different window to try
tr4ke.analyze(text=text, lower=True, window=2)

print('Keywords：')
for item in tr4ke.get_keywords(20, word_min_len=1):
    print(item.word, item.weight)

print()
print('Key Phrases:：')
for phrase in tr4ke.get_keyphrases(keywords_num=20, min_occur_num=2):
    print(phrase)

tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source='all_filters')

print()
print('Abstraction：')
for item in tr4s.get_key_sentences(num=3):
    print(item.sentence, item.index, item.weight)
