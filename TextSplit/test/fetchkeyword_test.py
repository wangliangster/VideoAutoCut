import codecs

from TextSplit.textrank4zh import TextRank4Keyword

sample = codecs.open('./data/03.txt', 'r', 'utf-8', 'ignore').read()

tr4ke = TextRank4Keyword()

tr4ke.analyze(text=sample, window=3, lower=True, pagerank_config={'alpha': 0.85})

for item in tr4ke.get_keywords(num=10, word_min_len=1):
    print(item.word, item.weight)

print(20 * '*', 'Keyphrase', 20 * '*')

for phrase in tr4ke.get_keyphrases(20, 1):
    print(phrase)
