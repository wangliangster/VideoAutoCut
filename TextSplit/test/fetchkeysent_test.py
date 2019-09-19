import codecs

from TextSplit.textrank4zh import TextRank4Sentence

sample = codecs.open('./data/01.txt', encoding='utf-8').read()

tr4s = TextRank4Sentence()

tr4s.analyze(text=sample, lower=True, source='all_filters')

for s in tr4s.sentences:
    print(s)

print(20 * '*', 'Key Sentences', 20 * '*')

for ks in tr4s.get_key_sentences(num=5, sentence_min_len=4):
    print(ks.sentence, ks.weight)
